# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_filmimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmimage',
            name='height',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='filmimage',
            name='image',
            field=models.ImageField(height_field=b'height', width_field=b'width', upload_to=b'film'),
        ),
        migrations.AlterField(
            model_name='filmimage',
            name='width',
            field=models.PositiveIntegerField(editable=False),
        ),
    ]
