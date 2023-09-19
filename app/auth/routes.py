from flask_login import login_user, current_user, logout_user
from app.auth import auth
from flask import render_template, redirect , flash
from .forms import LoginForm
import app

@auth.route('/login',  methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #selecciona al cliente por username 
        c = app.models.Cliente.query.filter_by(username = form.username.data).first()
        if c is None or not c.check_password(form.password.data):
            flash("Usuario inexistente o clave invalida")
            return render_template('login.html', form = form)
        #Mensaje de flash de usu
        else: 
            login_user(c, remember=True)
            flash("Bienvenido "+current_user.username)
            return redirect('/productos/listar')
    return render_template('login.html', form = form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect('/auth/login')