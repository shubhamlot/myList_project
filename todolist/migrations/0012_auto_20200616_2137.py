# Generated by Django 3.0.4 on 2020-06-16 16:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0011_auto_20200616_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='Discription',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='task',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 16, 21, 37, 53, 796710)),
        ),
        migrations.AlterField(
            model_name='task',
            name='TaskName',
            field=models.CharField(max_length=10),
        ),
    ]
