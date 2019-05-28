from django.db import models

class User(models.Model):
    id = models.BigIntegerField
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=32)

    def __unicode__(self):
        return self.username
    class Meta:
        db_table='dj_user'