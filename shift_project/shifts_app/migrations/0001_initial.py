# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(default=0, blank=True)),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
            ],
            options={
                'db_table': 'run',
            },
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
            ],
            options={
                'db_table': 'shift',
            },
        ),
        migrations.CreateModel(
            name='ShiftGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
                ('start_date_range', models.DateField()),
                ('end_date_range', models.DateField()),
            ],
            options={
                'db_table': 'shift_groups',
            },
        ),
        migrations.AddField(
            model_name='shift',
            name='shift_group',
            field=models.ForeignKey(related_name='shift_set', to='shifts_app.ShiftGroup'),
        ),
        migrations.AddField(
            model_name='run',
            name='shift',
            field=models.ForeignKey(to='shifts_app.Shift'),
        ),
    ]
