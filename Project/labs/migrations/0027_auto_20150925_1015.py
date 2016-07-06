# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0026_auto_20150924_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name_of_person',
            field=models.CharField(default=b'Anonymous', max_length=40, blank=True),
        ),
    ]
