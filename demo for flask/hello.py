from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    a = __name__
    return f'lvdund {a}'

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name = name)

@app.route('/lists')
def lists():
    list = [1, 2, 3, 4, 5]
    return render_template('list.html', list = list)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

