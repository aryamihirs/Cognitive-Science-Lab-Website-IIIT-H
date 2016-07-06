# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0002_auto_20150826_0456'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_text', models.CharField(max_length=500)),
                ('upvotes', models.IntegerField(default=0)),
                ('name_of_person', models.CharField(max_length=40)),
                ('email_id', models.CharField(max_length=40)),
                ('time_posted', models.DateTimeField(default=datetime.datetime(2015, 8, 26, 5, 2, 20, 814996, tzinfo=utc), verbose_name=b'date posted')),
            ],
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 5, 2, 20, 814292, tzinfo=utc), verbose_name=b'date published'),
        ),
    ]
