# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datum', models.DateField()),
                ('name', models.CharField(max_length=50, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort', models.IntegerField(default=0, db_index=True)),
                ('image', filer.fields.image.FilerImageField(to='filer.Image')),
            ],
            options={
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(verbose_name='content')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('slug', models.SlugField()),
                ('images', models.ManyToManyField(to='teams.Image', blank=True)),
            ],
            options={
                'ordering': ['slug'],
            },
        ),
        migrations.CreateModel(
            name='PersonalSponsor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('image', filer.fields.image.FilerImageField(blank=True, to='filer.Image', null=True)),
                ('person', models.ForeignKey(to='teams.Person')),
            ],
        ),
        migrations.CreateModel(
            name='PersonAttribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('birthdate', models.DateField(null=True, blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail address', blank=True)),
                ('height', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('weight', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('person', models.OneToOneField(related_name='attributes', to='teams.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'season',
                'verbose_name_plural': 'seasons',
            },
        ),
        migrations.CreateModel(
            name='Squad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('content', models.TextField(verbose_name='content')),
                ('sortorder', models.SmallIntegerField(default=0)),
                ('images', models.ManyToManyField(to='teams.Image', blank=True)),
                ('predecessor', models.ForeignKey(related_name='predecessor_set', blank=True, to='teams.Squad', null=True)),
                ('season', models.ForeignKey(to='teams.Season')),
                ('successor', models.ForeignKey(related_name='successor_set', blank=True, to='teams.Squad', null=True)),
            ],
            options={
                'ordering': ['team', 'season', 'sortorder', 'name'],
                'verbose_name': 'squad',
                'verbose_name_plural': 'squads',
            },
        ),
        migrations.CreateModel(
            name='SquadPerson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sortorder', models.SmallIntegerField(default=0)),
            ],
            options={
                'ordering': ['sortorder'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('sortorder', models.SmallIntegerField(default=0)),
                ('images', models.ManyToManyField(to='teams.Image', blank=True)),
                ('lastsquad', models.ForeignKey(related_name='lastteam_set', blank=True, to='teams.Squad', null=True)),
            ],
            options={
                'ordering': ['sortorder', 'name'],
                'verbose_name': 'team',
                'verbose_name_plural': 'teams',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('squadperson_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='teams.SquadPerson')),
                ('address', models.CharField(max_length=100, null=True, blank=True)),
                ('phone', models.CharField(max_length=15, null=True, blank=True)),
            ],
            bases=('teams.squadperson',),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('squadperson_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='teams.SquadPerson')),
                ('number', models.SmallIntegerField()),
                ('positions', models.ManyToManyField(to='teams.Position')),
            ],
            options={
                'ordering': ['number', 'sortorder', 'person'],
            },
            bases=('teams.squadperson',),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('squadperson_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='teams.SquadPerson')),
                ('function', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['sortorder', 'person'],
            },
            bases=('teams.squadperson',),
        ),
        migrations.AddField(
            model_name='squadperson',
            name='date_joined',
            field=models.ForeignKey(related_name='teams_squadperson_date_joined', blank=True, to='teams.Date', null=True),
        ),
        migrations.AddField(
            model_name='squadperson',
            name='date_left',
            field=models.ForeignKey(related_name='teams_squadperson_date_left', blank=True, to='teams.Date', null=True),
        ),
        migrations.AddField(
            model_name='squadperson',
            name='person',
            field=models.ForeignKey(related_name='teams_squadperson_person', to='teams.Person'),
        ),
        migrations.AddField(
            model_name='squadperson',
            name='squad',
            field=models.ForeignKey(related_name='teams_squadperson_squad', to='teams.Squad'),
        ),
        migrations.AddField(
            model_name='squad',
            name='team',
            field=models.ForeignKey(related_name='teams_squad_related', to='teams.Team', null=True),
        ),
        migrations.AddField(
            model_name='squad',
            name='contacts',
            field=models.ManyToManyField(related_name='teams_squad_contact_related', through='teams.Contact', to='teams.Person'),
        ),
        migrations.AddField(
            model_name='squad',
            name='players',
            field=models.ManyToManyField(related_name='teams_squad_players_related', through='teams.Player', to='teams.Person'),
        ),
        migrations.AddField(
            model_name='squad',
            name='staff',
            field=models.ManyToManyField(related_name='teams_squad_staff_related', through='teams.Staff', to='teams.Person'),
        ),
        migrations.AlterOrderWithRespectTo(
            name='squad',
            order_with_respect_to='team',
        ),
    ]
