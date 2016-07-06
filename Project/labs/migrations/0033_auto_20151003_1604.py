# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0032_auto_20150927_0831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='upvotes',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=3, to='labs.Post'),
            preserve_default=False,
        ),
    ]
