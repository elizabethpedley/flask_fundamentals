from flask import Flask, render_template, request, redirect, flash, session 

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result(): 
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
        return redirect('/')
    elif len(request.form['comments']) < 1:
        flash("Comments cannot be empty!")
        return redirect('/')
    elif len(request.form['comments']) > 120:
        flash("Comments cannot be longer than 120 characters!")
        return redirect('/')
    name = request.form['name']
    dojo = request.form['dojo_location']
    language = request.form['favorite_language']
    comment = request.form['comments']
    return render_template('results.html', name=name,dojo=dojo,language=language,comment=comment)


app.run(debug=True) 