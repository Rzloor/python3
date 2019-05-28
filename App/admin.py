from django.contrib import admin

# Register your models here.
from App import models
admin.site.register(models.User)
