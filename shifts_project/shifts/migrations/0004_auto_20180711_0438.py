# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0003_shift_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='employee',
            field=models.ForeignKey(related_name='employee_set', blank=True, to='accounts.Employee', null=True),
        ),
    ]
