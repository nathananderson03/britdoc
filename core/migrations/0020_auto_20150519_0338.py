# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20150519_0335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crew',
            name='height',
            field=models.PositiveIntegerField(null=True, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='crew',
            name='width',
            field=models.PositiveIntegerField(null=True, editable=False, blank=True),
        ),
    ]
