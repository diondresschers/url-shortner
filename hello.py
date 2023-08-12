from flask import Flask

app = Flask(__name__) # We've just imported `Flask` from line 1. The `__name__`  is the app we currenty run (thus `hello.py`).

# print(__name__) # This is the `hello` name, which is determined by the `hello.py` file.

@app.route("/")
def home(): 
    return "Hello World..."

app.run(host="0.0.0.0", port=50000, debug=True) # Necessary to access WSL2 flask via Windows, in WSL pipenv run with 'python3 hello.py'


