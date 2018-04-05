from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'


@app.route('/')
def index():
    if session.get('dont_add') is not None and session['dont_add'] == True:
        session['dont_add'] = False
        return render_template('index.html')
    if session.get('counter') is not None:
        session['counter'] += 1
    else: 
        session['counter'] = 1
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    if request.form['action'] == 'add_2':
        session['counter'] += 2
    elif request.form['action'] == 'reset':
        session['counter'] = 0
    session['dont_add'] = True
    return redirect('/')

app.run(debug=True)