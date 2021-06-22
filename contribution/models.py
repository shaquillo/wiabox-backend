from django.db import models

# Create your models here.

class Promotion(models.Model):
    promotion = models.CharField(max_length=10)


class Contributor(models.Model):
    name = models.CharField(max_length=50)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)


class Contribution(models.Model):
    theme = models.CharField(max_length=20)
    report = models.FileField(upload_to='contribution', null=True, blank=True)
    date = models.DateField()
    contributors = models.ForeignKey(Contributor, on_delete=models.SET_NULL, null=True)
