"""
Modelo de Empresa
"""

from datetime import datetime
from app import db

class Empresa(db.Model):
    """Modelo de empresa no sistema"""
    __tablename__ = 'empresas'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False, index=True)
    cnpj = db.Column(db.String(18), unique=True, index=True)
    
    # Dados de contato
    email = db.Column(db.String(120))
    telefone = db.Column(db.String(20))
    endereco = db.Column(db.Text)
    
    # Status
    ativa = db.Column(db.Boolean, default=True, nullable=False)
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relacionamentos
    tncs = db.relationship('TNC', backref='empresa', lazy='dynamic')
    projetos = db.relationship('Projeto', backref='empresa', lazy='dynamic')
    
    @property
    def total_tncs(self):
        """Total de TNCs da empresa"""
        return self.tncs.count()
    
    @property
    def tncs_abertas(self):
        """TNCs abertas da empresa"""
        return self.tncs.filter_by(status='Aberta').count()
    
    @property
    def tncs_concluidas(self):
        """TNCs concluídas da empresa"""
        return self.tncs.filter_by(status='Concluída').count()
    
    def get_status_display(self):
        """Retorna status para exibição"""
        return "Ativa" if self.ativa else "Inativa"
    
    def __repr__(self):
        return f'<Empresa {self.nome}>'