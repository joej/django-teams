# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='squadperson',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='squadperson',
            name='date_left',
        ),
        migrations.DeleteModel(
            name='Date',
        ),
    ]
