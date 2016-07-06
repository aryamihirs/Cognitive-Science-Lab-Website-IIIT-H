# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0010_auto_20150826_0608'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='verified',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='post_title',
            field=models.CharField(default=b'Post Title', unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time_posted',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 6, 9, 47, 947117, tzinfo=utc), verbose_name=b'date posted'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 6, 9, 47, 946441, tzinfo=utc), verbose_name=b'date published'),
        ),
    ]
