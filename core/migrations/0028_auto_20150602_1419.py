# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20150602_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharelink',
            name='url',
            field=models.URLField(max_length=128, verbose_name=b'URL for link', blank=True),
        ),
        migrations.AlterField(
            model_name='sharelink',
            name='name',
            field=models.CharField(max_length=128, verbose_name=b'Type of link', choices=[(b'FACEBOOK', b'Facebook'), (b'TWITTER', b'Twitter'), (b'WEBSITE', b'Film Website')]),
        ),
        migrations.AlterField(
            model_name='sharelink',
            name='text',
            field=models.CharField(max_length=128, verbose_name=b'Optional text to use on link', blank=True),
        ),
    ]
