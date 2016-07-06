# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0029_auto_20150925_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='professor_name',
            field=models.CharField(default='prof', max_length=60),
            preserve_default=False,
        ),
    ]
