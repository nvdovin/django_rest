# Generated by Django 4.0 on 2024-03-21 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materials_app', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='payment_id',
        ),
        migrations.RemoveField(
            model_name='course',
            name='payment_url',
        ),
    ]