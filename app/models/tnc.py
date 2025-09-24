"""
Modelo principal TNC (Tratativa de Não Conformidade)
"""

from datetime import datetime
from app import db

class TNC(db.Model):
    """Modelo de TNC (Tratativa de Não Conformidade)"""
    __tablename__ = 'tncs'
    
    id = db.Column(db.Integer, primary_key=True)
    numero_sequencia = db.Column(db.String(20), unique=True, nullable=False, index=True)
    
    # Dados básicos
    data_emissao = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    documento = db.Column(db.String(200))
    descricao = db.Column(db.Text, nullable=False)
    
    # Relacionamentos
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresas.id'), nullable=False)
    projeto_id = db.Column(db.Integer, db.ForeignKey('projetos.id'), nullable=False)
    disciplina_id = db.Column(db.Integer, db.ForeignKey('disciplinas.id'))
    
    # Classificação
    gravidade = db.Column(db.String(20), nullable=False, default='Média')  # Grave, Média, Leve
    status = db.Column(db.String(30), default='Aberta', nullable=False)  # Aberta, Em Reinspeção, Concluída
    
    # Valores financeiros
    valor = db.Column(db.Numeric(15, 2), default=0.0)
    custo_estimado = db.Column(db.Numeric(15, 2), default=0.0)
    
    # Responsáveis
    responsavel_emissor = db.Column(db.String(100))
    responsavel_tratativa = db.Column(db.String(100))
    created_by_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    assigned_to_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    # Datas importantes
    data_reinspeção = db.Column(db.DateTime)
    data_conclusao = db.Column(db.DateTime)
    prazo_limite = db.Column(db.DateTime)
    
    # Observações
    observacoes = db.Column(db.Text)
    tratativa_proposta = db.Column(db.Text)
    tratativa_realizada = db.Column(db.Text)
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relacionamentos para histórico
    historicos = db.relationship('TNHistorico', backref='tnc', lazy='dynamic', cascade='all, delete-orphan')
    anexos = db.relationship('TNAnexo', backref='tnc', lazy='dynamic', cascade='all, delete-orphan')
    
    def get_gravidade_color(self):
        """Retorna cor baseada na gravidade"""
        colors = {
            'Grave': '#dc3545',    # Vermelho
            'Média': '#ffc107',    # Amarelo
            'Leve': '#28a745'      # Verde
        }
        return colors.get(self.gravidade, '#6c757d')
    
    def get_status_color(self):
        """Retorna cor baseada no status"""
        colors = {
            'Aberta': '#dc3545',          # Vermelho
            'Em Reinspeção': '#ffc107',   # Amarelo
            'Concluída': '#28a745'        # Verde
        }
        return colors.get(self.status, '#6c757d')
    
    def is_overdue(self):
        """Verifica se TNC está atrasada"""
        if self.prazo_limite and self.status != 'Concluída':
            return datetime.utcnow() > self.prazo_limite
        return False
    
    def get_days_until_deadline(self):
        """Dias até o prazo limite"""
        if self.prazo_limite:
            delta = self.prazo_limite - datetime.utcnow()
            return delta.days
        return None
    
    def add_historic_entry(self, action, description, user_id=None):
        """Adiciona entrada no histórico"""
        from app.models.tnc_historico import TNHistorico
        historic = TNHistorico(
            tnc_id=self.id,
            action=action,
            description=description,
            user_id=user_id,
            timestamp=datetime.utcnow()
        )
        db.session.add(historic)
        return historic
    
    @staticmethod
    def generate_sequence_number():
        """Gera próximo número de sequência"""
        last_tnc = TNC.query.order_by(TNC.id.desc()).first()
        if last_tnc:
            try:
                last_num = int(last_tnc.numero_sequencia.split('-')[-1])
                return f"TNC-{last_num + 1:06d}"
            except:
                pass
        return "TNC-000001"
    
    def __repr__(self):
        return f'<TNC {self.numero_sequencia}>'


class TNHistorico(db.Model):
    """Histórico de alterações da TNC"""
    __tablename__ = 'tnc_historicos'
    
    id = db.Column(db.Integer, primary_key=True)
    tnc_id = db.Column(db.Integer, db.ForeignKey('tncs.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    action = db.Column(db.String(50), nullable=False)  # Created, Updated, Status Changed, etc.
    description = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    # Relacionamento com usuário
    user = db.relationship('User', backref='tnc_histories')
    
    def __repr__(self):
        return f'<TNHistorico {self.action} - TNC {self.tnc_id}>'


class TNAnexo(db.Model):
    """Anexos da TNC"""
    __tablename__ = 'tnc_anexos'
    
    id = db.Column(db.Integer, primary_key=True)
    tnc_id = db.Column(db.Integer, db.ForeignKey('tncs.id'), nullable=False)
    
    nome_original = db.Column(db.String(200), nullable=False)
    nome_arquivo = db.Column(db.String(200), nullable=False)
    tipo_arquivo = db.Column(db.String(50))
    tamanho = db.Column(db.Integer)
    
    uploaded_by_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    # Relacionamento com usuário
    uploaded_by = db.relationship('User', backref='uploaded_attachments')
    
    def __repr__(self):
        return f'<TNAnexo {self.nome_original}>'