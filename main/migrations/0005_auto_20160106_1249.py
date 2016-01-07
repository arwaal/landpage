# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20160106_1110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='reg_user',
        ),
        migrations.AddField(
            model_name='users',
            name='first_name',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='users',
            name='last_name',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='landpage',
            name='text',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
