# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0024_auto_20150912_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='verified',
            field=models.BooleanField(default=0),
        ),
    ]
