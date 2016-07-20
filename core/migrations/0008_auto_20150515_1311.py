# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20150515_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='subject',
            field=models.CharField(max_length=65536, verbose_name='Subject', blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='synopsis',
            field=redactor.fields.RedactorField(max_length=65536, verbose_name='Synopsis'),
        ),
    ]
