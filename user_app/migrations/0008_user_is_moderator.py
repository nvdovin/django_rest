# Generated by Django 5.0.2 on 2024-02-20 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0007_alter_payments_payed_course_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_moderator',
            field=models.BooleanField(default=False, verbose_name='Модератор?'),
        ),
    ]
