from flask import Flask, render_template 

app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/play')
def play():

    return render_template('levelone.html')

#When a user visits localhost:5000/play/(x), have it display the beautiful looking blue boxes x times. For example, localhost:5000/play/7 should display these blue boxes 7 times. Calling localhost:5000/play/35 would display these blue boxes 35 times. Please remember that x originally is a string, and if you want to use it as an integer, you must first convert it to integer using int(). For example int("7") returns 7.

@app.get('/play/<int:x>')
def playleveltwo(x):
    return render_template('leveltwo.html', number = x)


# When a user visits localhost:5000/play/(x)/(color), have it display beautiful looking boxes x times, but this time where the boxes appear in (color). For example, localhost:5000/play/5/green would display 5 beautiful green boxes. Calling localhost:5000/play/35/red would display 35 beautiful red boxes.


@app.get('/play/<int:x>/<color>')
def playlevelthree(x,color):
    
    return render_template('levelthree.html', number = x, color = color)





if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.