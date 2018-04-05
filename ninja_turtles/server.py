from flask import Flask, render_template, request, redirect  

app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/ninjas')
def ninjas(): 
    return render_template('ninjas.html')

@app.route('/ninjas/<color>')
def ninja(color):
    if color != 'red' and color != 'blue' and color != 'purple' and color != 'orange':
        ninja = 'notapril'
    elif color == 'blue':
        ninja = 'leonardo'
    elif color == 'red':
        ninja = 'raphael'
    elif color == 'orange':
        ninja = 'michelangelo'
    else:
        ninja = 'donatello'
        
    return render_template('ninja.html', ninja=ninja)




app.run(debug=True) 