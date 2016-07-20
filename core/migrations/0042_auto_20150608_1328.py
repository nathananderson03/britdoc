# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_auto_20150608_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='involvement',
            field=models.CharField(blank=True, max_length=128, choices=[(b'STAFF', b'Staff'), (b'FREELANCE', b'Freelance'), (b'FOUNDATION', b'Foundation'), (b'CHARITY', b'Charity'), (b'BRITDOC_INC', b'Britdoc INC'), (b'CONSULTANT', b'Consultant')]),
        ),
    ]
