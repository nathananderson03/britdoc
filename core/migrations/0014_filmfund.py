# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20150515_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilmFund',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('creator_id', models.IntegerField(null=True, editable=False, blank=True)),
                ('last_editor_id', models.IntegerField(null=True, editable=False, blank=True)),
                ('status', models.IntegerField(default=0, choices=[(0, b'Active'), (1, b'Inactive')])),
                ('name', models.CharField(unique=True, max_length=255)),
                ('slug', models.SlugField(help_text=b'Automatically generated', max_length=255)),
                ('film', models.ForeignKey(related_name='funds', to='core.Film')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
