# Generated by Django 4.2.5 on 2023-12-27 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(unique=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(),
        ),
    ]
