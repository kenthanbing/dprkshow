# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Articles(models.Model):
    aid = models.AutoField(primary_key=True)
    snap = models.CharField(max_length=300, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    abanner = models.CharField(max_length=300, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'articles'
