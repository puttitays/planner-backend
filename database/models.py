from django.db import models

# Create your models here.

class Quote(models.Model):
    Quote=models.CharField(max_length=200)
    Author=models.CharField(max_length=200)

    def __str__(self):
        return self.Quote
