# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20160106_1249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='users',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='users',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='users',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='users',
            name='mobile',
        ),
    ]
