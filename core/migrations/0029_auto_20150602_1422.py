# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_auto_20150602_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaselink',
            name='url',
            field=models.URLField(max_length=256, verbose_name=b'Link to view film.'),
        ),
    ]
