# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'join.friend'
        db.add_column(u'joins_join', 'friend',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='referral', null=True, to=orm['joins.join']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'join.friend'
        db.delete_column(u'joins_join', 'friend_id')


    models = {
        u'joins.join': {
            'Meta': {'unique_together': "(('email', 'ref_id'),)", 'object_name': 'join'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'friend': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'referral'", 'null': 'True', 'to': u"orm['joins.join']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'default': "'ABC'", 'max_length': '120'}),
            'ref_id': ('django.db.models.fields.CharField', [], {'default': "'PQR'", 'max_length': '120'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'update': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['joins']