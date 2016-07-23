# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20151113_1814'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ListModel',
        ),
    ]
