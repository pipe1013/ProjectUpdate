from . import auth
from flask import render_template, redirect, flash 
from .forms import LoginForm
import app

#Dependencias para Autenticacion
from flask_login import current_user, login_user, logout_user

#Ruta de Login
@auth.route('/login',
            methods = ['GET', 'POST'])
def login():
    f = LoginForm()
    if f.validate_on_submit():
        #Seleccionar el cliente con el username
        c = app.models.Cliente.query.filter_by(username = f.username.data).first()
        if c is None or not c.check_password(f.password.data):
            return redirect('/clientes/listar')
        else:
            login_user(c , True)
            return redirect('/productos/listar')
    return render_template("login.html", 
                           f = f)
#Ruta de Cierre de Sesion(Logout)
@auth.route('/logout')
def logout():
    logout_user()
    return redirect('/auth/login')