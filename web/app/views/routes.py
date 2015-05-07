__author__ = 'Xin Huang'
import os

from flask import render_template, jsonify, send_from_directory

from app import app


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


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