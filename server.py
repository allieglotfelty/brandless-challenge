from flask import Flask, render_template, session, request
from jinja2 import StrictUndefined

app = Flask(__name__)

app.secret_key = 'asldfjajeiownasldknvauwaeadsfanadnvaoqpndcsdf'

app.jinja_env.undefined = StrictUndefined


@app.route('/')
def display_homepage():
    """Displays homepage."""

    return render_template('homepage.html')


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
