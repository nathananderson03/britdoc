# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20150515_1311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='production_year',
            new_name='year',
        ),
    ]
