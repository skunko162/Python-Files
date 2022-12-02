from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'Keep it secret, keep it safe'

@app.route('/')
def user_list():  
    return render_template('index.html') 

@app.route('/survey', methods=['POST'])
def form()
    session['name'] = request.form['name']
    return redirect('index.html')

if __name__=="__main__":
    app.run(debug = True)