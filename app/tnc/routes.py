"""
Gestão de TNCs - CRUD completo
"""

from flask import render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from sqlalchemy import or_, and_
from datetime import datetime
from app.tnc import bp
from app import db
from app.models.tnc import TNC, TNHistorico, TNAnexo
from app.models.empresa import Empresa
from app.models.projeto import Projeto
from app.models.disciplina import Disciplina

@bp.route('/')
@login_required
def index():
    """Lista de TNCs com filtros e busca"""
    page = request.args.get('page', 1, type=int)
    per_page = 25
    
    # Filtros
    status_filter = request.args.get('status')
    gravidade_filter = request.args.get('gravidade')
    empresa_filter = request.args.get('empresa_id', type=int)
    projeto_filter = request.args.get('projeto_id', type=int)
    search = request.args.get('search', '').strip()
    
    # Query base
    query = TNC.query
    
    # Aplicar filtros
    if status_filter:
        query = query.filter(TNC.status == status_filter)
    
    if gravidade_filter:
        query = query.filter(TNC.gravidade == gravidade_filter)
    
    if empresa_filter:
        query = query.filter(TNC.empresa_id == empresa_filter)
    
    if projeto_filter:
        query = query.filter(TNC.projeto_id == projeto_filter)
    
    if search:
        query = query.filter(or_(
            TNC.numero_sequencia.contains(search),
            TNC.descricao.contains(search),
            TNC.documento.contains(search),
            TNC.observacoes.contains(search)
        ))
    
    # Ordenação
    order_by = request.args.get('order_by', 'created_at')
    order_dir = request.args.get('order_dir', 'desc')
    
    if order_by == 'data_emissao':
        query = query.order_by(TNC.data_emissao.desc() if order_dir == 'desc' else TNC.data_emissao.asc())
    elif order_by == 'gravidade':
        # Ordenar por gravidade: Grave, Média, Leve
        gravidade_order = {'Grave': 1, 'Média': 2, 'Leve': 3}
        query = query.order_by(
            db.case(gravidade_order, value=TNC.gravidade).desc() if order_dir == 'desc' else db.case(gravidade_order, value=TNC.gravidade).asc()
        )
    elif order_by == 'valor':
        query = query.order_by(TNC.valor.desc() if order_dir == 'desc' else TNC.valor.asc())
    else:  # created_at ou padrão
        query = query.order_by(TNC.created_at.desc() if order_dir == 'desc' else TNC.created_at.asc())
    
    # Paginação
    tncs = query.paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    # Dados para dropdowns de filtro
    empresas = Empresa.query.filter_by(ativa=True).order_by(Empresa.nome).all()
    projetos = Projeto.query.filter_by(status='Ativo').order_by(Projeto.nome).all()
    
    return render_template('tnc/index.html',
                         tncs=tncs,
                         empresas=empresas,
                         projetos=projetos,
                         filters={
                             'status': status_filter,
                             'gravidade': gravidade_filter,
                             'empresa_id': empresa_filter,
                             'projeto_id': projeto_filter,
                             'search': search
                         })

@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    """Criar nova TNC"""
    if not current_user.has_permission('create_tnc'):
        flash('Você não tem permissão para criar TNCs', 'error')
        return redirect(url_for('tnc.index'))
    
    if request.method == 'POST':
        try:
            # Gerar número de sequência
            numero_sequencia = TNC.generate_sequence_number()
            
            tnc = TNC(
                numero_sequencia=numero_sequencia,
                descricao=request.form['descricao'],
                empresa_id=request.form['empresa_id'],
                projeto_id=request.form['projeto_id'],
                disciplina_id=request.form.get('disciplina_id') or None,
                gravidade=request.form['gravidade'],
                valor=float(request.form.get('valor', 0) or 0),
                documento=request.form.get('documento'),
                responsavel_emissor=request.form.get('responsavel_emissor'),
                responsavel_tratativa=request.form.get('responsavel_tratativa'),
                observacoes=request.form.get('observacoes'),
                tratativa_proposta=request.form.get('tratativa_proposta'),
                created_by_id=current_user.id
            )
            
            # Data limite (se fornecida)
            prazo_limite = request.form.get('prazo_limite')
            if prazo_limite:
                tnc.prazo_limite = datetime.strptime(prazo_limite, '%Y-%m-%d')
            
            db.session.add(tnc)
            db.session.commit()
            
            # Adicionar entrada no histórico
            tnc.add_historic_entry('Criada', f'TNC criada por {current_user.name}', current_user.id)
            db.session.commit()
            
            flash(f'TNC {numero_sequencia} criada com sucesso!', 'success')
            return redirect(url_for('tnc.view', id=tnc.id))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao criar TNC: {str(e)}', 'error')
    
    # Dados para formulário
    empresas = Empresa.query.filter_by(ativa=True).order_by(Empresa.nome).all()
    projetos = Projeto.query.filter_by(status='Ativo').order_by(Projeto.nome).all()
    disciplinas = Disciplina.query.filter_by(ativa=True).order_by(Disciplina.nome).all()
    
    return render_template('tnc/create.html',
                         empresas=empresas,
                         projetos=projetos,
                         disciplinas=disciplinas)

