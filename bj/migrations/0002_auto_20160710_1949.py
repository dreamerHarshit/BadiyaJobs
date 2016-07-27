# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bj', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='year_founded',
            field=models.IntegerField(),
        ),
    ]
