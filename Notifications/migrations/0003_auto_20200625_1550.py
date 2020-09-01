# Generated by Django 3.0.6 on 2020-06-25 19:50

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notifications', '0002_auto_20200612_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationmodel',
            name='data',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=list, size=None),
        ),
        migrations.AddField(
            model_name='notificationmodel',
            name='url',
            field=models.CharField(blank=True, default='#', max_length=100),
        ),
    ]
