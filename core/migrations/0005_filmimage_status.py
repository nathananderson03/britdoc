# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150513_0709'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmimage',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, b'Active'), (1, b'Inactive')]),
        ),
    ]
