from flask import render_template, session, request,flash,redirect,url_for
from main import app
from helpers import FormularioSignIn
from models import Users

@app.route('/login')
def login():
    form = FormularioSignIn()
    return render_template('login.html', form=form)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    form = FormularioSignIn(request.form)
    usuario = Users.query.filter_by(nickname=form.nickname.data).first()

    if usuario:
         if form.password.data == usuario.password:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.name + ' logado com sucesso!') 
            return redirect(url_for('index'))

    flash('Usuario/Senha inválido!')

    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.clear()

    return redirect(url_for('login'))