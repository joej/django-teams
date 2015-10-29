# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20151021_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='images',
            field=models.ManyToManyField(related_name='teams_person_image', to='teams.Image', blank=True),
        ),
        migrations.AlterField(
            model_name='squad',
            name='images',
            field=models.ManyToManyField(related_name='teams_squad_image', to='teams.Image', blank=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='images',
            field=models.ManyToManyField(related_name='teams_team_image', to='teams.Image', blank=True),
        ),
    ]
