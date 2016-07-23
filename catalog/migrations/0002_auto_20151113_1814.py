# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listmodel',
            options={'verbose_name': 'lista', 'verbose_name_plural': 'listas'},
        ),
        migrations.AlterField(
            model_name='listmodel',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
