# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='amaakin',
            name='text',
            field=models.CharField(default=datetime.datetime(2015, 11, 26, 8, 10, 32, 472951, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
