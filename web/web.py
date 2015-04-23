from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/data')
def data():
    response = {
        "cols": [
            {"id": "", "label": "Topping", "pattern": "", "type": "string"},
            {"id": "", "label": "Slices", "pattern": "", "type": "number"}
        ],
        "rows": [
            {"c": [{"v": "Mushrooms", "f": None}, {"v": 3, "f": None}]},
            {"c": [{"v": "Onions", "f": None}, {"v": 1, "f": None}]},
            {"c": [{"v": "Olives", "f": None}, {"v": 1, "f": None}]},
            {"c": [{"v": "Zucchini", "f": None}, {"v": 1, "f": None}]},
            {"c": [{"v": "Pepperoni", "f": None}, {"v": 2, "f": None}]}
        ]
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
