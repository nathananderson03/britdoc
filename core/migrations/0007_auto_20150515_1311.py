# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_filmimage_primary'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='britdoc_help_development',
            field=models.BooleanField(default=False, verbose_name=b'Britdoc helped with DEVELOPMENT'),
        ),
        migrations.AddField(
            model_name='film',
            name='britdoc_help_goodpitch',
            field=models.BooleanField(default=False, verbose_name=b'Britdoc helped at GOODPITCH'),
        ),
        migrations.AddField(
            model_name='film',
            name='brtidoc_help_outreach',
            field=models.BooleanField(default=False, verbose_name=b'Britdoc helped with OUTREACH'),
        ),
        migrations.AddField(
            model_name='film',
            name='brtidoc_help_production',
            field=models.BooleanField(default=False, verbose_name=b'Britdoc helped in PRODUCTION'),
        ),
        migrations.AddField(
            model_name='film',
            name='runtime',
            field=models.IntegerField(null=True, verbose_name='Runtime in Minutes', blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='stage',
            field=models.CharField(default=b'COMPLETED', max_length=20, verbose_name='Production Stage', choices=[(b'DEVELOPMENT', b'In Development'), (b'COMPLETED', b'Completed')]),
        ),
        migrations.AlterField(
            model_name='film',
            name='synopsis',
            field=models.CharField(max_length=65536, verbose_name='Subject', blank=True),
        ),
    ]
