# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('shifts', '0002_auto_20180710_0758'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='employee',
            field=models.ForeignKey(related_name='employee_set', default=1, blank=True, to='accounts.Employee'),
            preserve_default=False,
        ),
    ]
