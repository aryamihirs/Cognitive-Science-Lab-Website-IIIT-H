# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0009_auto_20150826_0603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='verified',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_title',
        ),
        migrations.AlterField(
            model_name='comment',
            name='time_posted',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 6, 8, 0, 82413, tzinfo=utc), verbose_name=b'date posted'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 6, 8, 0, 81747, tzinfo=utc), verbose_name=b'date published'),
        ),
    ]
