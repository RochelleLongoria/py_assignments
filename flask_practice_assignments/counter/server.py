from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'bubba'


@app.route('/')
def create_count():
    session['session_name'] = 0
    print(f"this is what session is before the if statment {session['session_name']}")
    if 'session_name' in session:
        return redirect('/addone')
    # if 'session_name' in session:
    #     session['session_name'] = session['session_name'] + 1
    #     print('key exists!')
        
    # else:
    #     print("key 'session_name' does NOT exist")
    #     session['session_name'] = 1
        # session['session_name'] = session['session_name'] + 1
    return render_template('index.html')

@app.route('/addone')
def plusOne():
    if 'session_name' in session:
        session['session_name'] += 1
    return render_template('index.html')


# Add Two
@app.route('/addtwo')
def plusTwo():
    if 'session_name' in session:
        session['session_name'] = session['session_name'] + 2
        print('key exists!')
    else:
        print("key 'session_name' does NOT exist")
        session['session_name'] = 0
        session['session_name'] = session['session_name'] + 2
    return render_template('index.html')





@app.route('/destroy' )
def terminator():
    session.clear()
    print('Hasta la vista, baby')
    return redirect('/')



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.