# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shifts_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shiftgroup',
            name='end_date_range',
        ),
        migrations.RemoveField(
            model_name='shiftgroup',
            name='start_date_range',
        ),
        migrations.AlterField(
            model_name='shift',
            name='shift_group',
            field=models.ForeignKey(related_name='shift_set', blank=True, to='shifts_app.ShiftGroup', null=True),
        ),
    ]
