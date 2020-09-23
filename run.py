import os
from flask import Flask, render_template, request, flash


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/phones')
def phones():
    return render_template("phones.html")


@app.route('/tablets')
def tablets():
    return render_template("tablets.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/store')
def store():
    return render_template("store.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
