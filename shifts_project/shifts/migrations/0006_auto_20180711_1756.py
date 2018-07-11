# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0005_auto_20180711_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='employee',
            field=models.ForeignKey(related_name='employee_set', to='employees.Employee', null=True),
        ),
    ]
