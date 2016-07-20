# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150511_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilmImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('creator_id', models.IntegerField(null=True, editable=False, blank=True)),
                ('last_editor_id', models.IntegerField(null=True, editable=False, blank=True)),
                ('height', models.IntegerField()),
                ('width', models.IntegerField()),
                ('image', models.ImageField(height_field=models.IntegerField(), width_field=models.IntegerField(), upload_to=b'film')),
                ('film', models.ForeignKey(to='core.Film')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
