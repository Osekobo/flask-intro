from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    c = [1,2,3,4,5,6,7,8,9,10]
    return render_template("index.html", c=c)


@app.route('/products')
def products():
    e = "Milk"
    f = "Soap"
    return render_template("products.html", e=e, f=f)


@app.route('/sales')
def sales():
    g = "2 cups"
    h = "4 bottles"
    return render_template('sales.html', g=g, h=h)


@app.route('/register')
def registers():
    x = "Bread"
    y = "three"
    return render_template("register.html", x=x, y=y)


@app.route('/dashboard')
def dashboard():
    a = "Home"
    b = "Contact Us"
    return render_template('dashboard.html', a=a, b=b)


app.run(debug=True)

# debugging from browser and relation with productiion , html escaping, variable rules
