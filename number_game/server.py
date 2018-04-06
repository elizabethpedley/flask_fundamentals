from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if session.get('win') is not None:
        if session['win'] == True:
            win = "{} was the number!".format(session['num'])
            session.pop('num')
            session.pop('win')
            return render_template('index.html', guess_show='show',form_show='none',win_show='show', win = win)
        elif session['win'] == 'high':
            win = 'Too High!'
            return render_template('index.html', guess_show='show',form_show='show',win_show='none', win = win)
        else:
            win = 'Too Low!'
            return render_template('index.html', guess_show='show',form_show='show',win_show='none', win = win)
    if session.get('num') is None:
        session['num'] = random.randrange(0, 101)
    return render_template('index.html', guess_show='none',form_show='display',win_show='none')

@app.route('/guess', methods=['POST'])
def guess():
    if session.get('win') is None:
        session['win'] = False
    if request.form['action'] == 'guessing':
        if int(request.form['guess']) == session['num']:
            session['win'] = True
        elif int(request.form['guess']) > session['num']:
            session['win'] = 'high'
        else:
            session['win'] = 'low'
    return redirect('/')

app.run(debug=True)