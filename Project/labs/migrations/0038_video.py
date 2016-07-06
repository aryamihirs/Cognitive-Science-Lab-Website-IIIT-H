# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0037_auto_20151005_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=200)),
                ('video_url', models.URLField(blank=True)),
                ('uploaded_by', models.CharField(max_length=60, blank=True)),
                ('time_uploaded', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
