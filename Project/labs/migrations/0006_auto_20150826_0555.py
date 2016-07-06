# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0005_auto_20150826_0523'),
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
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 5, 55, 23, 474736, tzinfo=utc), verbose_name=b'date posted'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 5, 55, 23, 474066, tzinfo=utc), verbose_name=b'date published'),
        ),
    ]
