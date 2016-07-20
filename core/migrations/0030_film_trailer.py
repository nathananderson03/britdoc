# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20150602_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='trailer',
            field=models.URLField(verbose_name='Trailer Link', blank=True),
        ),
    ]
