# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_mailout'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mailout',
            new_name='MailoutSignup',
        ),
    ]
