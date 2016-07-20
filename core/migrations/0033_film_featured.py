# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_auto_20150604_0705'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='featured',
            field=models.BooleanField(default=False, verbose_name=b'Featured - show in main index page or not'),
        ),
    ]
