from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.PaymentSystem)
admin.site.register(models.Donator)
admin.site.register(models.Transaction)
