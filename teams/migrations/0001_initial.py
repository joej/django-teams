# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    depends_on = (
        ("cms", "0001_initial"),
    )

    def forwards(self, orm):
        # Adding model 'PersonAttributeBase'
        db.create_table('teams_personattributebase', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.OneToOneField')(related_name='attributes', unique=True, to=orm['teams.Person'])),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('birthdate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('teams', ['PersonAttributeBase'])

        # Adding model 'Position'
        db.create_table('teams_position', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal('teams', ['Position'])

        # Adding model 'Person'
        db.create_table('teams_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('sortorder', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('content_placeholder', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Placeholder'], null=True)),
        ))
        db.send_create_signal('teams', ['Person'])

        # Adding model 'PersonAttribute'
        db.create_table('teams_personattribute', (
            ('personattributebase_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['teams.PersonAttributeBase'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('teams', ['PersonAttribute'])

        # Adding model 'Team'
        db.create_table('teams_team', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('sortorder', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('lastsquad', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='lastteam_set', null=True, to=orm['teams.Squad'])),
        ))
        db.send_create_signal('teams', ['Team'])

        # Adding model 'ExternalTeam'
        db.create_table('teams_externalteam', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('teams', ['ExternalTeam'])

        # Adding model 'Date'
        db.create_table('teams_date', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('datum', self.gf('django.db.models.fields.DateField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal('teams', ['Date'])

        # Adding model 'Player'
        db.create_table('teams_player', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(related_name='teams_player_person', to=orm['teams.Person'])),
            ('squad', self.gf('django.db.models.fields.related.ForeignKey')(related_name='teams_player_squad', to=orm['teams.Squad'])),
            ('date_joined', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='teams_player_date_joined', null=True, to=orm['teams.Date'])),
            ('date_left', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='teams_player_date_left', null=True, to=orm['teams.Date'])),
            ('number', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal('teams', ['Player'])

        # Adding M2M table for field positions on 'Player'
        db.create_table('teams_player_positions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('player', models.ForeignKey(orm['teams.player'], null=False)),
            ('position', models.ForeignKey(orm['teams.position'], null=False))
        ))
        db.create_unique('teams_player_positions', ['player_id', 'position_id'])

        # Adding model 'Contact'
        db.create_table('teams_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(related_name='teams_contact_person', to=orm['teams.Person'])),
            ('squad', self.gf('django.db.models.fields.related.ForeignKey')(related_name='teams_contact_squad', to=orm['teams.Squad'])),
            ('date_joined', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='teams_contact_date_joined', null=True, to=orm['teams.Date'])),
            ('date_left', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='teams_contact_date_left', null=True, to=orm['teams.Date'])),
            ('sortorder', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
        ))
        db.send_create_signal('teams', ['Contact'])

        # Adding model 'Staff'
        db.create_table('teams_staff', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(related_name='teams_staff_person', to=orm['teams.Person'])),
            ('squad', self.gf('django.db.models.fields.related.ForeignKey')(related_name='teams_staff_squad', to=orm['teams.Squad'])),
            ('date_joined', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='teams_staff_date_joined', null=True, to=orm['teams.Date'])),
            ('date_left', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='teams_staff_date_left', null=True, to=orm['teams.Date'])),
            ('sortorder', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('function', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('teams', ['Staff'])

        # Adding model 'Transfer'
        db.create_table('teams_transfer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teams.Person'])),
            ('old', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='leaving', null=True, to=orm['teams.Squad'])),
            ('oldextern', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='leaving_ext', null=True, to=orm['teams.ExternalTeam'])),
            ('new', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='joining', null=True, to=orm['teams.Squad'])),
            ('newextern', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='joining_ext', null=True, to=orm['teams.ExternalTeam'])),
        ))
        db.send_create_signal('teams', ['Transfer'])

        # Adding model 'Squad'
        db.create_table('teams_squad', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('sortorder', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('predecessor', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='predecessor_set', null=True, to=orm['teams.Squad'])),
            ('successor', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='successor_set', null=True, to=orm['teams.Squad'])),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(related_name='squad_set', null=True, to=orm['teams.Team'])),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teams.Season'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('content_placeholder', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Placeholder'], null=True)),
        ))
        db.send_create_signal('teams', ['Squad'])

        # Adding model 'Season'
        db.create_table('teams_season', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal('teams', ['Season'])

        # Adding model 'SquadPlayerCopy'
        db.create_table('teams_squadplayercopy', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(related_name='source_copies', to=orm['teams.Squad'])),
            ('target', self.gf('django.db.models.fields.related.ForeignKey')(related_name='target_copies', to=orm['teams.Squad'])),
        ))
        db.send_create_signal('teams', ['SquadPlayerCopy'])

        # Adding model 'PersonImage'
        db.create_table('teams_personimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teams.Person'])),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['filer.Image'], null=True, blank=True)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True)),
        ))
        db.send_create_signal('teams', ['PersonImage'])

        # Adding model 'TeamImage'
        db.create_table('teams_teamimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teams.Team'])),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['filer.Image'], null=True, blank=True)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True)),
        ))
        db.send_create_signal('teams', ['TeamImage'])

        # Adding model 'SquadImage'
        db.create_table('teams_squadimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('squad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teams.Squad'])),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['filer.Image'], null=True, blank=True)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True)),
        ))
        db.send_create_signal('teams', ['SquadImage'])

        # Adding model 'TransferUpdate'
        db.create_table('teams_transferupdate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('teams', ['TransferUpdate'])


    def backwards(self, orm):
        # Deleting model 'PersonAttributeBase'
        db.delete_table('teams_personattributebase')

        # Deleting model 'Position'
        db.delete_table('teams_position')

        # Deleting model 'Person'
        db.delete_table('teams_person')

        # Deleting model 'PersonAttribute'
        db.delete_table('teams_personattribute')

        # Deleting model 'Team'
        db.delete_table('teams_team')

        # Deleting model 'ExternalTeam'
        db.delete_table('teams_externalteam')

        # Deleting model 'Date'
        db.delete_table('teams_date')

        # Deleting model 'Player'
        db.delete_table('teams_player')

        # Removing M2M table for field positions on 'Player'
        db.delete_table('teams_player_positions')

        # Deleting model 'Contact'
        db.delete_table('teams_contact')

        # Deleting model 'Staff'
        db.delete_table('teams_staff')

        # Deleting model 'Transfer'
        db.delete_table('teams_transfer')

        # Deleting model 'Squad'
        db.delete_table('teams_squad')

        # Deleting model 'Season'
        db.delete_table('teams_season')

        # Deleting model 'SquadPlayerCopy'
        db.delete_table('teams_squadplayercopy')

        # Deleting model 'PersonImage'
        db.delete_table('teams_personimage')

        # Deleting model 'TeamImage'
        db.delete_table('teams_teamimage')

        # Deleting model 'SquadImage'
        db.delete_table('teams_squadimage')

        # Deleting model 'TransferUpdate'
        db.delete_table('teams_transferupdate')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'filer.file': {
            'Meta': {'object_name': 'File'},
            '_file_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'all_files'", 'null': 'True', 'to': "orm['filer.Folder']"}),
            'has_all_mandatory_data': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'original_filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'owned_files'", 'null': 'True', 'to': "orm['auth.User']"}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_filer.file_set'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'sha1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40', 'blank': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'filer.folder': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('parent', 'name'),)", 'object_name': 'Folder'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'filer_owned_folders'", 'null': 'True', 'to': "orm['auth.User']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['filer.Folder']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'filer.image': {
            'Meta': {'object_name': 'Image', '_ormbases': ['filer.File']},
            '_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            '_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'default_alt_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'default_caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'file_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['filer.File']", 'unique': 'True', 'primary_key': 'True'}),
            'must_always_publish_author_credit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'must_always_publish_copyright': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject_location': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '64', 'null': 'True', 'blank': 'True'})
        },
        'teams.contact': {
            'Meta': {'object_name': 'Contact'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'teams_contact_date_joined'", 'null': 'True', 'to': "orm['teams.Date']"}),
            'date_left': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'teams_contact_date_left'", 'null': 'True', 'to': "orm['teams.Date']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'teams_contact_person'", 'to': "orm['teams.Person']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'sortorder': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'squad': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'teams_contact_squad'", 'to': "orm['teams.Squad']"})
        },
        'teams.date': {
            'Meta': {'object_name': 'Date'},
            'datum': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'teams.externalteam': {
            'Meta': {'object_name': 'ExternalTeam'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'teams.person': {
            'Meta': {'object_name': 'Person'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'sortorder': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        },
        'teams.personattribute': {
            'Meta': {'object_name': 'PersonAttribute', '_ormbases': ['teams.PersonAttributeBase']},
            'personattributebase_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['teams.PersonAttributeBase']", 'unique': 'True', 'primary_key': 'True'})
        },
        'teams.personattributebase': {
            'Meta': {'object_name': 'PersonAttributeBase'},
            'birthdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'attributes'", 'unique': 'True', 'to': "orm['teams.Person']"}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'teams.personimage': {
            'Meta': {'ordering': "['sort']", 'object_name': 'PersonImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.Image']", 'null': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teams.Person']"}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'})
        },
        'teams.player': {
            'Meta': {'ordering': "['squad', 'number', 'person']", 'object_name': 'Player'},
            'date_joined': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'teams_player_date_joined'", 'null': 'True', 'to': "orm['teams.Date']"}),
            'date_left': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'teams_player_date_left'", 'null': 'True', 'to': "orm['teams.Date']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.SmallIntegerField', [], {}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'teams_player_person'", 'to': "orm['teams.Person']"}),
            'positions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['teams.Position']", 'symmetrical': 'False'}),
            'squad': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'teams_player_squad'", 'to': "orm['teams.Squad']"})
        },
        'teams.position': {
            'Meta': {'object_name': 'Position'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'teams.season': {
            'Meta': {'ordering': "['name']", 'object_name': 'Season'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'teams.squad': {
            'Meta': {'object_name': 'Squad'},
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'contact_squad'", 'symmetrical': 'False', 'through': "orm['teams.Contact']", 'to': "orm['teams.Person']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'players': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'player_squad'", 'symmetrical': 'False', 'through': "orm['teams.Player']", 'to': "orm['teams.Person']"}),
            'predecessor': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'predecessor_set'", 'null': 'True', 'to': "orm['teams.Squad']"}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teams.Season']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'sortorder': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'staff': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'staff_squad'", 'symmetrical': 'False', 'through': "orm['teams.Staff']", 'to': "orm['teams.Person']"}),
            'successor': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'successor_set'", 'null': 'True', 'to': "orm['teams.Squad']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'squad_set'", 'null': 'True', 'to': "orm['teams.Team']"})
        },
        'teams.squadimage': {
            'Meta': {'object_name': 'SquadImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.Image']", 'null': 'True', 'blank': 'True'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'squad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teams.Squad']"})
        },
        'teams.squadplayercopy': {
            'Meta': {'object_name': 'SquadPlayerCopy'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'source_copies'", 'to': "orm['teams.Squad']"}),
            'target': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'target_copies'", 'to': "orm['teams.Squad']"})
        },
        'teams.staff': {
            'Meta': {'ordering': "['squad', 'sortorder', 'person']", 'object_name': 'Staff'},
            'date_joined': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'teams_staff_date_joined'", 'null': 'True', 'to': "orm['teams.Date']"}),
            'date_left': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'teams_staff_date_left'", 'null': 'True', 'to': "orm['teams.Date']"}),
            'function': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'teams_staff_person'", 'to': "orm['teams.Person']"}),
            'sortorder': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'squad': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'teams_staff_squad'", 'to': "orm['teams.Squad']"})
        },
        'teams.team': {
            'Meta': {'ordering': "['sortorder', 'name']", 'object_name': 'Team'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastsquad': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'lastteam_set'", 'null': 'True', 'to': "orm['teams.Squad']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'sortorder': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        },
        'teams.teamimage': {
            'Meta': {'object_name': 'TeamImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.Image']", 'null': 'True', 'blank': 'True'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teams.Team']"})
        },
        'teams.transfer': {
            'Meta': {'ordering': "['person']", 'object_name': 'Transfer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'new': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'joining'", 'null': 'True', 'to': "orm['teams.Squad']"}),
            'newextern': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'joining_ext'", 'null': 'True', 'to': "orm['teams.ExternalTeam']"}),
            'old': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'leaving'", 'null': 'True', 'to': "orm['teams.Squad']"}),
            'oldextern': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'leaving_ext'", 'null': 'True', 'to': "orm['teams.ExternalTeam']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teams.Person']"})
        },
        'teams.transferupdate': {
            'Meta': {'object_name': 'TransferUpdate'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['teams']