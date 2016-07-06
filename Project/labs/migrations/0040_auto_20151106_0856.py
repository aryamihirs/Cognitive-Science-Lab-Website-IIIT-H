# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0039_auto_20151106_0610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='professor_name',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='video',
            name='uploaded_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
