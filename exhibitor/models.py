# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Exhibitors(models.Model):
    eid = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    company = models.CharField(max_length=200)
    section = models.CharField(max_length=200)
    contact = models.CharField(max_length=100)
    tel = models.CharField(max_length=30)
    position = models.CharField(max_length=200)
    nation = models.CharField(max_length=200)
    email = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    intro = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'exhibitors'
