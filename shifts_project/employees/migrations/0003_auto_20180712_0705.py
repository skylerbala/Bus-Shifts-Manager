# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20180712_0703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='strikes',
        ),
        migrations.AddField(
            model_name='employee',
            name='call_offs',
            field=models.IntegerField(default=3),
        ),
    ]
