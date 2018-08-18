# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0009_shift_can_swap'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shift',
            name='can_swap',
        ),
    ]
