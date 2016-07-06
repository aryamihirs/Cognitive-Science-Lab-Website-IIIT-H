# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0038_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video_url',
        ),
        migrations.AddField(
            model_name='video',
            name='video_id',
            field=models.CharField(default='abhishek', help_text=b"copy the video id given in the url. write xyz if v='xyz' in the video url.", max_length=100),
            preserve_default=False,
        ),
    ]
