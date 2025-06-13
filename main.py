from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Home"


@app.route('/first')
def first():
    return "32"

@app.route('/second')
def second():
    return "True"


app.run(debug=True)
