# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_auto_20150605_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='trailer',
            field=models.URLField(default='', verbose_name='Film Trailer Link', blank=True),
            preserve_default=False,
        ),
    ]
