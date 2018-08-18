# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='city',
        ),
        migrations.AddField(
            model_name='employee',
            name='strikes',
            field=models.IntegerField(default=5),
        ),
    ]
