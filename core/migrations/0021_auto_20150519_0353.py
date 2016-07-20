# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20150519_0338'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='temp_according_to_filmmakers',
            field=models.CharField(max_length=65536, verbose_name=b'temporary copy of old according to filmmakers', blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='temp_quote_attribution',
            field=models.CharField(max_length=65536, verbose_name=b'temporary copy of old quote attribution field', blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='temp_quote_text',
            field=models.CharField(max_length=65536, verbose_name=b'temporary copy of quote text field', blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='temp_related_links',
            field=models.CharField(max_length=65536, verbose_name=b'temporary copy of old related links field', blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='temp_sales_contacts',
            field=models.CharField(max_length=65536, verbose_name=b'temporary copy of old sales field', blank=True),
        ),
        migrations.AddField(
            model_name='film',
            name='temp_trailer_url',
            field=models.CharField(max_length=65536, verbose_name=b'temporary copy of old trailer url field', blank=True),
        ),
    ]
