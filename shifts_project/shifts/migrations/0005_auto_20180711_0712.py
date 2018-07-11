# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0004_auto_20180711_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='employee',
            field=models.ForeignKey(related_name='employee_set', to='accounts.Employee', null=True),
        ),
        migrations.AlterField(
            model_name='shift',
            name='shift_group',
            field=models.ForeignKey(related_name='shift_set', to='shifts.ShiftGroup', null=True),
        ),
    ]
