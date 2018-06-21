# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shifts_app', '0002_run_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='shift',
            field=models.ForeignKey(to='shifts_app.Shift'),
        ),
    ]
