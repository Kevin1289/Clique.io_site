# Generated by Django 3.0.6 on 2020-06-11 23:07

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorize_main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='show_to_public',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.BooleanField(), default=[True, True, True, True, True, True, True, True], size=None),
        ),
    ]
