# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0035_volunteer_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='volunteer',
            old_name='date_of_birth',
            new_name='Date_of_birth',
        ),
        migrations.RenameField(
            model_name='volunteer',
            old_name='gender',
            new_name='Gender',
        ),
        migrations.RenameField(
            model_name='volunteer',
            old_name='mail_id',
            new_name='Mail_id',
        ),
        migrations.RenameField(
            model_name='volunteer',
            old_name='mobile_number',
            new_name='Mobile_number',
        ),
        migrations.RenameField(
            model_name='volunteer',
            old_name='name',
            new_name='Name',
        ),
        migrations.AddField(
            model_name='volunteer',
            name='Handedness',
            field=models.CharField(default=b'Right', max_length=2, choices=[(b'Left', b'Left'), (b'Right', b'Right')]),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='How_do_you_plan_to_contribute',
            field=models.TextField(default='by doing research work.', max_length=6000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='Lab_you_want_to_contribute_in',
            field=models.CharField(default=b'a', max_length=5, choices=[(b'a', b'a'), (b'b', b'b'), (b'c', b'c'), (b'd', b'd')]),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='Nationality',
            field=models.CharField(default='indian', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='Occupation_status',
            field=models.CharField(default=b'Student', max_length=2, choices=[(b'Student', b'Student'), (b'Service', b'Service Man'), (b'Business', b'Business Man'), (b'Doctor', b'Doctor'), (b'Teacher', b'Teacher'), (b'Unemployed', b'Unemployed')]),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='Transportation_plans',
            field=models.CharField(default=b'Public', max_length=2, choices=[(b'Public', b'Public Transport'), (b'Private Vehicle', b'Private Vehicle'), (b'Bicycle', b'Bicycle'), (b'Walk', b'Walk'), (b'Others', b'Others')]),
        ),
    ]
