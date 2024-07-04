#importando biblotecas necessárias
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect


csrf = CSRFProtect()

app = Flask(__name__)
app.config.from_pyfile('config.py')

csrf.init_app(app)

db = SQLAlchemy(app)

from views import *

if __name__  == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)