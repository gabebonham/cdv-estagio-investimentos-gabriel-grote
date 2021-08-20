from app import app, db
from flask import render_template, request, redirect, url_for

from app.models.UsersTable import User

@app.route('/', methods=['GET'])
def index():
    clients = User.query.order_by(User.id).all()
    return render_template('index.html', clients=clients)

@app.route('/add', methods=['POST', 'GET'])
def adicionar():
    if request.method == 'POST':
        name1 = request.form['name']
        CPF1 = request.form['CPF']
        etapaAtual1 = request.form['etapaAtual']
        newClient = User(name=name1, CPF=CPF1, etapaAtual=etapaAtual1)
        print('asdf')
        try:
            db.session.add(newClient)
            db.session.commit()
            print('asdf2')
            return redirect('/')
        except:
            return 'There was an error while creating new client.'
    else:
        return render_template('add.html')

@app.route('/delete/<int:id>')
def delete(id):
    clientDelete = User.query.get_or_404(id)

    try:
        db.session.delete(clientDelete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting the client'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    client = User.query.get_or_404(id)

    if request.method == 'POST':
        client.name = request.form['name']
        client.CPF = request.form['CPF']
        client.etapaAtual = request.form['etapaAtual']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was a problem updating client'
    else:
        return render_template('update.html', client=client)