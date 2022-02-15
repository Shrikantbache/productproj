from django.db import models

# Create your models here.
class Productss(models.Model):
    name = models.CharField(max_length = 70)
    weight = models.IntegerField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        app_label = 'products'
        

