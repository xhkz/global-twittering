__author__ = 'Xin Huang'

from flask import render_template, jsonify

from app import app, db


@app.route('/')
def pie():
    return render_template('pie.html')


@app.route('/pie_data')
def pie_data():
    response = {
        'cols': [
            {'id': '', 'label': 'Topping', 'pattern': '', 'type': 'string'},
            {'id': '', 'label': 'Slices', 'pattern': '', 'type': 'number'}
        ],
        'rows': [
            {'c': [{'v': 'Mushrooms', 'f': None}, {'v': 3, 'f': None}]},
            {'c': [{'v': 'Onions', 'f': None}, {'v': 1, 'f': None}]},
            {'c': [{'v': 'Olives', 'f': None}, {'v': 1, 'f': None}]},
            {'c': [{'v': 'Zucchini', 'f': None}, {'v': 1, 'f': None}]},
            {'c': [{'v': 'Pepperoni', 'f': None}, {'v': 2, 'f': None}]}
        ]
    }

    return jsonify(response)


@app.route('/bar')
def bar():
    return render_template('bar.html')


@app.route('/bar_data')
def bar_data():
    response = {
        'cols': [
            {'id': '', 'label': 'Galaxy', 'type': 'string'},
            {'id': '', 'label': 'Distance', 'type': 'number'}
        ],
        'rows': [
            {'c': [{'v': 'Canis Major Dwarf'}, {'v': 8000}]},
            {'c': [{'v': 'Sagittarius Dwarf'}, {'v': 24000}]},
            {'c': [{'v': 'Ursa Major II Dwarf'}, {'v': 30000}]},
            {'c': [{'v': 'Lg. Magellanic Cloud'}, {'v': 50000}]},
            {'c': [{'v': 'Bootes I'}, {'v': 60000}]},
        ]
    }

    return jsonify(response)


@app.route('/col')
def col():
    return render_template('col.html')


@app.route('/col_data')
def col_data():
    response = {
        'cols': [
            {'id': '', 'label': 'Galaxy', 'type': 'string'},
            {'id': '', 'label': 'Distance', 'type': 'number'},
            {'id': '', 'label': 'Brightness', 'type': 'number'}
        ],
        'rows': [
            {'c': [{'v': 'Canis Major Dwarf'}, {'v': 8000}, {'v': 23.3}]},
            {'c': [{'v': 'Sagittarius Dwarf'}, {'v': 24000}, {'v': 4.5}]},
            {'c': [{'v': 'Ursa Major II Dwarf'}, {'v': 30000}, {'v': 14.3}]},
            {'c': [{'v': 'Lg. Magellanic Cloud'}, {'v': 50000}, {'v': 0.9}]},
            {'c': [{'v': 'Bootes I'}, {'v': 60000}, {'v': 13.1}]}
        ]
    }

    return jsonify(response)


@app.route('/scatter')
def scatter():
    return render_template('scatter.html')


@app.route('/couch')
def couch_data():
    """
    sample data for querying couchdb and return json
    :return: json
    """
    data = list(db.query("zoey/test"))
    return jsonify({'data': data})