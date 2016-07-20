# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20150515_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseLink',
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
                ('film', models.ForeignKey(related_name='purchase_links', to='core.Film')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShareLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('creator_id', models.IntegerField(null=True, editable=False, blank=True)),
                ('last_editor_id', models.IntegerField(null=True, editable=False, blank=True)),
                ('status', models.IntegerField(default=0, choices=[(0, b'Active'), (1, b'Inactive')])),
                ('name', models.CharField(max_length=128, verbose_name=b'Type of sharing link', choices=[(b'FACEBOOK', b'Facebook'), (b'TWITTER', b'Twitter')])),
                ('text', models.CharField(max_length=128, verbose_name=b'Optional text to use on share link', blank=True)),
                ('film', models.ForeignKey(related_name='share_links', to='core.Film')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='filmpurchaselink',
            name='film',
        ),
        migrations.AlterField(
            model_name='filmimage',
            name='film',
            field=models.ForeignKey(related_name='images', to='core.Film'),
        ),
        migrations.DeleteModel(
            name='FilmPurchaseLink',
        ),
    ]
