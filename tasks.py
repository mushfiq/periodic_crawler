import requests
from celery.decorators import periodic_task
from datetime import timedelta

@periodic_task(run_every=timedelta(seconds=5))
def check_status():
	url = 'http://mushfiq.com'
	res = requests.get(url)
	print res.status_code