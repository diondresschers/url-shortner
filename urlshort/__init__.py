from flask import Flask

# This file is automatically called by Flask, as this is in the Flask Blueprint folder.

def create_app(test_config=None): # This `test_config` is not used now, but may be used in the future. We need to run everyhting as a function.
  app = Flask(__name__) # We've just imported `Flask` from line 1. The `__name__`  is the app we currenty run (thus `hello.py`).
  app.secret_key = '&%%@&^$)()%*%' # needed to send securely send data from flash messages to the user.

  from urlshort import urlshort
  app.register_blueprint(urlshort.bp)
  return app