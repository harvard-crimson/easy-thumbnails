# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Source.modified'
        db.delete_column('easy_thumbnails_source', 'modified')

        # Deleting field 'Thumbnail.modified'
        db.delete_column('easy_thumbnails_thumbnail', 'modified')


    def backwards(self, orm):
        # Adding field 'Source.modified'
        db.add_column('easy_thumbnails_source', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 9, 16, 9, 47, 8, 272761)),
                      keep_default=False)

        # Adding field 'Thumbnail.modified'
        db.add_column('easy_thumbnails_thumbnail', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 9, 16, 9, 47, 8, 272761)),
                      keep_default=False)


    models = {
        'easy_thumbnails.source': {
            'Meta': {'unique_together': "(('storage_hash', 'name'),)", 'object_name': 'Source'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'storage_hash': ('django.db.models.fields.CharField', [], {'max_length': '40', 'db_index': 'True'})
        },
        'easy_thumbnails.thumbnail': {
            'Meta': {'unique_together': "(('storage_hash', 'name', 'source'),)", 'object_name': 'Thumbnail'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'thumbnails'", 'to': "orm['easy_thumbnails.Source']"}),
            'storage_hash': ('django.db.models.fields.CharField', [], {'max_length': '40', 'db_index': 'True'})
        }
    }

    complete_apps = ['easy_thumbnails']