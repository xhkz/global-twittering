from flask import Flask
import views.viewRepository as views
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    data = views.viewRepository();
    #rows = data.top10twettersView();
    rows = data.latest100Tweets();
    app.run(debug=True)


