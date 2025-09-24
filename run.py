"""
Aplicação TNC Gestão - Ponto de entrada principal
"""

from app import create_app, db
from app.models.user import User
from app.models.empresa import Empresa
from app.models.tnc import TNC
from app.models.projeto import Projeto
from app.models.disciplina import Disciplina

app = create_app()

@app.shell_context_processor
def make_shell_context():
    """Fornece contexto para shell interativo do Flask"""
    return {
        'db': db,
        'User': User,
        'Empresa': Empresa,
        'TNC': TNC,
        'Projeto': Projeto,
        'Disciplina': Disciplina
    }

@app.cli.command()
def init_db():
    """Inicializar banco de dados com dados de exemplo"""
    db.create_all()
    print("Banco de dados inicializado!")

if __name__ == '__main__':
    app.run(debug=True)