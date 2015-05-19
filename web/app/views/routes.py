"""
Author: Team 8
City: Chicago
Subject: COMP90024
"""

from flask import render_template

from app import app


@app.route('/')
def arch():
    return render_template('architecture.html')


@app.route('/device')
def device():
    return render_template('device.html')


@app.route('/lang')
def lang():
    return render_template('lang.html')


@app.route('/follower')
def follower():
    return render_template('follower.html')


@app.route('/topic')
def topic():
    return render_template('topic.html')


@app.route('/sentiment')
def sentiment():
    return render_template('sentiment.html')


@app.route('/google_map')
def google_map():
    return render_template('map.html')


@app.route('/time_line')
def time_line():
    return render_template('timeline.html')
