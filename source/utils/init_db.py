import sqlite3
import os
import dlogging as log

DB_PATH = os.getenv('DB_PATH', 'db/')

log.info("Connect to data base {}".format(DB_PATH + 'mishankovio.db'))
conn = sqlite3.connect(DB_PATH + 'mishankovio.db')
c = conn.cursor()

log.info('Create EVENTS(datestamp TEXT, type TEXT, json_content TEXT) table')
c.execute("CREATE TABLE IF NOT EXISTS EVENTS(datestamp TEXT, type TEXT, json_content TEXT)")

log.info("Commit and close connection to {}".format(DB_PATH))
conn.commit()
c.close()
conn.close()