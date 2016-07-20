# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_film_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('creator_id', models.IntegerField(null=True, editable=False, blank=True)),
                ('last_editor_id', models.IntegerField(null=True, editable=False, blank=True)),
                ('status', models.IntegerField(default=0, choices=[(0, b'Active'), (1, b'Inactive')])),
                ('name', models.CharField(unique=True, max_length=255)),
                ('slug', models.SlugField(help_text=b'Automatically generated', max_length=255)),
                ('image', models.ImageField(height_field=b'height', width_field=b'width', upload_to=b'crew', blank=True)),
                ('height', models.PositiveIntegerField(null=True, editable=False, blank=True)),
                ('width', models.PositiveIntegerField(null=True, editable=False, blank=True)),
                ('role', models.CharField(max_length=40)),
                ('about', redactor.fields.RedactorField(max_length=65536, verbose_name='About', blank=True)),
                ('involvement', models.CharField(blank=True, max_length=128, choices=[(b'STAFF', b'Staff'), (b'FREELANCE', b'Freelance'), (b'FOUNDATION', b'Foundation'), (b'CHARITY', b'Charity'), (b'BRITDOC_INC', b'Britdoc INC')])),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
