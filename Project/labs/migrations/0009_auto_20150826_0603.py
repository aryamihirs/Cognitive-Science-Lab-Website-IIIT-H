# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0008_auto_20150826_0559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time_posted',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 6, 3, 13, 474530, tzinfo=utc), verbose_name=b'date posted'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='verified',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_title',
            field=models.CharField(default=b'Post Title', max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 6, 3, 13, 473855, tzinfo=utc), verbose_name=b'date published'),
        ),
    ]
