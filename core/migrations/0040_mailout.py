# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_auto_20150608_0948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mailout',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('creator_id', models.IntegerField(null=True, editable=False, blank=True)),
                ('last_editor_id', models.IntegerField(null=True, editable=False, blank=True)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('first_name', models.CharField(max_length=128, blank=True)),
                ('last_name', models.CharField(max_length=128, blank=True)),
                ('job_title', models.CharField(max_length=128)),
                ('region', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
