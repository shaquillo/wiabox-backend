from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    date = models.DateField(auto_now_add=True)
