# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0014_auto_20150901_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email_id',
            field=models.EmailField(max_length=40, blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time_posted',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 1, 15, 37, 57, 907936, tzinfo=utc), verbose_name=b'date posted'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 1, 15, 37, 57, 907257, tzinfo=utc), verbose_name=b'date published'),
        ),
        migrations.AlterField(
            model_name='subscribers',
            name='date_subscribed',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 1, 15, 37, 57, 908487, tzinfo=utc)),
        ),
    ]
