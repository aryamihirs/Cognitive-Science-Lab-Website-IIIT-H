# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0027_auto_20150925_1015'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=100)),
                ('answer', models.TextField(max_length=1000)),
                ('time_added', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'time added')),
            ],
        ),
    ]
