# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20160105_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.CharField(default=b'male', max_length=255, null=True, blank=True, choices=[(b'male', b'male'), (b'female', b'female')]),
        ),
    ]
