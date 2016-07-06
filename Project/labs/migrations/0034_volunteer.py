# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0033_auto_20151003_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('mail_id', models.EmailField(max_length=60)),
                ('mobile_number', models.CharField(max_length=15)),
                ('date_of_birth', models.DateField()),
            ],
        ),
    ]
