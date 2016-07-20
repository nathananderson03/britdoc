# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20150519_0353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('creator_id', models.IntegerField(null=True, editable=False, blank=True)),
                ('last_editor_id', models.IntegerField(null=True, editable=False, blank=True)),
                ('status', models.IntegerField(default=0, choices=[(0, b'Active'), (1, b'Inactive')])),
                ('body', redactor.fields.RedactorField(max_length=65536, verbose_name=b'Review Copy')),
                ('attribution', models.CharField(max_length=128, verbose_name=b'Review Attribution')),
                ('film', models.ForeignKey(related_name='reviews', to='core.Film')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
