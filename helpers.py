import os
from main import app,db
from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, PasswordField
from models import Games

class FormularioJogo(FlaskForm):
    titulo = StringField('Título do Jogo', [validators.DataRequired(), validators.Length(min=3, max=70)])
    genero = StringField('Gênero', [validators.DataRequired(), validators.Length(min=3, max=30)])
    plataforma = StringField('Plataforma', [validators.DataRequired(), validators.Length(min=3, max=20)])
    adicionar = SubmitField('Adicionar')
    salvar_alteracao = SubmitField('Salvar Alteração')

class FormularioSignIn(FlaskForm):
    nickname = StringField('Nickname',[validators.DataRequired(),validators.Length(min=2,max=8)])
    password = PasswordField('Password',[validators.DataRequired(),validators.Length(min=6,max=100)])    
    sign_in = SubmitField('Sign in')

class SearchForm(FlaskForm):
    search = StringField('Search', validators=[validators.DataRequired()])
    submit = SubmitField('Search')

def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo

    return 'capa_padrao.jpg'

def deleta_capa_antiga(id):
    capa_antiga = recupera_imagem(id)
    if capa_antiga != 'capa_padrao.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH'],capa_antiga))
    
def busca_jogos(plataforma):
    lista_jogos = Games.query.filter_by(platform=plataforma.upper())
    
    return lista_jogos

