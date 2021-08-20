from app import db

class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    CPF = db.Column(db.String)
    etapaAtual = db.Column(db.String)

    def __init__(self, name, CPF, etapaAtual):
        self.name = name
        self.CPF = CPF
        self.etapaAtual = etapaAtual
    
    def __repr__(self):
        return '<User %r>' % self.id
    