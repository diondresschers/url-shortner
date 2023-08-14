from flask import Flask
from flask import render_template # now it can use templates
from flask import request # This is for the GET-requests

# This file is `hello.py` but if it was `app.py`, than you don't have to specify `export FLASK_APP=app`.





app = Flask(__name__) # We've just imported `Flask` from line 1. The `__name__`  is the app we currenty run (thus `hello.py`).

# print(__name__) # This is the `hello` name, which is determined by the `hello.py` file.

@app.route("/")
def home(): 
  return render_template('home.html', name="Dion") # This is the template file `home.html`, that Flask automatically will find because it is in the `templates` directory.
#    return "Hello World..."

#app.run(host="0.0.0.0", port=50000, debug=True) # Necessary to access WSL2 flask via Windows, in WSL pipenv run with 'python3 hello.py'

@app.route("/about")
def about(): # The route and the function name don't have to match.
  return "This is a url shortner"

@app.route("/your-url")
def your_url(): # Python functions, don't allow dashes, so we use `_`.
  return render_template("your-url.html", code=request.args['code']) # The latter is to access the GET-request for the field `code` that we put into an HTML form.




