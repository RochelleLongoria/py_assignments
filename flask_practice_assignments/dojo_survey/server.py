from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def createuser():
    session['your_name'] = request.form['your_name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/results')



@app.route('/results')
def show_user():
    return render_template('resultpage.html')



if __name__ =="__main__":
    app.run(debug = True)