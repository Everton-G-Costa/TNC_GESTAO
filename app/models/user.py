"""
Modelo de usuário para sistema de autenticação
"""

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db

class User(UserMixin, db.Model):
    """Modelo de usuário do sistema"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    
    # Perfis de usuário
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    is_inspector = db.Column(db.Boolean, default=False, nullable=False)
    is_viewer = db.Column(db.Boolean, default=True, nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    last_login = db.Column(db.DateTime)
    
    # Relacionamentos
    tncs_created = db.relationship('TNC', foreign_keys='TNC.created_by_id', backref='created_by', lazy='dynamic')
    tncs_assigned = db.relationship('TNC', foreign_keys='TNC.assigned_to_id', backref='assigned_to', lazy='dynamic')
    
    def set_password(self, password):
        """Define senha do usuário com hash"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Verifica senha do usuário"""
        return check_password_hash(self.password_hash, password)
    
    def get_role(self):
        """Retorna o role do usuário"""
        if self.is_admin:
            return 'Administrador'
        elif self.is_inspector:
            return 'Inspetor'
        else:
            return 'Visualizador'
    
    def has_permission(self, permission):
        """Verifica se usuário tem permissão específica"""
        if self.is_admin:
            return True
        elif permission == 'create_tnc' and self.is_inspector:
            return True
        elif permission == 'view_tnc':
            return True
        return False
    
    def __repr__(self):
        return f'<User {self.username}>'