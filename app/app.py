import sys
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return f"Hello, Docker! Running on Python {sys.version}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
