# Generated by Django 3.0.4 on 2020-06-16 05:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='Date',
            field=models.DateField(default=datetime.datetime(2020, 6, 16, 10, 41, 47, 314375)),
        ),
    ]