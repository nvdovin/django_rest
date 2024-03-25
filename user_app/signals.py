import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from user_app.models import User


@receiver(post_save, sender=User)
def handle_course_save(sender, instance, created, **kwargs):
    print("I'm here")  

    if created:
        print("Новая пользователь:", instance)
    else:
        user = User.objects.get(pk=instance.pk)
        user.last_login = datetime.datetime.now()
        print(f'Пользователь {user} залогинился')
