from flask import session, render_template, redirect, url_for, flash, request, send_from_directory
from main import app, db
from models import Games, Users
from helpers import recupera_imagem, deleta_capa_antiga
import time

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


    arquivo = request.files['capa_jogo']
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()
    arquivo.save(f'{upload_path}/capa{novo_jogo.id}-{timestamp}.jpg')


    return render_template('adicionar_jogo_pagina.html',titulo_da_pagina=titulo_da_pagina)
    # return redirect(url_for('adicionar_jogo_pagina', adicionados=titulos_novos))

@app.route('/editar_jogo_pagina/<int:id>')
def editar_jogo_pagina(id):
    titulo_da_pagina = 'Editando titulo'
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    
    jogo = Games.query.filter_by(id=id).first()
    capa_jogo = recupera_imagem(id)
    return render_template('editar_jogo_pagina.html', titulo_da_pagina=titulo_da_pagina, jogo=jogo, capa_jogo=capa_jogo)

@app.route('/editar_jogo', methods=['POST',])
def editar_jogo():
    titulo_da_pagina = 'Editando titulo'

    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))

    id_jogo = request.form['id']

    jogo = Games.query.filter_by(id=id_jogo).first()

    jogo.titulo = request.form['titulo']
    jogo.genero = request.form['genero']
    jogo.plataforma = request.form['plataforma']

    db.session.add(jogo)
    db.session.commit()

    arquivo = request.files['capa_jogo']
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()
    deleta_capa_antiga(jogo.id)
    arquivo.save(f'{upload_path}/capa{jogo.id}-{timestamp}.jpg')
    flash('Jogo editado com sucesso!')


    return render_template('editar_jogo_pagina.html', titulo_da_pagina=titulo_da_pagina, jogo=jogo)
    # return redirect(url_for('index'))

@app.route('/remover_jogo/<int:id>')
def remover_jogo(id):

    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))

    Games.query.filter_by(id=id).delete()

    db.session.commit()
    flash('Jogo deletado com sucesso!')

    return redirect(url_for('index'))

@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)