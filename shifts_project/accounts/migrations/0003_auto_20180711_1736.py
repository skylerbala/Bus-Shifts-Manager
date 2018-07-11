# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180711_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='description',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='website',
        ),
        migrations.AddField(
            model_name='employee',
            name='wage',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='employee',
            name='city',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
