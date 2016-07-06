# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='time_posted',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 4, 56, 10, 889889, tzinfo=utc), verbose_name=b'date posted'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 4, 56, 10, 889267, tzinfo=utc), verbose_name=b'date published'),
        ),
    ]
