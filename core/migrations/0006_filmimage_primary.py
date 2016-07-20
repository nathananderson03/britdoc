# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_filmimage_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmimage',
            name='primary',
            field=models.BooleanField(default=False),
        ),
    ]
