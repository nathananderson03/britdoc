# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20150519_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crew',
            name='height',
            field=models.PositiveIntegerField(editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='crew',
            name='image',
            field=models.ImageField(height_field=b'height', width_field=b'width', upload_to=b'crew', blank=True),
        ),
        migrations.AlterField(
            model_name='crew',
            name='width',
            field=models.PositiveIntegerField(editable=False, blank=True),
        ),
    ]
