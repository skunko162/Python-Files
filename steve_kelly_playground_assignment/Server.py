from turtle import colormode
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def boxes():
    return render_template('index.html', num = 1)

@app.route('/play')
def num():
    return render_template('index.html', num = 3)

@app.route('/play/<int:num>/')
def x(num): 
    return render_template('index.html', num = num)

@app.route('/play/<int:num>/<string:color>')
def colors(num, color):
    return render_template('index.html', num = num, color = color)

if __name__=="__main__":
    app.run(debug = True)