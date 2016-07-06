# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0021_auto_20150901_1604'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriber',
            old_name='email_id',
            new_name='sub_email_id',
        ),
        migrations.RenameField(
            model_name='subscriber',
            old_name='name',
            new_name='sub_name',
        ),
    ]
