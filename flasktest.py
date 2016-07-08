from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/friznit/<arg>')
def hello_world(arg = 'nothing'):
    return 'This is the arg' + arg


if __name__ == '__main__':
    app.run()
