#configure your broker and host into the BROKER URL below
BROKER_URL = "amqp://mushfiq:mushfiq@localhost:5672//"
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Dacca'
CELERY_ENABLE_UTC = True
CELERY_IMPORTS=("tasks",)