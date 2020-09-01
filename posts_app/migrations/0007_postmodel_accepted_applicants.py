# Generated by Django 3.0.6 on 2020-06-11 19:23

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0006_postmodel_applicants'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='accepted_applicants',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=list, size=None),
        ),
    ]
