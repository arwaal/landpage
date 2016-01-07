# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_amaakin_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Landpage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to=b'amaakin', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile', models.CharField(max_length=255, null=True, blank=True)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('gender', models.CharField(default=b'male', max_length=255, null=True, choices=[(b'male', b'male'), (b'female', b'female')])),
                ('reg_user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Amaakin',
        ),
    ]
