# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0028_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='question',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(help_text=b'enter your comment in no more than 500 words.', max_length=500),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name_of_person',
            field=models.CharField(default=b'Anonymous', max_length=60, blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_text',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_title',
            field=models.CharField(default=b'Post Title', unique=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='sub_email_id',
            field=models.EmailField(unique=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='sub_name',
            field=models.CharField(max_length=60),
        ),
    ]
