# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_film_trailer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharelink',
            name='name',
            field=models.CharField(max_length=128, verbose_name=b'Type of link', choices=[(b'FACEBOOK', b'Facebook'), (b'TWITTER', b'Twitter'), (b'WEBSITE', b'Film Website'), (b'DOCACADEMY', b'Docacademy Link')]),
        ),
    ]
