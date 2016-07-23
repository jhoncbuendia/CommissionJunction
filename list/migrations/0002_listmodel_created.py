# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listmodel',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 18, 18, 28, 23, 192575, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
