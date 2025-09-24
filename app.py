"""
TNC GESTÃO - Sistema Web para Gestão de TNCs
Aplicação principal Flask
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import os
from pathlib import Path

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

def create_app(config_name=None):
    """Factory function to create Flask app"""
    app = Flask(__name__)
    
    # Configure app
    if config_name is None:
        config_name = os.environ.get('FLASK_CONFIG', 'development')
    
    # Basic configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data/tnc_gestao.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Create data directories
    data_dirs = [
        'data/database',
        'data/exports/pdf',
        'data/exports/excel',
        'data/exports/csv',
        'data/backups',
        'data/uploads',
        'static/uploads',
        'static/reports'
    ]
    
    for directory in data_dirs:
        Path(directory).mkdir(parents=True, exist_ok=True)
    
    # Initialize extensions with app
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    
    # Configure login manager
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Por favor, faça login para acessar esta página.'
    login_manager.login_message_category = 'info'
    
    # Register blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    from app.tnc import bp as tnc_bp
    app.register_blueprint(tnc_bp, url_prefix='/tnc')
    
    from app.dashboard import bp as dashboard_bp
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
    
    from app.reports import bp as reports_bp
    app.register_blueprint(reports_bp, url_prefix='/reports')
    
    from app.admin import bp as admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)