from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template('default.jinja2')


@app.route("/echo.php", methods=['POST', 'GET'])
def echo():
    msg = request.form.get('msg')

    return render_template('default.jinja2', MSG=msg)


@app.route("/<a>/<b>")
def hello_world(a, b):

    a = int(a)
    b = int(b)

    one_message = f'{a} + {b} = {a + b}'

    return render_template('default.jinja2', MSG=one_message)


if __name__ == '__main__':
    app.run()
