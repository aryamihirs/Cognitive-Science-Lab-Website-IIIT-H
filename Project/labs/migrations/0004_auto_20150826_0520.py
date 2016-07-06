# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0003_auto_20150826_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(help_text=b'enter your comment in no more than 50 words.', max_length=500),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email_id',
            field=models.EmailField(max_length=40, blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name_of_person',
            field=models.CharField(max_length=40, blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time_posted',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 5, 20, 10, 88875, tzinfo=utc), verbose_name=b'date posted'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='upvotes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to=b'images', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_text',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 5, 20, 10, 88221, tzinfo=utc), verbose_name=b'date published'),
        ),
    ]
