# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0010_remove_shift_can_swap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='shift',
            field=models.ForeignKey(related_name='shift_set', to='shifts.Shift'),
        ),
    ]
