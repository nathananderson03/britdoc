# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='brtidoc_help_outreach',
            new_name='britdoc_help_outreach',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='brtidoc_help_production',
            new_name='britdoc_help_production',
        ),
    ]
