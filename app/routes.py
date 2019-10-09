from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Alec'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'I like flavored meatpies!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'I live in a giant bucket!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
