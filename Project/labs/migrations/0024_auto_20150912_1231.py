# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0023_remove_subscriber_date_subscribed'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='date_subscribed',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='sub_email_id',
            field=models.EmailField(unique=True, max_length=40),
        ),
    ]
