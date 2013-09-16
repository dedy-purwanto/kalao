# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'PackageHotel.number_of_bonus_nights'
        db.alter_column(u'packages_packagehotel', 'number_of_bonus_nights', self.gf('django.db.models.fields.IntegerField')(default=1))

        # Changing field 'PackageHotel.number_of_nights'
        db.alter_column(u'packages_packagehotel', 'number_of_nights', self.gf('django.db.models.fields.IntegerField')(default=1))

    def backwards(self, orm):

        # Changing field 'PackageHotel.number_of_bonus_nights'
        db.alter_column(u'packages_packagehotel', 'number_of_bonus_nights', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'PackageHotel.number_of_nights'
        db.alter_column(u'packages_packagehotel', 'number_of_nights', self.gf('django.db.models.fields.IntegerField')(null=True))

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
        u'packages.package': {
            'Meta': {'object_name': 'Package'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'package_created'", 'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'markup_amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '30', 'decimal_places': '2'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'package_modified'", 'to': u"orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'packages.packagebatch': {
            'Meta': {'ordering': "('id',)", 'object_name': 'PackageBatch'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'batches_created'", 'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_from': ('django.db.models.fields.DateField', [], {}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_to': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'batches_modified'", 'to': u"orm['auth.User']"}),
            'package': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'batches'", 'to': u"orm['packages.Package']"})
        },
        u'packages.packagehotel': {
            'Meta': {'object_name': 'PackageHotel'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'package_hotel_created'", 'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'hotel': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'package_hotels'", 'to': u"orm['hotels.Hotel']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'package_hotel_modified'", 'to': u"orm['auth.User']"}),
            'number_of_bonus_nights': ('django.db.models.fields.IntegerField', [], {}),
            'number_of_nights': ('django.db.models.fields.IntegerField', [], {}),
            'package': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'package_hotels'", 'to': u"orm['packages.Package']"}),
            'room': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'package_hotels'", 'to': u"orm['references.Room']"}),
            'transfer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['references.Transfer']", 'null': 'True', 'blank': 'True'})
        },
        u'packages.remark': {
            'Meta': {'object_name': 'Remark'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'remarks_created'", 'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'remarks_modified'", 'to': u"orm['auth.User']"}),
            'package': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'remarks'", 'to': u"orm['packages.Package']"}),
            'remarks': ('django.db.models.fields.CharField', [], {'max_length': '2048'})
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
        },
        u'references.transfer': {
            'Meta': {'object_name': 'Transfer'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'transfer_created'", 'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'destination': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['references.CountryDestination']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'transfer_modified'", 'to': u"orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '30', 'decimal_places': '2'})
        }
    }

    complete_apps = ['packages']