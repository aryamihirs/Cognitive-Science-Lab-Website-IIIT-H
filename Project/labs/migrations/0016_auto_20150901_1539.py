# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0015_auto_20150901_1537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email_id',
        ),
        migrations.AlterField(
            model_name='comment',
            name='time_posted',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 1, 15, 39, 42, 522202, tzinfo=utc), verbose_name=b'date posted'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 1, 15, 39, 42, 521544, tzinfo=utc), verbose_name=b'date published'),
        ),
        migrations.AlterField(
            model_name='subscribers',
            name='date_subscribed',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 1, 15, 39, 42, 522776, tzinfo=utc)),
        ),
    ]
