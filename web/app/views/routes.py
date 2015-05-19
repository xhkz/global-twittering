__author__ = 'Xin Huang'

from collections import Counter

from flask import render_template, jsonify

from bs4 import BeautifulSoup

from twitter_languages import lang_codes
from app import app, db


@app.route('/')
def pie():
    return render_template('pie.html')


@app.route('/pie_data')
def pie_data():
    rows = []
    for row in list(db.view('mapviews/devices', group=True)):
        if row.value >= 100:
            rows.append({'c': [{'v': BeautifulSoup(row.key).a.text}, {'v': row.value}]})

    response = {
        'cols': [
            {'id': '', 'label': 'Device', 'type': 'string'},
            {'id': '', 'label': 'Tweets', 'type': 'number'}
        ],
        'rows': rows
    }

    return jsonify(response)


# Display all languages used as pie chart
@app.route('/lang')
def lang():
    return render_template('lang.html')


@app.route('/lang_data')
@app.route('/lang_data/<m>')
def lang_data(m=None):
    rows = []
    for row in list(db.view('mapviews/language', group=True)):
        if m and row.key in ['en', 'und']:
            continue
        if row.value >= 100:
            rows.append(
                {'c': [{'v': lang_codes[row.key]['name'] if row.key in lang_codes else row.key}, {'v': row.value}]})

    response = {
        'cols': [
            {'id': '', 'label': 'Language', 'type': 'string'},
            {'id': '', 'label': 'Tweets', 'type': 'number'}
        ],
        'rows': rows
    }
    return jsonify(response)


@app.route('/bar')
def bar():
    return render_template('bar.html')


@app.route('/bar_data')
def bar_data():
    rows = []
    for r in list(db.list('mapviews/sortMax', 'mapviews/followers', group=True))[1]['rows']:
        rows.append({'c': [{'v': r['key']}, {'v': r['value']['max']}]})

    response = {
        'cols': [
            {'id': '', 'label': 'Name', 'type': 'string'},
            {'id': '', 'label': 'Followers', 'type': 'number'}
        ],
        'rows': rows
    }

    return jsonify(response)


@app.route('/col')
def col():
    return render_template('col.html')


@app.route('/col_data')
def col_data():
    rows = []
    for r in list(db.list('mapviews/sort', 'mapviews/topics', group=True))[1]['rows']:
        rows.append({'c': [{'v': r['key']}, {'v': r['value']}]})

    response = {
        'cols': [
            {'id': '', 'label': 'Topic', 'type': 'string'},
            {'id': '', 'label': 'Tweets', 'type': 'number'}
        ],
        'rows': rows
    }

    return jsonify(response)


@app.route('/scatter')
def scatter():
    return render_template('scatter.html')


@app.route('/scatter_data')
def scatter_data():
    counter = Counter()
    for row in list(db.view('mapviews/c2e2')):
        if row.value:
            counter[row.value['sentiScore']] += 1

    # exclude neu(0)
    counter.pop(0)

    data = {
        'cols': [
            {'id': '', 'label': 'Score', 'type': 'number'},
            {'id': '', 'label': 'Count', 'type': 'number'}
        ],
        'rows': [{'c': [{'v': key}, {'v': val}]} for (key, val) in counter.iteritems()]
    }
    return jsonify(data)


@app.route('/google_map')
def google_map():
    return render_template('map.html')


@app.route('/google_map_data')
def google_map_data():
    geo_list = []
    for row in list(db.view('mapviews/latestTweets', descending=True, limit=200)):
        geo_list.append([row.value['geo'][1], row.value['geo'][0], row.value['text']])

    data = {
        'geo': geo_list
    }
    return jsonify(data)


@app.route('/couch')
def couch_data():
    """
    sample data for querying couchdb and return json
    :return: json
    """
    data = list(db.list('mapviews/sortMax', 'mapviews/followers', group=True))[1]

    return jsonify(data)
