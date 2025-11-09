"""
Fatima Nadeem
Oct 27, 2025
Lab 12, introduction to Flask
"""
from flask import Flask

"""
create an object 'app' from the Flask module.
__name__set to__main__ if the script is runnning directly from the main file
"""
app = Flask(__name__)

# set the routing to the main page
#'route' decorator is used to access the root URL
@app.route('/')
def index():
    return render_template ("index.html")

@app.route('/about')
def about():
    return '<h1>About us</h1>'

@app.route('/quotes')
def quotes():
    return '<h1>Quotes</h1>'

@app.route('./login')
def login():
    return redirect(url_for('home'))
     
#set the 'app' to run if you execute the file directly (not when it is important)
if __name__ == "__main__":
    app.run(debug=True)
