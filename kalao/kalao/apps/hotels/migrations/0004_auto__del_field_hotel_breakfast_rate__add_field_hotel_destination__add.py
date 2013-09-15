# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Hotel.breakfast_rate'
        db.delete_column('hotels_hotel', 'breakfast_rate')

        # Adding field 'Hotel.destination'
        db.add_column('hotels_hotel', 'destination',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='hotels', null=True, to=orm['references.CountryDestination']),
                      keep_default=False)

        # Adding field 'Hotel.stars'
        db.add_column('hotels_hotel', 'stars',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Hotel.adult_breakfast_rate'
        db.add_column('hotels_hotel', 'adult_breakfast_rate',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=30, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Hotel.child_breakfast_rate'
        db.add_column('hotels_hotel', 'child_breakfast_rate',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=30, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Rate.date_from_year'
        db.add_column('hotels_rate', 'date_from_year',
                      self.gf('django.db.models.fields.IntegerField')(default=2013),
                      keep_default=False)

        # Adding field 'Rate.date_to_year'
        db.add_column('hotels_rate', 'date_to_year',
                      self.gf('django.db.models.fields.IntegerField')(default=2013),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Hotel.breakfast_rate'
        raise RuntimeError("Cannot reverse this migration. 'Hotel.breakfast_rate' and its values cannot be restored.")
        # Deleting field 'Hotel.destination'
        db.delete_column('hotels_hotel', 'destination_id')

        # Deleting field 'Hotel.stars'
        db.delete_column('hotels_hotel', 'stars')

        # Deleting field 'Hotel.adult_breakfast_rate'
        db.delete_column('hotels_hotel', 'adult_breakfast_rate')

        # Deleting field 'Hotel.child_breakfast_rate'
        db.delete_column('hotels_hotel', 'child_breakfast_rate')

        # Deleting field 'Rate.date_from_year'
        db.delete_column('hotels_rate', 'date_from_year')

        # Deleting field 'Rate.date_to_year'
        db.delete_column('hotels_rate', 'date_to_year')


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
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'hotels.hotel': {
            'Meta': {'unique_together': "(('name', 'country'),)", 'object_name': 'Hotel'},
            'adult_breakfast_rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '30', 'decimal_places': '2', 'blank': 'True'}),
            'adult_extra_bed_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '30', 'decimal_places': '2'}),
            'child_breakfast_rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '30', 'decimal_places': '2', 'blank': 'True'}),
            'child_with_bed_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '30', 'decimal_places': '2'}),
            'child_without_bed_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '30', 'decimal_places': '2'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hotels'", 'to': "orm['references.Country']"}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hotel_created'", 'to': "orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'destination': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'hotels'", 'null': 'True', 'to': "orm['references.CountryDestination']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hotel_modified'", 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'stars': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'hotels.rate': {
            'Meta': {'unique_together': "(('hotel', 'room', 'date_from_day', 'date_from_month', 'date_to_day', 'date_to_month'),)", 'object_name': 'Rate'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rate_created'", 'to': "orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_from_day': ('django.db.models.fields.IntegerField', [], {}),
            'date_from_month': ('django.db.models.fields.IntegerField', [], {}),
            'date_from_year': ('django.db.models.fields.IntegerField', [], {'default': '2013'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_to_day': ('django.db.models.fields.IntegerField', [], {}),
            'date_to_month': ('django.db.models.fields.IntegerField', [], {}),
            'date_to_year': ('django.db.models.fields.IntegerField', [], {'default': '2013'}),
            'hotel': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rates'", 'to': "orm['hotels.Hotel']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rate_modified'", 'to': "orm['auth.User']"}),
            'rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '30', 'decimal_places': '2'}),
            'room': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rates'", 'to': "orm['references.Room']"})
        },
        'references.country': {
            'Meta': {'object_name': 'Country'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'country_created'", 'to': "orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'country_modified'", 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'references.countrydestination': {
            'Meta': {'object_name': 'CountryDestination'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'destinations'", 'to': "orm['references.Country']"}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'country_destination_created'", 'to': "orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'country_destination_modified'", 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'references.room': {
            'Meta': {'object_name': 'Room'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'room_created'", 'to': "orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'room_modified'", 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['hotels']