# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='wage',
        ),
        migrations.AddField(
            model_name='employee',
            name='city',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='employee',
            name='description',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='employee',
            name='website',
            field=models.URLField(default=b''),
        ),
    ]
