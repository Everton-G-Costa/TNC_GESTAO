"""
Modelo de Projeto
"""

from datetime import datetime
from app import db

class Projeto(db.Model):
    """Modelo de projeto no sistema"""
    __tablename__ = 'projetos'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False, index=True)
    codigo = db.Column(db.String(50), unique=True, index=True)
    descricao = db.Column(db.Text)
    
    # Relacionamento com empresa
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresas.id'), nullable=False)
    
    # Datas do projeto
    data_inicio = db.Column(db.Date)
    data_fim_prevista = db.Column(db.Date)
    data_fim_real = db.Column(db.Date)
    
    # Status
    status = db.Column(db.String(50), default='Ativo', nullable=False)  # Ativo, Pausado, Concluído, Cancelado
    
    # Valores
    valor_total = db.Column(db.Numeric(15, 2), default=0.0)
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relacionamentos
    tncs = db.relationship('TNC', backref='projeto', lazy='dynamic')
    
    @property
    def total_tncs(self):
        """Total de TNCs do projeto"""
        return self.tncs.count()
    
    @property
    def tncs_por_gravidade(self):
        """TNCs agrupadas por gravidade"""
        from sqlalchemy import func
        return db.session.query(
            TNC.gravidade,
            func.count(TNC.id).label('count')
        ).filter_by(projeto_id=self.id).group_by(TNC.gravidade).all()
    
    @property
    def valor_total_tncs(self):
        """Valor total das TNCs do projeto"""
        from sqlalchemy import func
        result = db.session.query(func.sum(TNC.valor)).filter_by(projeto_id=self.id).scalar()
        return result or 0.0
    
    def get_progresso(self):
        """Calcula progresso do projeto baseado em datas"""
        if not self.data_inicio or not self.data_fim_prevista:
            return 0
        
        hoje = datetime.now().date()
        if hoje <= self.data_inicio:
            return 0
        elif hoje >= self.data_fim_prevista:
            return 100
        else:
            total_dias = (self.data_fim_prevista - self.data_inicio).days
            dias_passados = (hoje - self.data_inicio).days
            return min(100, max(0, (dias_passados / total_dias) * 100))
    
    def __repr__(self):
        return f'<Projeto {self.nome}>'