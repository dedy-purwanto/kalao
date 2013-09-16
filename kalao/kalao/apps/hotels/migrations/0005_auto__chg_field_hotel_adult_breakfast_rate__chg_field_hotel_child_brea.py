# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Hotel.adult_breakfast_rate'
        db.alter_column(u'hotels_hotel', 'adult_breakfast_rate', self.gf('django.db.models.fields.DecimalField')(default=1, max_digits=30, decimal_places=2))

        # Changing field 'Hotel.child_breakfast_rate'
        db.alter_column(u'hotels_hotel', 'child_breakfast_rate', self.gf('django.db.models.fields.DecimalField')(default=1, max_digits=30, decimal_places=2))

    def backwards(self, orm):

        # Changing field 'Hotel.adult_breakfast_rate'
        db.alter_column(u'hotels_hotel', 'adult_breakfast_rate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=30, decimal_places=2))

        # Changing field 'Hotel.child_breakfast_rate'
        db.alter_column(u'hotels_hotel', 'child_breakfast_rate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=30, decimal_places=2))

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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'hotels.hotel': {
            'Meta': {'unique_together': "(('name', 'country'),)", 'object_name': 'Hotel'},
            'adult_breakfast_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '30', 'decimal_places': '2'}),
            'adult_extra_bed_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '30', 'decimal_places': '2'}),
            'child_breakfast_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '30', 'decimal_places': '2'}),
            'child_with_bed_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '30', 'decimal_places': '2'}),
            'child_without_bed_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '30', 'decimal_places': '2'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hotels'", 'to': u"orm['references.Country']"}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hotel_created'", 'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'destination': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'hotels'", 'null': 'True', 'to': u"orm['references.CountryDestination']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hotel_modified'", 'to': u"orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'stars': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'hotels.rate': {
            'Meta': {'unique_together': "(('hotel', 'room', 'date_from_day', 'date_from_month', 'date_to_day', 'date_to_month'),)", 'object_name': 'Rate'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rate_created'", 'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_from_day': ('django.db.models.fields.IntegerField', [], {}),
            'date_from_month': ('django.db.models.fields.IntegerField', [], {}),
            'date_from_year': ('django.db.models.fields.IntegerField', [], {'default': '2013'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_to_day': ('django.db.models.fields.IntegerField', [], {}),
            'date_to_month': ('django.db.models.fields.IntegerField', [], {}),
            'date_to_year': ('django.db.models.fields.IntegerField', [], {'default': '2013'}),
            'hotel': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rates'", 'to': u"orm['hotels.Hotel']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rate_modified'", 'to': u"orm['auth.User']"}),
            'rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '30', 'decimal_places': '2'}),
            'room': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rates'", 'to': u"orm['references.Room']"})
        },
        u'references.country': {
            'Meta': {'object_name': 'Country'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'country_created'", 'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'country_modified'", 'to': u"orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'references.countrydestination': {
            'Meta': {'object_name': 'CountryDestination'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'destinations'", 'to': u"orm['references.Country']"}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'country_destination_created'", 'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'country_destination_modified'", 'to': u"orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'references.room': {
            'Meta': {'object_name': 'Room'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'room_created'", 'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'room_modified'", 'to': u"orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['hotels']