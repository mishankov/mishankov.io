import requests
import json

URL = 'https://api.github.com/'

def get_user(username):
	r = requests.get(URL + 'users/{}'.format(username))

	return {'status': r.status_code, 'content': json.loads(r.content)}

def get_events(username):
	r = requests.get(URL + 'users/{}/events'.format(username))

	return {'status': r.status_code, 'content': json.loads(r.content)}
