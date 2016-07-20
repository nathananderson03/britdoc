# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20150518_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fund',
            name='film',
        ),
        migrations.AddField(
            model_name='fund',
            name='films',
            field=models.ManyToManyField(related_name='funds', to='core.Film'),
        ),
    ]
