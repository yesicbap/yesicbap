from django.db import models

# Create your models here.
class Blog(models.Model):
    """Model definition for Blog."""

    title = models.CharField(max_length=200)
    description = models.TextField(max_length=50000)
    image = models.ImageField(upload_to="blog_image")
    clap = models.IntegerField(default=0)
    auther = models.CharField(max_length=100)
    blog_refrences = models.TextField(max_length=2000)

    



