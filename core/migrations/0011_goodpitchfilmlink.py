# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20150515_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodpitchFilmLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('creator_id', models.IntegerField(null=True, editable=False, blank=True)),
                ('last_editor_id', models.IntegerField(null=True, editable=False, blank=True)),
                ('status', models.IntegerField(default=0, choices=[(0, b'Active'), (1, b'Inactive')])),
                ('title', models.CharField(max_length=128, verbose_name=b'Descriptive name for goodpitch event')),
                ('slug', models.CharField(unique=True, max_length=12, verbose_name=b'Slug on goodpitch site - e.g. gp2012eu')),
                ('films', models.ManyToManyField(related_name='goodpitches', to='core.Film')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
