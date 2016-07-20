# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0046_resourcecategory_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='crew',
            options={'verbose_name_plural': 'Crew'},
        ),
        migrations.AlterModelOptions(
            name='goodpitch',
            options={'verbose_name_plural': 'Goodpitches'},
        ),
        migrations.AlterModelOptions(
            name='resourcecategory',
            options={'verbose_name_plural': 'Resource Categories'},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'verbose_name_plural': 'Staff'},
        ),
    ]
