# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20150519_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodpitch',
            name='slug',
            field=models.CharField(unique=True, max_length=20, verbose_name=b'Slug on goodpitch site - e.g. gp2012eu'),
        ),
    ]
