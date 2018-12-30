import os
import sqlite3
import json
from flask import Flask, render_template, g
from utils import dlogging as log

app = Flask(__name__)

DATABASE = os.getenv('DB_PATH', 'db/main.db')

def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = sqlite3.connect(DATABASE)
	return db

@app.teardown_appcontext
def close_connection(exception):
	db = getattr(g, '_database', None)
	if db is not None:
		db.close()

@app.route('/')
def index():
	log.debug("Request for '/'")

	return render_template('events.html')

@app.route('/api/v1/events')
def api_events():
	log.debug("Request for '/api/v1/events'")

	c = get_db().cursor()
	c.execute("SELECT * FROM EVENTS")
	data = c.fetchall()
	c.close()

	data_json = []
	for row in data:
		data_json.append({'datetime': row[0], 'type': row[1], 'content': json.loads(row[2])})

	return json.dumps(data_json)
