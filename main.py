#importando biblotecas necessárias
from flask import Flask, render_template, request, session, redirect, flash, url_for
from biblioteca import Jogo
from usuario import Usuario

#---
#instanciando 3 objetos da classe importada Jogo
jogo1 = Jogo('The Witcher 3','RPG','GOG Galaxy')
jogo2 = Jogo('Fallout 4','RPG','Steam')
jogo3 = Jogo('Cyber Punk 2077','RPG','GOG Galaxy')

lista = [jogo1, jogo2, jogo3]
titulos_novos = []
#---

#---
#instanciando 3 objetos da classe importada Usuario
usuario1 = Usuario('Roger Alves Rodrigues Melo','roger','denise02')
usuario2 = Usuario('Denise Azevedo da Silva Rodrigues','deh','keka2412')
usuario3 = Usuario('Aylla Vitória Alves Azevedo', 'aylla', 'denise02')

usuarios = {usuario1.nickname:usuario1,
           usuario2.nickname:usuario2,
           usuario3.nickname:usuario3}
#---

app = Flask(__name__)
app.secret_key = 'estudo'

@app.route('/')
def index():
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
    if request.form['nickname'] in usuarios:
        usuario = usuarios[request.form['nickname']]
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

    jogo = Jogo(titulo,genero,plataforma)
    titulos_novos.append(jogo)
    lista.append(jogo)
    
    return render_template('adicionar_jogo_pagina.html',titulo_da_pagina=titulo_da_pagina,adicionados=titulos_novos)
    # return redirect(url_for('adicionar_jogo_pagina', adicionados=titulos_novos))




    # if request.form['nickname'] in usuarios:
    #     if request.form['password'] == usuarios[request.form['nickname']].senha:
    #         usuario = usuarios[request.form['nickname']].nome
    #         session['usuario_logado'] = usuario
    #         flash(usuario + ' Logado com sucesso!')
    #         return redirect(url_for('index'))
    # flash('Login inválido')
    # return redirect(url_for('login'))
   














# @app.route('/')
# def index():
#     titulo_da_pagina = 'biblioteca de games'

#     if 'usuario_logado' not in session or session['usuario_logado'] == None:
#         return redirect(url_for('login', proxima=url_for('index')))
    
#     return render_template('index.html',titulo=titulo_da_pagina, lista_de_jogos=lista)

# @app.route('/login')
# def login():
#     proxima = request.args.get('proxima')

#     return render_template('login.html',proxima=proxima)

# @app.route('/autenticar', methods=['POST',])
# def autenticar():
#     if request.form['nickname'] in usuarios:
#         usuario = usuarios[request.form['nickname']]
#         if request.form['password'] == usuario.senha:
#             session['usuario_logado'] = usuario.nickname
#             flash(usuario.nome + ' logado com sucesso!')
#             proxima_pagina = request.form['proxima']
#             return redirect((proxima_pagina))
#     else:
#         flash('Usuário não encontrado')
#         return redirect(url_for('login'))
        
# @app.route('/logout', methods=['POST',])
# def logout():
#     session['usuario_logado'] = None
#     flash('Logout efetuado com sucesso!')

#     return redirect(url_for('login',proxima=url_for('index')))

# @app.route('/adicionar-jogo', methods=['POST',])
# def adicionar_jogo():
#     titulo = 'adicionar novos titulos'

#     return render_template('adicionar_jogo_pagina.html', titulo=titulo)

# @app.route('/criar-registro', methods=['POST',])
# def criar_registro():
#     titulo = request.form['titulo']
#     genero = request.form['genero']
#     plataforma = request.form['plataforma']

#     jogo = Jogo(titulo,genero,plataforma)
#     lista.append(jogo)

#     flash('Jogo adicionado com sucesso!')

#     return redirect(url_for('adicionar_jogo'))


app.run(host='127.0.0.1', port=5000, debug=True)