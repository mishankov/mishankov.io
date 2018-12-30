import sqlite3
import os
import json
import time
import dlogging as log
import github_api


while True:
	DB_PATH = os.getenv('DB_PATH', 'db/main.db')

	conn = sqlite3.connect(DB_PATH)
	c = conn.cursor()

	log.info('Get data from GitHub')
	events = github_api.get_events('mishankov')
	if events['status'] == 200:
		log.info('Truncate EVENTS table')
		c.execute("DELETE FROM EVENTS;")
		conn.commit()

		for event in events['content']:
			c.execute("INSERT INTO EVENTS VALUES(?, ?, ?);", (event['created_at'], 'GitHub', json.dumps(event)))
	else:
		log.error('Response from GitHub is not good. Status: {}. Content: {}'.format(events['status'], events['content']))

	log.info("Commit and close connection to {}".format(DB_PATH))
	conn.commit()
	c.close()
	conn.close()

	time.sleep(3600)
