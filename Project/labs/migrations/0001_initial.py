# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_text', models.CharField(max_length=500)),
                ('upvotes', models.IntegerField(default=0)),
                ('name_of_person', models.CharField(max_length=40)),
                ('email_id', models.CharField(max_length=40)),
                ('time_posted', models.DateTimeField(verbose_name=b'date posted')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_text', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('photo', models.ImageField(upload_to=b'images')),
            ],
        ),
    ]
