from flask import Flask, render_template 
app = Flask(__name__)  # Import Flask to allow us to create our app     # Create a new instance of the Flask class called "app"


@app.route("/")
def template():
    return render_template("index.html", x = 8)

@app.route("/<int:x>")
def get_it(x):
    return render_template("index.html", x = x)






if __name__=="__main__":   # Ensure this file is being run directly and not from a different module 
    app.run(debug=True)    # Run the app in debug mode.