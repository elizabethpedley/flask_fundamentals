from flask import Flask, render_template, request, redirect, session
import random
import datetime

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if session.get('gold') is None:
        session['gold'] = 0
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
    if session.get('log') is None:
        session['log'] = []
    if request.form['action'] == 'farm':
        range_1 = 10
        range_2 = 20
    elif request.form['action'] == 'cave':
        range_1 = 5
        range_2 = 10
    elif request.form['action'] == 'house':
        range_1 = 5
        range_2 = 10
    else:
        range_1 = 0
        range_2 = 50
    winnings = random.randrange(range_1, range_2+1)
    win = random.randrange(1,3)
    if win == 1:
        session['gold'] += winnings
        log = 'Earned {} golds from the {}! '.format(winnings, request.form['action'])
    else:
        session['gold'] -= winnings
        log = 'Entered a {} and lost {} golds... Ouch.. '.format(request.form['action'], winnings)
    log += str(datetime.datetime.now())
    session['log'].append(log)
    return redirect('/')

app.run(debug=True)