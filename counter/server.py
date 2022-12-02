from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.errorhandler(404)
def page_not_found(error):
    return "<h1>Sorry! No response. Try again.</h1>"

@app.route('/')        
def main():
    if 'counter' not in session:
        session['counter'] = 1
    else:
        session['counter'] += 1
    return render_template('index.html')  

@app.route('/click')
def click():
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":       
    app.run(debug=True)    

