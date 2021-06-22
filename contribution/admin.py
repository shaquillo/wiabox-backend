from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Promotion)
admin.site.register(models.Contributor)
admin.site.register(models.Contribution)
