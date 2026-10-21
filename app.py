from flask import Flask, render_template , url_for

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/profissial')
def profissional():
    return render_template('profissional.html')

if __name__ == '__main__':
    app.run(debug=True)
