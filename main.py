"""
TNC GESTÃO - Sistema Web para Gestão de TNCs
Sistema principal Flask
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
    
    # User loader for Flask-Login
    from app.models.user import User
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # Register blueprints
    from app.main.routes import bp as main_bp
    app.register_blueprint(main_bp)
    
    from app.auth.routes import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    from app.tnc.routes import bp as tnc_bp
    app.register_blueprint(tnc_bp, url_prefix='/tnc')
    
    from app.dashboard.routes import bp as dashboard_bp
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
    
    # Create sample data if database is empty
    with app.app_context():
        db.create_all()
        
        # Check if we have users
        if User.query.count() == 0:
            from werkzeug.security import generate_password_hash
            
            # Create admin user
            admin = User(
                username='admin',
                email='admin@tnc-gestao.com',
                name='Administrador',
                password_hash=generate_password_hash('admin123'),
                is_admin=True,
                is_inspector=True,
                is_viewer=True
            )
            
            # Create sample inspector
            inspector = User(
                username='inspetor',
                email='inspetor@tnc-gestao.com',
                name='Inspetor TNC',
                password_hash=generate_password_hash('inspetor123'),
                is_inspector=True,
                is_viewer=True
            )
            
            db.session.add(admin)
            db.session.add(inspector)
            
            # Create sample companies
            from app.models.empresa import Empresa
            
            empresas = [
                Empresa(nome='Petrobras S.A.', cnpj='33.000.167/0001-01', email='contato@petrobras.com.br', ativa=True),
                Empresa(nome='Vale S.A.', cnpj='33.592.510/0001-54', email='contato@vale.com', ativa=True),
                Empresa(nome='Construtora ABC Ltda.', cnpj='12.345.678/0001-90', email='contato@abc.com.br', ativa=True),
            ]
            
            for empresa in empresas:
                db.session.add(empresa)
            
            # Create sample disciplines
            from app.models.disciplina import Disciplina
            
            disciplinas = [
                Disciplina(nome='Estruturas', codigo='EST', descricao='Disciplina de estruturas'),
                Disciplina(nome='Elétrica', codigo='ELE', descricao='Disciplina elétrica'),
                Disciplina(nome='Mecânica', codigo='MEC', descricao='Disciplina mecânica'),
                Disciplina(nome='Instrumentação', codigo='INS', descricao='Disciplina de instrumentação'),
                Disciplina(nome='Processo', codigo='PRO', descricao='Disciplina de processo'),
            ]
            
            for disciplina in disciplinas:
                db.session.add(disciplina)
            
            db.session.commit()
            print("✅ Dados de exemplo criados!")
            print("👤 Login Admin: admin / admin123")
            print("👤 Login Inspetor: inspetor / inspetor123")
    
    return app

def show_startup_intro():
    """Exibe introdução na inicialização do sistema"""
    print("=" * 80)
    print("🌐 TNC GESTÃO - SISTEMA WEB DE GESTÃO DE TNCs")
    print("=" * 80)
    print()
    print("🚀 INICIALIZANDO SISTEMA WEB...")
    print("   • Configurando servidor Flask")
    print("   • Inicializando banco de dados SQLite")
    print("   • Preparando dashboard analítico web")
    print("   • Configurando geração de relatórios PDF")
    print("   • Configurando autenticação e controle de acesso")
    print()
    print("📊 FUNCIONALIDADES DISPONÍVEIS:")
    print("   ✅ Dashboard web interativo com gráficos")
    print("   ✅ Gestão completa de TNCs via web")
    print("   ✅ Sistema de autenticação (Admin, Inspetor, Visualizador)")
    print("   ✅ Relatórios PDF profissionais")
    print("   ✅ Importação/Exportação Excel/CSV")
    print("   ✅ API REST para integrações")
    print()
    print("🌐 ACESSO:")
    print("   • URL: http://localhost:5000")
    print("   • Login Admin: admin / admin123")
    print("   • Login Inspetor: inspetor / inspetor123")
    print()
    print("👨‍💻 Sistema Web Responsivo | 📅 Versão 2025.01")
    print("=" * 80)
    print()

if __name__ == '__main__':
    # Exibir introdução
    show_startup_intro()
    
    # Criar aplicação Flask
    app = create_app()
    
    # Executar em modo desenvolvimento
    app.run(debug=True, host='0.0.0.0', port=5000)

import sys
import os
from pathlib import Path

# Adicionar o diretório raiz ao Python path
sys.path.insert(0, str(Path(__file__).parent))

try:
    from PyQt6.QtWidgets import QApplication, QSplashScreen, QMessageBox
    from PyQt6.QtGui import QPixmap, QIcon
    from PyQt6.QtCore import Qt, QTimer
    PYQT_AVAILABLE = True
except ImportError:
    print("❌ PyQt6 não está instalado!")
    print("Execute: pip install PyQt6")
    PYQT_AVAILABLE = False

if PYQT_AVAILABLE:
    try:
        from src.database.connection import DatabaseConnection
        from src.gui.windows.main_window import MainWindow
        from src.gui.widgets.splash_screen import SplashScreen
    except ImportError as e:
        print(f"Erro ao importar módulos: {e}")
        PYQT_AVAILABLE = False


class TNGestaoApp:
    """Classe principal da aplicação TNC Gestão"""
    
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.setup_application()
        
    def setup_application(self):
        """Configura a aplicação"""
        self.app.setApplicationName("TNC Gestão")
        self.app.setApplicationVersion("1.0.0")
        self.app.setOrganizationName("TNC Solutions")
        
        # Configurar ícone da aplicação (se existir)
        icon_path = Path("resources/icons/app/tnc-gestao.ico")
        if icon_path.exists():
            self.app.setWindowIcon(QIcon(str(icon_path)))
        
        # Configurar estilo global
        self.setup_global_style()
    
    def setup_global_style(self):
        """Configura o estilo global da aplicação"""
        style = """
        QApplication {
            font-family: 'Segoe UI', Arial, sans-serif;
            font-size: 9pt;
        }
        
        QMainWindow {
            background-color: #f0f0f0;
        }
        
        QWidget {
            background-color: #ffffff;
        }
        
        QPushButton {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 4px;
            font-weight: bold;
            min-height: 20px;
        }
        
        QPushButton:hover {
            background-color: #2980b9;
        }
        
        QPushButton:pressed {
            background-color: #21618c;
        }
        
        QPushButton:disabled {
            background-color: #bdc3c7;
            color: #7f8c8d;
        }
        
        QMenuBar {
            background-color: #2c3e50;
            color: white;
            border: none;
            padding: 4px;
        }
        
        QMenuBar::item {
            background-color: transparent;
            padding: 8px 12px;
        }
        
        QMenuBar::item:selected {
            background-color: #34495e;
            border-radius: 4px;
        }
        
        QMenu {
            background-color: white;
            border: 1px solid #bdc3c7;
            border-radius: 4px;
            padding: 4px;
        }
        
        QMenu::item {
            padding: 8px 24px;
            border-radius: 4px;
        }
        
        QMenu::item:selected {
            background-color: #3498db;
            color: white;
        }
        
        QToolBar {
            background-color: #34495e;
            border: none;
            spacing: 2px;
            padding: 4px;
        }
        
        QToolBar QToolButton {
            background-color: transparent;
            border: none;
            padding: 8px;
            border-radius: 4px;
            color: white;
            font-size: 14px;
        }
        
        QToolBar QToolButton:hover {
            background-color: #2c3e50;
        }
        
        QStatusBar {
            background-color: #ecf0f1;
            border-top: 1px solid #bdc3c7;
            padding: 4px;
        }
        
        QGroupBox {
            font-weight: bold;
            border: 2px solid #bdc3c7;
            border-radius: 8px;
            margin-top: 12px;
            padding-top: 8px;
            background-color: white;
        }
        
        QGroupBox::title {
            subcontrol-origin: margin;
            left: 12px;
            padding: 0 8px;
            color: #2c3e50;
            background-color: white;
        }
        
        QTableWidget {
            gridline-color: #bdc3c7;
            background-color: white;
            alternate-background-color: #f8f9fa;
            border: 1px solid #bdc3c7;
            border-radius: 4px;
        }
        
        QTableWidget::item {
            padding: 8px;
            border: none;
        }
        
        QTableWidget::item:selected {
            background-color: #3498db;
            color: white;
        }
        
        QHeaderView::section {
            background-color: #34495e;
            color: white;
            border: none;
            padding: 8px;
            font-weight: bold;
        }
        
        QLineEdit, QTextEdit, QComboBox, QDateEdit, QSpinBox, QDoubleSpinBox {
            border: 1px solid #bdc3c7;
            border-radius: 4px;
            padding: 6px;
            background-color: white;
        }
        
        QLineEdit:focus, QTextEdit:focus, QComboBox:focus {
            border-color: #3498db;
            outline: none;
        }
        
        QTabWidget::pane {
            border: 1px solid #bdc3c7;
            border-radius: 4px;
            background-color: white;
        }
        
        QTabBar::tab {
            background-color: #ecf0f1;
            border: 1px solid #bdc3c7;
            padding: 8px 16px;
            margin-right: 2px;
        }
        
        QTabBar::tab:selected {
            background-color: white;
            border-bottom-color: white;
        }
        
        QProgressBar {
            border: 1px solid #bdc3c7;
            border-radius: 4px;
            text-align: center;
            background-color: #ecf0f1;
            min-height: 20px;
        }
        
        QProgressBar::chunk {
            background-color: #27ae60;
            border-radius: 3px;
        }
        """
        
        self.app.setStyleSheet(style)
    
    def show_splash_screen(self):
        """Mostra tela de splash durante a inicialização"""
        splash_path = Path("resources/images/splash_screen.png")
        
        if splash_path.exists():
            pixmap = QPixmap(str(splash_path))
        else:
            # Criar splash simples se não existir imagem
            pixmap = QPixmap(400, 300)
            pixmap.fill(Qt.GlobalColor.white)
        
        splash = QSplashScreen(pixmap)
        splash.show()
        
        # Mostrar mensagens de inicialização
        splash.showMessage("Inicializando TNC Gestão...", Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter)
        self.app.processEvents()
        
        return splash
    
    def initialize_database(self, splash=None):
        """Inicializa o banco de dados"""
        try:
            if splash:
                splash.showMessage("Configurando banco de dados...", Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter)
                self.app.processEvents()
            
            db = DatabaseConnection()
            db.create_tables()
            db.migrate_database()  # Executar migrações necessárias
            db.insert_sample_data()
            
            if splash:
                splash.showMessage("Banco de dados configurado!", Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter)
                self.app.processEvents()
            
            return db
            
        except Exception as e:
            QMessageBox.critical(
                None,
                "Erro de Inicialização",
                f"Erro ao inicializar banco de dados:\n\n{str(e)}\n\nA aplicação será encerrada."
            )
            return None
    
    def run(self):
        """Executa a aplicação"""
        if not PYQT_AVAILABLE:
            print("❌ PyQt6 não está disponível. Executando em modo console...")
            print("Execute: pip install PyQt6")
            return 1
            
        try:
            # Mostrar splash screen
            splash = self.show_splash_screen()
            
            # Pequena pausa para mostrar o splash
            QTimer.singleShot(500, lambda: None)
            self.app.processEvents()
            
            # Inicializar banco de dados
            db = self.initialize_database(splash)
            if not db:
                return 1
            
            # Inicializar janela principal
            if splash:
                splash.showMessage("Carregando interface...", Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter)
                self.app.processEvents()
            
            main_window = MainWindow(db)
            
            # Fechar splash e mostrar janela principal
            if splash:
                splash.finish(main_window)
            
            main_window.show()
            
            # Executar loop principal
            return self.app.exec()
            
        except Exception as e:
            QMessageBox.critical(
                None,
                "Erro Fatal",
                f"Erro inesperado durante a inicialização:\n\n{str(e)}\n\nA aplicação será encerrada."
            )
            return 1


def show_startup_intro():
    """Exibe introdução na inicialização do sistema"""
    print("=" * 80)
    print("🏗️  TNC GESTÃO - SISTEMA DE REGISTROS DE NÃO CONFORMIDADE")
    print("=" * 80)
    print()
    print("🚀 INICIALIZANDO SISTEMA...")
    print("   • Carregando banco de dados SQLite")
    print("   • Configurando interface PyQt6")
    print("   • Preparando dashboard analítico")
    print("   • Configurando geração de relatórios PDF")
    print()
    print("📊 FUNCIONALIDADES DISPONÍVEIS:")
    print("   ✅ Gestão completa de RNCs")
    print("   ✅ Dashboard com 6 gráficos analíticos")
    print("   ✅ Relatórios PDF profissionais")
    print("   ✅ Sistema de tratativas e assinaturas")
    print("   ✅ Categorização por destinatário")
    print()
    print("👨‍💻 Desenvolvido por GitHub Copilot | 📅 Versão 2025.07.23")
    print("=" * 80)
    print()

def main():
    """Função principal"""
    try:
        # Exibir introdução
        show_startup_intro()
        
        # Configurar diretórios necessários
        data_dirs = [
            "data/database",
            "data/exports/pdf",
            "data/exports/excel", 
            "data/exports/csv",
            "data/backups/daily",
            "data/logs",
            "data/temp",
            "data/user_data"
        ]
        
        for directory in data_dirs:
            Path(directory).mkdir(parents=True, exist_ok=True)
        
        if not PYQT_AVAILABLE:
            print("❌ PyQt6 não está disponível")
            print("Execute: pip install PyQt6 reportlab pandas matplotlib pillow")
            return 1
        
        # Criar e executar aplicação
        app = TNGestaoApp()
        return app.run()
        
    except ImportError as e:
        print("❌ Erro de importação:")
        print(f"   {e}")
        print("\n💡 Certifique-se de que as dependências estão instaladas:")
        print("   pip install PyQt6 reportlab pandas matplotlib pillow")
        return 1
        
    except Exception as e:
        print(f"❌ Erro fatal: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
