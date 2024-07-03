from main import db

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
