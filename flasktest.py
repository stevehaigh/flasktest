from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/friznit/<arg>')
def friznit(arg):
    return 'Friznit: ' + arg

if __name__ == '__main__':
    app.run()
