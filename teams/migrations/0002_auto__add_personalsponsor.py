# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PersonalSponsor'
        db.create_table(u'teams_personalsponsor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['filer.Image'], null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teams.Person'])),
        ))
        db.send_create_signal(u'teams', ['PersonalSponsor'])


    def backwards(self, orm):
        # Deleting model 'PersonalSponsor'
        db.delete_table(u'teams_personalsponsor')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'original_filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'owned_files'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_filer.file_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'sha1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40', 'blank': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'filer.folder': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('parent', 'name'),)", 'object_name': 'Folder'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'filer_owned_folders'", 'null': 'True', 'to': u"orm['auth.User']"}),
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
            u'file_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['filer.File']", 'unique': 'True', 'primary_key': 'True'}),
            'must_always_publish_author_credit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'must_always_publish_copyright': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject_location': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '64', 'null': 'True', 'blank': 'True'})
        },
        u'teams.contact': {
            'Meta': {'object_name': 'Contact'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'teams_contact_date_joined'", 'null': 'True', 'to': u"orm['teams.Date']"}),
            'date_left': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'teams_contact_date_left'", 'null': 'True', 'to': u"orm['teams.Date']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'teams_contact_person'", 'to': u"orm['teams.Person']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'sortorder': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'squad': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'teams_contact_squad'", 'to': u"orm['teams.Squad']"})
        },
        u'teams.date': {
            'Meta': {'object_name': 'Date'},
            'datum': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'teams.externalteam': {
            'Meta': {'object_name': 'ExternalTeam'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'teams.person': {
            'Meta': {'object_name': 'Person'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'sortorder': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        },
        u'teams.personalsponsor': {
            'Meta': {'object_name': 'PersonalSponsor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.Image']", 'null': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teams.Person']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'teams.personattribute': {
            'Meta': {'object_name': 'PersonAttribute', '_ormbases': [u'teams.PersonAttributeBase']},
            u'personattributebase_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['teams.PersonAttributeBase']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'teams.personattributebase': {
            'Meta': {'object_name': 'PersonAttributeBase'},
            'birthdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'attributes'", 'unique': 'True', 'to': u"orm['teams.Person']"}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'teams.personimage': {
            'Meta': {'ordering': "['sort']", 'object_name': 'PersonImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.Image']", 'null': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teams.Person']"}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'})
        },
        u'teams.player': {
            'Meta': {'ordering': "['squad', 'number', 'person']", 'object_name': 'Player'},
            'date_joined': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'teams_player_date_joined'", 'null': 'True', 'to': u"orm['teams.Date']"}),
            'date_left': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'teams_player_date_left'", 'null': 'True', 'to': u"orm['teams.Date']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.SmallIntegerField', [], {}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'teams_player_person'", 'to': u"orm['teams.Person']"}),
            'positions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['teams.Position']", 'symmetrical': 'False'}),
            'squad': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'teams_player_squad'", 'to': u"orm['teams.Squad']"})
        },
        u'teams.position': {
            'Meta': {'object_name': 'Position'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'teams.season': {
            'Meta': {'ordering': "['name']", 'object_name': 'Season'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'teams.squad': {
            'Meta': {'object_name': 'Squad'},
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'contact_squad'", 'symmetrical': 'False', 'through': u"orm['teams.Contact']", 'to': u"orm['teams.Person']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'players': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'player_squad'", 'symmetrical': 'False', 'through': u"orm['teams.Player']", 'to': u"orm['teams.Person']"}),
            'predecessor': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'predecessor_set'", 'null': 'True', 'to': u"orm['teams.Squad']"}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teams.Season']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'sortorder': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'staff': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'staff_squad'", 'symmetrical': 'False', 'through': u"orm['teams.Staff']", 'to': u"orm['teams.Person']"}),
            'successor': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'successor_set'", 'null': 'True', 'to': u"orm['teams.Squad']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'squad_set'", 'null': 'True', 'to': u"orm['teams.Team']"})
        },
        u'teams.squadimage': {
            'Meta': {'object_name': 'SquadImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.Image']", 'null': 'True', 'blank': 'True'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'squad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teams.Squad']"})
        },
        u'teams.squadplayercopy': {
            'Meta': {'object_name': 'SquadPlayerCopy'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'source_copies'", 'to': u"orm['teams.Squad']"}),
            'target': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'target_copies'", 'to': u"orm['teams.Squad']"})
        },
        u'teams.staff': {
            'Meta': {'ordering': "['squad', 'sortorder', 'person']", 'object_name': 'Staff'},
            'date_joined': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'teams_staff_date_joined'", 'null': 'True', 'to': u"orm['teams.Date']"}),
            'date_left': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'teams_staff_date_left'", 'null': 'True', 'to': u"orm['teams.Date']"}),
            'function': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'teams_staff_person'", 'to': u"orm['teams.Person']"}),
            'sortorder': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'squad': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'teams_staff_squad'", 'to': u"orm['teams.Squad']"})
        },
        u'teams.team': {
            'Meta': {'ordering': "['sortorder', 'name']", 'object_name': 'Team'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastsquad': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'lastteam_set'", 'null': 'True', 'to': u"orm['teams.Squad']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'sortorder': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        },
        u'teams.teamimage': {
            'Meta': {'object_name': 'TeamImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.Image']", 'null': 'True', 'blank': 'True'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teams.Team']"})
        },
        u'teams.transfer': {
            'Meta': {'ordering': "['person']", 'object_name': 'Transfer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'new': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'joining'", 'null': 'True', 'to': u"orm['teams.Squad']"}),
            'newextern': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'joining_ext'", 'null': 'True', 'to': u"orm['teams.ExternalTeam']"}),
            'old': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'leaving'", 'null': 'True', 'to': u"orm['teams.Squad']"}),
            'oldextern': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'leaving_ext'", 'null': 'True', 'to': u"orm['teams.ExternalTeam']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teams.Person']"})
        },
        u'teams.transferupdate': {
            'Meta': {'object_name': 'TransferUpdate'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['teams']