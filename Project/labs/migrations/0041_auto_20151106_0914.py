# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0040_auto_20151106_0856'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Subscriber',
        ),
        migrations.RemoveField(
            model_name='post',
            name='video_link',
        ),
    ]
