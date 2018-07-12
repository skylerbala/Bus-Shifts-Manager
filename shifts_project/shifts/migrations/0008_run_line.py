# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0007_auto_20180711_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='run',
            name='line',
            field=models.CharField(default=datetime.datetime(2018, 7, 11, 21, 9, 20, 367357, tzinfo=utc), max_length=1),
            preserve_default=False,
        ),
    ]
