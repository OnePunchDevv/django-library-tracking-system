# Generated by Django 4.2 on 2025-03-24 18:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2025, 4, 7, 18, 25, 37, 650617, tzinfo=datetime.timezone.utc)),
        ),
    ]
