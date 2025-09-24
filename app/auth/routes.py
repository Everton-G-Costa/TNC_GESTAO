"""
Rotas de autenticação e controle de acesso
"""

from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from app.auth import bp
from app import db
from app.models.user import User
from datetime import datetime

@bp.route('/login', methods=['GET', 'POST'])
def login():
    """Página de login"""
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        remember = bool(request.form.get('remember'))
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password) and user.is_active:
            # Atualizar último login
            user.last_login = datetime.utcnow()
            db.session.commit()
            
            login_user(user, remember=remember)
            
            # Redirecionar para página original ou dashboard
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('dashboard.index')
            
            flash(f'Bem-vindo(a), {user.name}!', 'success')
            return redirect(next_page)
        else:
            flash('Usuário ou senha inválidos', 'error')
    
    return render_template('auth/login.html')

@bp.route('/logout')
@login_required
def logout():
    """Logout do usuário"""
    logout_user()
    flash('Você foi desconectado com sucesso', 'info')
    return redirect(url_for('main.index'))

@bp.route('/profile')
@login_required
def profile():
    """Perfil do usuário"""
    return render_template('auth/profile.html')

# Função auxiliar para validar URLs
from urllib.parse import urlparse

def url_parse(url):
    """Parse URL helper"""
    return urlparse(url)