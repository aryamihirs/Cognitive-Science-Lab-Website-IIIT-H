# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0017_auto_20150901_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('email_id', models.EmailField(max_length=40)),
                ('date_subscribed', models.DateTimeField(default=datetime.datetime(2015, 9, 1, 15, 43, 46, 890495, tzinfo=utc))),
            ],
        ),
        migrations.DeleteModel(
            name='Subscribers',
        ),
        migrations.AlterField(
            model_name='comment',
            name='time_posted',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 1, 15, 43, 46, 889963, tzinfo=utc), verbose_name=b'date posted'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 1, 15, 43, 46, 889309, tzinfo=utc), verbose_name=b'date published'),
        ),
    ]
