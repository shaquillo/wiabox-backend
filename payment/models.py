from django.db import models

# Create your models here.

class Donator(models.Model):
    COUNTRY = (('CMR', 'CAMEROON'),
               ('FR', 'FRANCE')
               )
    name = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    country = models.CharField(max_length=30, choices=COUNTRY)


class PaymentSystem(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)


class Transaction(models.Model):
    solde = models.DecimalField(max_digits=11, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    payment_system = models.OneToOneField(PaymentSystem, on_delete=models.DO_NOTHING)
    donator = models.OneToOneField(Donator, on_delete=models.SET_NULL, null=True)

