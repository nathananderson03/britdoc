# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laurel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('creator_id', models.IntegerField(null=True, editable=False, blank=True)),
                ('last_editor_id', models.IntegerField(null=True, editable=False, blank=True)),
                ('status', models.IntegerField(default=0, choices=[(0, b'Active'), (1, b'Inactive')])),
                ('award', models.CharField(max_length=128, verbose_name=b'Name of award')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='film',
            name='trailer',
            field=models.URLField(max_length=256, null=True, verbose_name='Film Trailer'),
        ),
        migrations.AddField(
            model_name='laurel',
            name='film',
            field=models.ForeignKey(to='core.Film'),
        ),
    ]
