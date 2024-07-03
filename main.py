#importando biblotecas necessárias
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

from views import *

if __name__  == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)