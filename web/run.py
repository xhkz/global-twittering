"""
Author: Team 8
City: Chicago
Subject: COMP90024
"""

from app import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
