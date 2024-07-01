#importando biblotecas necessárias
from flask import Flask, render_template, request, session, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'estudo'

app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'admin',
        servidor = 'localhost',
        database = 'game_list'
    )

db = SQLAlchemy(app)

class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    titulo = db.Column(db.String(70), nullable=False)
    genero = db.Column(db.String(30), nullable=False)
    plataforma = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

class Users(db.Model):
    nickname = db.Column(db.String(8), primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return '<Name %r>' % self.name

@app.route('/')
def index():
    lista = Games.query.order_by(Games.id)    
    titulo_da_pagina = 'lista de jogos' 
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    else:
        return render_template('index.html', titulo_da_pagina=titulo_da_pagina, lista_de_jogos=lista)

@app.route('/adicionar-jogo-pagina')
def adicionar_jogo_pagina():
    titulo_da_pagina = 'adicinoar novos titulos'
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    return render_template('adicionar_jogo_pagina.html', titulo_da_pagina=titulo_da_pagina)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = Users.query.filter_by(nickname=request.form['nickname']).first()

    if usuario:
         if request.form['password'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nome + ' logado com sucesso!') 
            return redirect(url_for('index'))
    flash('login inválido!')
    return redirect(url_for('login'))

@app.route('/logout', methods=['POST'])
def logout():
    session['usuario_logado'] = None
    return redirect(url_for('login'))

@app.route('/incluir-jogos', methods=['POST'])
def incluir_jogos():
    
    titulo_da_pagina = 'Adicionando titulos'

    titulo = request.form['titulo']
    genero = request.form['genero']
    plataforma = request.form['plataforma']

    jogo = Games.query.filter_by(titulo=titulo).first()

    if jogo and jogo.plataforma == plataforma:
            flash(jogo.titulo + ' já existe na lista ' + jogo.plataforma)
            return render_template('adicionar_jogo_pagina.html',titulo_da_pagina=titulo_da_pagina)

    novo_jogo = Games(titulo=titulo,genero=genero,plataforma=plataforma)

    db.session.add(novo_jogo)
    db.session.commit()

    return render_template('adicionar_jogo_pagina.html',titulo_da_pagina=titulo_da_pagina)
    # return redirect(url_for('adicionar_jogo_pagina', adicionados=titulos_novos))

app.run(host='127.0.0.1', port=5000, debug=True)