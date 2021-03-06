from flask import Flask
import pysolr

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5002)
