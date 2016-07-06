# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0012_auto_20150826_0610'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('email_id', models.EmailField(max_length=40)),
                ('date_subscribed', models.DateField(default=datetime.datetime(2015, 9, 1, 15, 31, 16, 858171, tzinfo=utc))),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='email_id',
        ),
        migrations.AlterField(
            model_name='comment',
            name='time_posted',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 1, 15, 31, 16, 857565, tzinfo=utc), verbose_name=b'date posted'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 1, 15, 31, 16, 856818, tzinfo=utc), verbose_name=b'date published'),
        ),
    ]
