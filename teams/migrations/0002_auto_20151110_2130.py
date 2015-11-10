# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='squad',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='team',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
