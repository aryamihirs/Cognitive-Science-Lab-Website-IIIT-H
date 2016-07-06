# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0036_auto_20151004_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='Time_applied',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date posted'),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='reviewed',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='Gender',
            field=models.CharField(default=b'M', max_length=20, choices=[(b'M', b'Male'), (b'F', b'Female')]),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='Handedness',
            field=models.CharField(default=b'Right', max_length=50, choices=[(b'Left', b'Left'), (b'Right', b'Right')]),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='Lab_you_want_to_contribute_in',
            field=models.CharField(default=b'a', max_length=50, choices=[(b'a', b'a'), (b'b', b'b'), (b'c', b'c'), (b'd', b'd')]),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='Occupation_status',
            field=models.CharField(default=b'Student', max_length=50, choices=[(b'Student', b'Student'), (b'Service', b'Service Man'), (b'Business', b'Business Man'), (b'Doctor', b'Doctor'), (b'Teacher', b'Teacher'), (b'Unemployed', b'Unemployed')]),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='Transportation_plans',
            field=models.CharField(default=b'Public', max_length=50, choices=[(b'Public', b'Public Transport'), (b'Private Vehicle', b'Private Vehicle'), (b'Bicycle', b'Bicycle'), (b'Walk', b'Walk'), (b'Others', b'Others')]),
        ),
    ]
