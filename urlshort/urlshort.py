# from flask import Flask
from flask import render_template # now it can use templates
from flask import request # This is for the GET-requests
from flask import redirect
from flask import url_for
import json # install json via pip
import os.path # needed to read data from a file
from flask import flash
from werkzeug.utils import secure_filename # check if uploaded files are okay to upload
from flask import abort
from flask import session # With this you can use cookies.
from flask import jsonify # Takes any sort of list or dictionary and cheanges it into JSON format.
from flask import Blueprint

# This file is `hello.py` but if it was `app.py`, than you don't have to specify `export FLASK_APP=app`.

bp = Blueprint('urlshort',__name__) # `urlshort` is the folder and the filename.


# print(__name__) # This is the `hello` name, which is determined by the `hello.py` file.

@bp.route("/") # normally this should be app.route("")
def home(): 
  return render_template('home.html', codes=session.keys()) # This is the template file `home.html`, that Flask automatically will find because it is in the `templates` directory. # With `codes=session.keys()`, we are also using the data in the cookies.

#app.run(host="0.0.0.0", port=50000, debug=True) # Necessary to access WSL2 flask via Windows, in WSL pipenv run with 'python3 hello.py'

#@bp.route("/about") # this should orginally be app.route if there where no blueprints.
#def about(): # The route and the function name don't have to match.
#  return "This is a url shortner"<--<--

@bp.route("/your-url", methods=['POST', 'GET'])
def your_url(): # Python functions, don't allow dashes, so we use `_`.
  if request.method == "POST":
    urls = {} # We are going to use a dictionary so we can us a json file to save our data.

    if os.path.exists('urls.json'): # if the file exists
      with open('urls.json') as urls_file:
        urls = json.load(urls_file) # put all the data from the file in the dictionary called `urls`
    if request.form['code'] in urls.keys(): # if the code (short n-ame) already exist in the key values:
      flash('That short name has already been taken. Please select another name.')
      return redirect(url_for('urlshort.home')) # The `urlshort`, is mandatry because this is the Home for the Blueprint.

    if 'url' in request.form.keys():
       urls[request.form['code']] = {'url':request.form['url']}
    else: # if no URL is given, than it is a file!
      f = request.files['file']
      full_name = request.form['code'] + secure_filename(f.filename) # Name of the file will also have the short URL!
      f.save('/mnt/c/Users/Dion Dresschers/data/gitg/url-shortner/urlshort/static/user_files/' + full_name)
      urls[request.form['code']] = {'file':full_name}
    with open('urls.json','w') as url_file: # create a file named `url_file`
      json.dump(urls, url_file) # `urls` is the dictionary, the secons id the file # import `json` for this. Save the file.
      session[request.form['code']] = True # Save this as a cookie. We don't save this as a value, so we just use `True`. # In stead of `True, you could also use a timestampt, so the user knew when it was saved.`
    return render_template("your-url.html", code=request.form['code']) # use `request.form` with 'POST' and `request.args` with GET. The latter is to access the GET-request for the field `code` that we put into an HTML form.
  else: # if it is a 'GET'
    return redirect(url_for('urlshort.home')) # the `home` is redirecting to the function `home` # return redirect(url) #return render_template('home.html') # With a redirect you are are not viewing the `/your-url` in the address bar of the web browser.

@bp.route('/<string:code>') # This `'<string:code>`, means look for any `string` and put it in a variable called 'code'.
def redirect_to_url(code):
  if os.path.exists('urls.json'):
    with open('urls.json') as urls_file:
      urls = json.load(urls_file)
      if code in urls.keys(): # if the short url is stored:
        if 'url' in urls[code].keys(): # check if it is in the 'url' rather than a 'file'
          return redirect(urls[code]['url'])
        else: # If the short code is redirecting to a file rather than a URL.
          return redirect(url_for('static', filename='/user_files/' + urls[code]['file']))
  return abort(404) # send a 404 message ('Not Found')

@bp.errorhandler(404) # handle 404 codes nicely.
def page_not_found(error):
  return render_template('page_not_found.html'), 404 # The `404` only tells the web browser there was a 404.

@bp.route('/api')
def session_api():
  return jsonify(list(session.keys())) # This takes all of the info of the cookie, put that one into a list, and than make it into JSON format.





