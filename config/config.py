"""
Configurações da aplicação TNC Gestão
"""

import os
from pathlib import Path

basedir = Path(__file__).parent.parent.absolute()

class Config:
    """Configuração base"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-2025-tnc-gestao'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f'sqlite:///{basedir}/data/tnc_gestao.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configurações de upload
    UPLOAD_FOLDER = basedir / 'static' / 'uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max
    
    # Configurações de relatórios
    REPORTS_FOLDER = basedir / 'static' / 'reports'
    
    # Configurações de email (opcional)
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    
    # Paginação
    POSTS_PER_PAGE = 25
    
    @staticmethod
    def init_app(app):
        """Inicializar configurações específicas do app"""
        pass

class DevelopmentConfig(Config):
    """Configuração de desenvolvimento"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or f'sqlite:///{basedir}/data/tnc_gestao_dev.db'

class ProductionConfig(Config):
    """Configuração de produção"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f'sqlite:///{basedir}/data/tnc_gestao.db'
    
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)
        
        # Configurações específicas de produção
        import logging
        from logging.handlers import RotatingFileHandler
        
        if not app.debug:
            # Logs de arquivo
            if not (basedir / 'logs').exists():
                (basedir / 'logs').mkdir()
            
            file_handler = RotatingFileHandler(
                basedir / 'logs' / 'tnc_gestao.log',
                maxBytes=10240000,  # 10MB
                backupCount=10
            )
            file_handler.setFormatter(logging.Formatter(
                '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
            ))
            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)
            
            app.logger.setLevel(logging.INFO)
            app.logger.info('TNC Gestão startup')

class TestingConfig(Config):
    """Configuração de testes"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False

# Dicionário de configurações
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}