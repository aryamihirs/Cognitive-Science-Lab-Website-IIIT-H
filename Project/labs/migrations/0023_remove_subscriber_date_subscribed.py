# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0022_auto_20150901_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriber',
            name='date_subscribed',
        ),
    ]
