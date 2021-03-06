# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Location.gps'
        db.delete_column(u'public_location', 'gps')

        # Adding field 'Location.gpsLat'
        db.add_column(u'public_location', 'gpsLat',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Location.gpsLng'
        db.add_column(u'public_location', 'gpsLng',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Location.reliableGPS'
        db.add_column(u'public_location', 'reliableGPS',
                      self.gf('django.db.models.fields.BooleanField')(default='false'),
                      keep_default=False)


        # Changing field 'Location.street'
        db.alter_column(u'public_location', 'street', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Location.gps'
        raise RuntimeError("Cannot reverse this migration. 'Location.gps' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Location.gps'
        db.add_column(u'public_location', 'gps',
                      self.gf('django.db.models.fields.CharField')(max_length=200),
                      keep_default=False)

        # Deleting field 'Location.gpsLat'
        db.delete_column(u'public_location', 'gpsLat')

        # Deleting field 'Location.gpsLng'
        db.delete_column(u'public_location', 'gpsLng')

        # Deleting field 'Location.reliableGPS'
        db.delete_column(u'public_location', 'reliableGPS')


        # User chose to not deal with backwards NULL issues for 'Location.street'
        raise RuntimeError("Cannot reverse this migration. 'Location.street' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Location.street'
        db.alter_column(u'public_location', 'street', self.gf('django.db.models.fields.CharField')(max_length=200))

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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'public.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'gps': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'public.comment': {
            'Meta': {'object_name': 'Comment'},
            'commentDate': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'commentText': ('django.db.models.fields.CharField', [], {'max_length': '900'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locationPostID': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['public.Location']"}),
            'locationRating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'public.location': {
            'Meta': {'object_name': 'Location'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'datecreated': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'gpsLat': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'gpsLng': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locationName': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'photos': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'reliableGPS': ('django.db.models.fields.BooleanField', [], {}),
            'sponsored': ('django.db.models.fields.BooleanField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'voteCount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['public']