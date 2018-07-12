# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0008_run_line'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='can_swap',
            field=models.BooleanField(default=False),
        ),
    ]
