from flask import Flask, render_template, request, redirect  

app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result(): 
    name = request.form['name']
    dojo = request.form['dojo_location']
    language = request.form['favorite_language']
    comment = request.form['comments']
    return render_template('results.html', name=name,dojo=dojo,language=language,comment=comment)


app.run(debug=True) 