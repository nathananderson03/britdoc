# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_auto_20150612_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcecategory',
            name='description',
            field=redactor.fields.RedactorField(max_length=65536, verbose_name='Section Introduction', blank=True),
        ),
    ]
