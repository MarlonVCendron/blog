# Generated by Django 2.2.1 on 2019-11-24 17:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191124_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 24, 17, 30, 19, 605068, tzinfo=utc), verbose_name='date published'),
        ),
    ]