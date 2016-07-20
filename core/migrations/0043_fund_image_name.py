# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0042_auto_20150608_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='fund',
            name='image_name',
            field=models.CharField(max_length=128, verbose_name=b'The name of the image used on site', blank=True),
        ),
    ]
