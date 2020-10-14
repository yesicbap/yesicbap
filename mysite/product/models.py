from django.db import models

# Create your models here.
class Product(models.Model):
    """Model definition for Product."""

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    thumbnail = models.ImageField(upload_to="product_image")
    developer = models.CharField(max_length=300)
    technology_used = models.CharField(max_length=1000)
    language = models.CharField(max_length=300)