@bp.route('/<int:id>')
@login_required
def view(id):
    """Visualizar TNC específica"""
    tnc = TNC.query.get_or_404(id)
    
    # Histórico da TNC
    historicos = TNHistorico.query.filter_by(tnc_id=id).order_by(TNHistorico.timestamp.desc()).all()
    
    # Anexos da TNC
    anexos = TNAnexo.query.filter_by(tnc_id=id).order_by(TNAnexo.uploaded_at.desc()).all()
    
    return render_template('tnc/view.html',
                         tnc=tnc,
                         historicos=historicos,
                         anexos=anexos)

@bp.route('/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit(id):
    """Editar TNC"""
    tnc = TNC.query.get_or_404(id)
    
    if not current_user.has_permission('create_tnc') and tnc.created_by_id != current_user.id:
        flash('Você não tem permissão para editar esta TNC', 'error')
        return redirect(url_for('tnc.view', id=id))
    
    if request.method == 'POST':
        try:
            # Salvar valores antigos para histórico
            old_values = {
                'status': tnc.status,
                'gravidade': tnc.gravidade,
                'valor': tnc.valor
            }
            
            # Atualizar campos
            tnc.descricao = request.form['descricao']
            tnc.empresa_id = request.form['empresa_id']
            tnc.projeto_id = request.form['projeto_id']
            tnc.disciplina_id = request.form.get('disciplina_id') or None
            tnc.gravidade = request.form['gravidade']
            tnc.status = request.form['status']
            tnc.valor = float(request.form.get('valor', 0) or 0)
            tnc.documento = request.form.get('documento')
            tnc.responsavel_emissor = request.form.get('responsavel_emissor')
            tnc.responsavel_tratativa = request.form.get('responsavel_tratativa')
            tnc.observacoes = request.form.get('observacoes')
            tnc.tratativa_proposta = request.form.get('tratativa_proposta')
            tnc.tratativa_realizada = request.form.get('tratativa_realizada')
            
            # Data limite
            prazo_limite = request.form.get('prazo_limite')
            if prazo_limite:
                tnc.prazo_limite = datetime.strptime(prazo_limite, '%Y-%m-%d')
            else:
                tnc.prazo_limite = None
            
            # Data de conclusão automática
            if request.form['status'] == 'Concluída' and not tnc.data_conclusao:
                tnc.data_conclusao = datetime.utcnow()
            elif request.form['status'] != 'Concluída':
                tnc.data_conclusao = None
            
            db.session.commit()
            
            # Registrar alterações no histórico
            changes = []
            if old_values['status'] != tnc.status:
                changes.append(f"Status: {old_values['status']} → {tnc.status}")
            if old_values['gravidade'] != tnc.gravidade:
                changes.append(f"Gravidade: {old_values['gravidade']} → {tnc.gravidade}")
            if old_values['valor'] != tnc.valor:
                changes.append(f"Valor: R$ {old_values['valor']} → R$ {tnc.valor}")
            
            if changes:
                tnc.add_historic_entry('Editada', f'Alterações: {"; ".join(changes)}', current_user.id)
                db.session.commit()
            
            flash('TNC atualizada com sucesso!', 'success')
            return redirect(url_for('tnc.view', id=id))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao atualizar TNC: {str(e)}', 'error')
    
    # Dados para formulário
    empresas = Empresa.query.filter_by(ativa=True).order_by(Empresa.nome).all()
    projetos = Projeto.query.filter_by(status='Ativo').order_by(Projeto.nome).all()
    disciplinas = Disciplina.query.filter_by(ativa=True).order_by(Disciplina.nome).all()
    
    return render_template('tnc/edit.html',
                         tnc=tnc,
                         empresas=empresas,
                         projetos=projetos,
                         disciplinas=disciplinas)

@bp.route('/<int:id>/delete', methods=['POST'])
@login_required
def delete(id):
    """Excluir TNC"""
    tnc = TNC.query.get_or_404(id)
    
    if not current_user.is_admin:
        flash('Apenas administradores podem excluir TNCs', 'error')
        return redirect(url_for('tnc.view', id=id))
    
    try:
        numero = tnc.numero_sequencia
        db.session.delete(tnc)
        db.session.commit()
        
        flash(f'TNC {numero} excluída com sucesso!', 'success')
        return redirect(url_for('tnc.index'))
        
    except Exception as e:
        db.session.rollback()
        flash(f'Erro ao excluir TNC: {str(e)}', 'error')
        return redirect(url_for('tnc.view', id=id))

@bp.route('/api/projetos/<int:empresa_id>')
@login_required
def api_projetos_empresa(empresa_id):
    """API para buscar projetos de uma empresa (AJAX)"""
    projetos = Projeto.query.filter_by(empresa_id=empresa_id, status='Ativo').order_by(Projeto.nome).all()
    return jsonify([
        {'id': p.id, 'nome': p.nome}
        for p in projetos
    ])