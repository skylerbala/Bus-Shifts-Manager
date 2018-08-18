# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0011_auto_20180719_0558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='shift',
            field=models.ForeignKey(related_name='run_set', to='shifts.Shift'),
        ),
        migrations.AlterField(
            model_name='shift',
            name='employee',
            field=models.ForeignKey(related_name='shift_set', to='employees.Employee', null=True),
        ),
    ]
