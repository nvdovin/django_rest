# Generated by Django 5.0.2 on 2024-02-17 19:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials_app', '0002_remove_course_lessons_lesson_course'),
        ('user_app', '0007_alter_payments_payed_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='payed_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='materials_app.course'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payed_lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='materials_app.lesson'),
        ),
    ]