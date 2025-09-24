"""
Rotas principais do sistema
"""

from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from app.main import bp

@bp.route('/')
def index():
    """Página inicial - redireciona para dashboard se logado"""
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.index'))
    return render_template('main/index.html')

@bp.route('/sobre')
def about():
    """Página sobre o sistema"""
    return render_template('main/about.html')

@bp.route('/ajuda')
@login_required
def help():
    """Página de ajuda do sistema"""
    return render_template('main/help.html')