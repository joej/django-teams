# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20151110_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='squad',
            name='shv_id',
        ),
        migrations.AddField(
            model_name='squad',
            name='shv_group_id',
            field=models.CharField(max_length=5, blank=True),
        ),
        migrations.AddField(
            model_name='squad',
            name='shv_saison_id',
            field=models.CharField(max_length=5, blank=True),
        ),
        migrations.AddField(
            model_name='squad',
            name='shv_team_id',
            field=models.CharField(max_length=5, blank=True),
        ),
    ]
