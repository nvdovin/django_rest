from django.db.models.signals import post_save
from django.dispatch import receiver

from config import settings
from .models import Course, CourseSubscribe
from user_app.models import User
from django.core.mail import send_mail


@receiver(post_save, sender=Course)
def handle_course_save(sender, instance, created, **kwargs):
    print("I'm here")
    subscribes = CourseSubscribe.objects.all()    

    if sender == Course:
        if created:
            # Это создание новой записи
            print("Новая запись создана:", instance)
        else:
            # Это изменение существующей записи
            changed_course_id = instance.pk
            users_id_to_send = subscribes.filter(course=changed_course_id).values_list('user', flat=True)
            user_emails_list = User.objects.filter(id__in=users_id_to_send).values_list('email', flat=True)
            emails = list(user_emails_list)
            send_mail(
                subject=f"Изменение курса {instance.title}",
                message=f"Курс {instance.title} был изменен",
                from_email=settings.DEFAULT_FROM_EMAIL, 
                recipient_list=emails
            )
            print(f'Пользователи {emails} получил уведомление о изменении курса: {instance.title}')
