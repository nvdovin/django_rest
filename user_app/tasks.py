from .models import User
from datetime import datetime

def check_last_login_date():
    """
    Check the last login date of all users and set the is_active flag to False if the last login date is older than 30 days.
    """ 
    users = User.objects.all()
    print("checking")
    for user in users:
        if user.last_login - datetime.now() < 30:
            user.is_active = False
            user.save()
