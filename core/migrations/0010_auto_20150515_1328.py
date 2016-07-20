# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20150515_1314'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilmPurchaseLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('creator_id', models.IntegerField(null=True, editable=False, blank=True)),
                ('last_editor_id', models.IntegerField(null=True, editable=False, blank=True)),
                ('status', models.IntegerField(default=0, choices=[(0, b'Active'), (1, b'Inactive')])),
                ('name', models.CharField(max_length=128, verbose_name=b'Service - i.e. iTunes')),
                ('title', models.CharField(max_length=128, verbose_name=b'Longer name i.e. Watch this film on iTunes in the UK', blank=True)),
                ('url', models.URLField(max_length=256, verbose_name=b'Link to view film. Will be shortened automatically')),
                ('country', django_countries.fields.CountryField(max_length=2, verbose_name=b'Country')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='film',
            name='year',
            field=models.IntegerField(default=2015, verbose_name='Year of Completion', choices=[(2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015)]),
        ),
        migrations.AddField(
            model_name='filmpurchaselink',
            name='film',
            field=models.ForeignKey(related_name='filmsites', to='core.Film'),
        ),
    ]
