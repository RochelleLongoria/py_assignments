from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes


@app.route('/')
def dashboard():
    randomly = random.randint(0,100)
    session['randomly'] = randomly
    print(session)
    return render_template('index.html')

@app.route('/guess', methods = ['POST'])
def guess():
    session['num'] = int(request.form['num'])
    print(request.form)
    return redirect('/') 


if __name__ =="__main__":
    app.run(debug = True)
