# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('enemies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='state',
            field=django_fsm.FSMIntegerField(default=10, choices=[(10, b'wandering'), (20, b'attacking'), (30, b'looking_for_aid'), (40, b'evading')]),
        ),
    ]
