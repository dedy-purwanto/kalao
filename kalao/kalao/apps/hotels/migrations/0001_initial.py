# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Hotel'
        db.create_table('hotels_hotel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(related_name='hotels', to=orm['references.Country'])),
            ('child_with_bed_rate', self.gf('django.db.models.fields.DecimalField')(max_digits=30, decimal_places=2)),
            ('child_without_bed_rate', self.gf('django.db.models.fields.DecimalField')(max_digits=30, decimal_places=2)),
            ('breakfast_rate', self.gf('django.db.models.fields.DecimalField')(max_digits=30, decimal_places=2)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='hotel_created', to=orm['auth.User'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='hotel_modified', to=orm['auth.User'])),
        ))
        db.send_create_signal('hotels', ['Hotel'])

        # Adding unique constraint on 'Hotel', fields ['name', 'country']
        db.create_unique('hotels_hotel', ['name', 'country_id'])

        # Adding model 'Rate'
        db.create_table('hotels_rate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hotel', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rooms', to=orm['hotels.Hotel'])),
            ('room', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rates', to=orm['references.Room'])),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_from_day', self.gf('django.db.models.fields.IntegerField')()),
            ('date_from_month', self.gf('django.db.models.fields.IntegerField')()),
            ('date_to_day', self.gf('django.db.models.fields.IntegerField')()),
            ('date_to_month', self.gf('django.db.models.fields.IntegerField')()),
            ('rate', self.gf('django.db.models.fields.DecimalField')(max_digits=30, decimal_places=2)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rate_created', to=orm['auth.User'])),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rate_modified', to=orm['auth.User'])),
        ))
        db.send_create_signal('hotels', ['Rate'])

        # Adding unique constraint on 'Rate', fields ['hotel', 'room', 'date_from_day', 'date_from_month', 'date_to_day', 'date_to_month']
        db.create_unique('hotels_rate', ['hotel_id', 'room_id', 'date_from_day', 'date_from_month', 'date_to_day', 'date_to_month'])


    def backwards(self, orm):
        # Removing unique constraint on 'Rate', fields ['hotel', 'room', 'date_from_day', 'date_from_month', 'date_to_day', 'date_to_month']
        db.delete_unique('hotels_rate', ['hotel_id', 'room_id', 'date_from_day', 'date_from_month', 'date_to_day', 'date_to_month'])

        # Removing unique constraint on 'Hotel', fields ['name', 'country']
        db.delete_unique('hotels_hotel', ['name', 'country_id'])

        # Deleting model 'Hotel'
        db.delete_table('hotels_hotel')

        # Deleting model 'Rate'
        db.delete_table('hotels_rate')


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
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'breakfast_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '30', 'decimal_places': '2'}),
            'child_with_bed_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '30', 'decimal_places': '2'}),
            'child_without_bed_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '30', 'decimal_places': '2'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hotels'", 'to': "orm['references.Country']"}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hotel_created'", 'to': "orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hotel_modified'", 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'hotels.rate': {
            'Meta': {'unique_together': "(('hotel', 'room', 'date_from_day', 'date_from_month', 'date_to_day', 'date_to_month'),)", 'object_name': 'Rate'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rate_created'", 'to': "orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_from_day': ('django.db.models.fields.IntegerField', [], {}),
            'date_from_month': ('django.db.models.fields.IntegerField', [], {}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_to_day': ('django.db.models.fields.IntegerField', [], {}),
            'date_to_month': ('django.db.models.fields.IntegerField', [], {}),
            'hotel': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rooms'", 'to': "orm['hotels.Hotel']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rate_modified'", 'to': "orm['auth.User']"}),
            'rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '30', 'decimal_places': '2'}),
            'room': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rates'", 'to': "orm['references.Room']"})
        },
        'references.country': {
            'Meta': {'object_name': 'Country'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'country_created'", 'to': "orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'country_modified'", 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'references.room': {
            'Meta': {'object_name': 'Room'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'room_created'", 'to': "orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'room_modified'", 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['hotels']