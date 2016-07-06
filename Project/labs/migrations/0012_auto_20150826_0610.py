# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0011_auto_20150826_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time_posted',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 6, 10, 47, 724910, tzinfo=utc), verbose_name=b'date posted'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='verified',
            field=models.BooleanField(default=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 6, 10, 47, 724189, tzinfo=utc), verbose_name=b'date published'),
        ),
    ]
