# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20150518_1929'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilmCrew',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('creator_id', models.IntegerField(null=True, editable=False, blank=True)),
                ('last_editor_id', models.IntegerField(null=True, editable=False, blank=True)),
                ('status', models.IntegerField(default=0, choices=[(0, b'Active'), (1, b'Inactive')])),
                ('name', models.CharField(unique=True, max_length=255)),
                ('slug', models.SlugField(help_text=b'Automatically generated', max_length=255)),
                ('image', models.ImageField(height_field=b'height', width_field=b'width', upload_to=b'crew')),
                ('height', models.PositiveIntegerField(editable=False)),
                ('width', models.PositiveIntegerField(editable=False)),
                ('role', models.CharField(max_length=40)),
                ('about', redactor.fields.RedactorField(max_length=65536, verbose_name='About', blank=True)),
                ('films', models.ManyToManyField(related_name='crew', to='core.Film')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
