from django.db import models

# Create your models here.

class Users(models.Model):
    login = models.CharField(primary_key=True, max_length=255)
    password = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
