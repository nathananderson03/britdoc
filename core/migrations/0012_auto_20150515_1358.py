# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_goodpitchfilmlink'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GoodpitchFilmLink',
            new_name='Goodpitch',
        ),
    ]
