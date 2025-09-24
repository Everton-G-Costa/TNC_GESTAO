"""
Dashboard analítico com gráficos e indicadores
"""

from flask import render_template, jsonify, request
from flask_login import login_required, current_user
from sqlalchemy import func
from app.dashboard import bp
from app import db
from app.models.tnc import TNC
from app.models.empresa import Empresa
from app.models.projeto import Projeto
from app.models.disciplina import Disciplina
from datetime import datetime, timedelta

@bp.route('/')
@login_required
def index():
    """Dashboard principal com indicadores e gráficos"""
    
    # Estatísticas gerais
    stats = {
        'total_tncs': TNC.query.count(),
        'tncs_abertas': TNC.query.filter_by(status='Aberta').count(),
        'tncs_reinspeção': TNC.query.filter_by(status='Em Reinspeção').count(),
        'tncs_concluidas': TNC.query.filter_by(status='Concluída').count(),
        'total_empresas': Empresa.query.filter_by(ativa=True).count(),
        'total_projetos': Projeto.query.filter_by(status='Ativo').count(),
    }
    
    # Valor total das TNCs
    valor_total = db.session.query(func.sum(TNC.valor)).scalar() or 0
    stats['valor_total'] = valor_total
    
    # TNCs por gravidade
    tncs_gravidade = db.session.query(
        TNC.gravidade,
        func.count(TNC.id).label('count')
    ).group_by(TNC.gravidade).all()
    
    # TNCs por status
    tncs_status = db.session.query(
        TNC.status,
        func.count(TNC.id).label('count')
    ).group_by(TNC.status).all()
    
    # TNCs por disciplina (top 10)
    tncs_disciplina = db.session.query(
        Disciplina.nome,
        func.count(TNC.id).label('count')
    ).join(TNC).group_by(Disciplina.nome).order_by(func.count(TNC.id).desc()).limit(10).all()
    
    # TNCs por projeto (top 10)
    tncs_projeto = db.session.query(
        Projeto.nome,
        func.count(TNC.id).label('count'),
        func.sum(TNC.valor).label('valor_total')
    ).join(TNC).group_by(Projeto.nome).order_by(func.count(TNC.id).desc()).limit(10).all()
    
    # Evolução mensal das TNCs (últimos 12 meses)
    data_inicio = datetime.now() - timedelta(days=365)
    evolucao_mensal = db.session.query(
        func.strftime('%Y-%m', TNC.data_emissao).label('mes'),
        func.count(TNC.id).label('count')
    ).filter(TNC.data_emissao >= data_inicio).group_by(func.strftime('%Y-%m', TNC.data_emissao)).all()
    
    # TNCs atrasadas
    tncs_atrasadas = TNC.query.filter(
        TNC.prazo_limite < datetime.utcnow(),
        TNC.status != 'Concluída'
    ).count()
    stats['tncs_atrasadas'] = tncs_atrasadas
    
    return render_template('dashboard/index.html',
                         stats=stats,
                         tncs_gravidade=tncs_gravidade,
                         tncs_status=tncs_status,
                         tncs_disciplina=tncs_disciplina,
                         tncs_projeto=tncs_projeto,
                         evolucao_mensal=evolucao_mensal)

@bp.route('/api/chart-data/<chart_type>')
@login_required
def chart_data(chart_type):
    """API para dados dos gráficos (AJAX)"""
    
    if chart_type == 'gravidade':
        data = db.session.query(
            TNC.gravidade,
            func.count(TNC.id).label('count')
        ).group_by(TNC.gravidade).all()
        
        return jsonify({
            'labels': [item[0] for item in data],
            'data': [item[1] for item in data],
            'colors': ['#dc3545', '#ffc107', '#28a745']  # Grave, Média, Leve
        })
    
    elif chart_type == 'status':
        data = db.session.query(
            TNC.status,
            func.count(TNC.id).label('count')
        ).group_by(TNC.status).all()
        
        return jsonify({
            'labels': [item[0] for item in data],
            'data': [item[1] for item in data],
            'colors': ['#dc3545', '#ffc107', '#28a745']  # Aberta, Reinspeção, Concluída
        })
    
    elif chart_type == 'evolucao':
        data_inicio = datetime.now() - timedelta(days=365)
        data = db.session.query(
            func.strftime('%Y-%m', TNC.data_emissao).label('mes'),
            func.count(TNC.id).label('count')
        ).filter(TNC.data_emissao >= data_inicio).group_by(func.strftime('%Y-%m', TNC.data_emissao)).all()
        
        return jsonify({
            'labels': [item[0] for item in data],
            'data': [item[1] for item in data]
        })
    
    return jsonify({'error': 'Tipo de gráfico inválido'}), 400

@bp.route('/api/kpis')
@login_required
def kpis():
    """API para indicadores em tempo real"""
    now = datetime.utcnow()
    
    # Estatísticas básicas
    total_tncs = TNC.query.count()
    tncs_abertas = TNC.query.filter_by(status='Aberta').count()
    tncs_atrasadas = TNC.query.filter(
        TNC.prazo_limite < now,
        TNC.status != 'Concluída'
    ).count()
    
    # Taxa de conclusão
    tncs_concluidas = TNC.query.filter_by(status='Concluída').count()
    taxa_conclusao = (tncs_concluidas / total_tncs * 100) if total_tncs > 0 else 0
    
    # Valor médio por TNC
    valor_total = db.session.query(func.sum(TNC.valor)).scalar() or 0
    valor_medio = (valor_total / total_tncs) if total_tncs > 0 else 0
    
    return jsonify({
        'total_tncs': total_tncs,
        'tncs_abertas': tncs_abertas,
        'tncs_atrasadas': tncs_atrasadas,
        'taxa_conclusao': round(taxa_conclusao, 1),
        'valor_total': float(valor_total),
        'valor_medio': float(valor_medio)
    })