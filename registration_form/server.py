from flask import Flask, render_template, request, redirect, flash, session 
import re

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    email = request.form['email'] 
    f_name = request.form['f_name']
    l_name = request.form['l_name']
    password1 = request.form['password']
    password2 = request.form['c_password']
    allgood = True
    if len(email)<1 or len(f_name)<1 or len(l_name)<1 or len(password1)<1 or len(password2)<1:
        flash("All fields are required and must not be blank")
        allgood = False
    if not f_name.isalpha() or not l_name.isalpha():
        flash("Names cannot contain numbers")
        allgood = False
    if len(password1)<8 or len(password2)<8:
        flash("Passwords must be atleast 8 characters.")
        allgood = False
    if not EMAIL_REGEX.match(email):
        flash("Not a valid email address")
        allgood = False
    if password1 != password2:
        flash("Your passwords do not match")
        allgood = False
    if allgood == True:
        flash("Thanks for submitting your information.")
    return redirect('/')


app.run(debug=True) 