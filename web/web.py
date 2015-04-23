from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'COMP90024'


if __name__ == '__main__':
    app.run()
