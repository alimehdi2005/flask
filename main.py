from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contact')
def contact():
    return render_template('index.html')


@app.route('/book')
def book():
    return render_template('book.html')


if __name__ == "__main__":
    app.run(debug=True)
