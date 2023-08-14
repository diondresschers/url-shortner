from flask import Flask
from flask import render_template # now it can use templates
from flask import request # This is for the GET-requests
from flask import redirect
from flask import url_for
import json # install json via pip
import os.path # needed to read data from a file

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

@app.route("/your-url", methods=['POST', 'GET'])
def your_url(): # Python functions, don't allow dashes, so we use `_`.
  if request.method == "POST":
    urls = {} # We are going to use a dictionary so we can us a json file to save our data.

    if os.path.exists('urls.json'): # if the file exists
      with open('urls.json') as urls_file:
        urls = json.load(urls_file) # put all the data from the file in the dictionary called `urls`
    if request.form['code'] in urls.keys(): # if the code already exist in the key values:
      return redirect(url_for('home')) 

    urls[request.form['code']] = {'url':request.form['url']} # if the form name is not correct than you can get the error in the browser: `Bad Request The browser (or proxy) sent a request that this server could not understand.`
    with open('urls.json','w') as url_file: # create a file named `url_file`
      json.dump(urls, url_file) # `urls` is the dictionary, the secons id the file # import `json` for this.
    return render_template("your-url.html", code=request.form['code']) # use `request.form` with 'POST' and `request.args` with GET. The latter is to access the GET-request for the field `code` that we put into an HTML form.
  else: # if it is a 'GET'
    return redirect(url_for('home')) # the `home` is redirecting to the function `home` # return redirect(url) #return render_template('home.html') # With a redirect you are are not viewing the `/your-url` in the address bar of the web browser.




