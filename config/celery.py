import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


# Example for celery
@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


@app.task(bind=True, ignore_result=True)
def check_last_login_date():
    """
    Check the last login date of all users and set the is_active flag to False if the last login date is older than 30 days.
    """ 

    from user_app.models import User
    from datetime import datetime
    
    users = User.objects.all()
    print("checking")
    for user in users:
        if user.last_login - datetime.now() < 30:
            user.is_active = False
            user.save()
