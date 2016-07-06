# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0016_auto_20150901_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time_posted',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 1, 15, 42, 37, 495854, tzinfo=utc), verbose_name=b'date posted'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 1, 15, 42, 37, 495121, tzinfo=utc), verbose_name=b'date published'),
        ),
        migrations.AlterField(
            model_name='subscribers',
            name='date_subscribed',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 1, 15, 42, 37, 496386, tzinfo=utc)),
        ),
    ]
