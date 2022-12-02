from ast import Num
from os import times
from flask import Flask
app = Flask(__name__)

@app.route('/')

def hello_world():
    return "Hello World!"


@app.route('/dojo')
    
def dojo():
    return "dojo"

@app.route('/say/flask/<word>')
    
def word(word):
    return f"hi {word}"

@app.route('/say/<int:num>/<word>')
    
def repeating(word, num):
    return f"{word * num}"




if __name__== "__main__":
    app.run(debug=True)