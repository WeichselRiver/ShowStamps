from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'hard to guess'

class GebietSelect(FlaskForm):
    gebiet = StringField('Gebiet')
    submit = SubmitField('Abschicken')

marken = [
    {'Gebiet' : 'Baden',
    'MichNr': 1,
    'Entwertung' : 'o',
    'Farbe': 'b',
    'Anzahl': 1},
       {'Gebiet' : 'Bayern',
    'MichNr': 1,
    'Entwertung' : 'o',
    'Anzahl': 0}

]

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = GebietSelect()
    marken1 = marken
    if request.method == "POST":
        gebiet = form.gebiet.data
        marken1 = [marke for marke in marken if marke['Gebiet'] == gebiet]
        print(marken)
    return render_template('index.html', marken = marken1, form = form)