# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0004_auto_20150826_0520'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time_posted',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 5, 23, 49, 54896, tzinfo=utc), verbose_name=b'date posted'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 5, 23, 49, 54237, tzinfo=utc), verbose_name=b'date published'),
        ),
    ]
