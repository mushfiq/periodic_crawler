import requests
from celery.decorators import periodic_task
from datetime import timedelta

'''	here you will have to write tasks as a method 
		that you want to run as a periodic task  '''

@periodic_task(run_every=timedelta(seconds=5))
def check_status():
	url = 'http://mushfiq.com'
	res = requests.get(url)
	print res.status_code

