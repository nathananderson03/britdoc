# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_auto_20150605_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='recommended',
            field=models.ManyToManyField(related_name='recommended_rel_+', verbose_name=b'Also Recommended', to='core.Film', blank=True),
        ),
    ]
