"""
Modelo de Disciplina Técnica
"""

from datetime import datetime
from app import db

class Disciplina(db.Model):
    """Modelo de disciplina técnica"""
    __tablename__ = 'disciplinas'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False, unique=True, index=True)
    codigo = db.Column(db.String(10), unique=True, index=True)
    descricao = db.Column(db.Text)
    
    # Status
    ativa = db.Column(db.Boolean, default=True, nullable=False)
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    # Relacionamentos
    tncs = db.relationship('TNC', backref='disciplina', lazy='dynamic')
    
    @property
    def total_tncs(self):
        """Total de TNCs da disciplina"""
        return self.tncs.count()
    
    def __repr__(self):
        return f'<Disciplina {self.nome}>'