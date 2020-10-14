from django.db import models

# Create your models here.

class Contact_us(models.Model):
    """Model definition for Contact_us."""

    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=300)

    class Meta:
        """Meta definition for Contact_us."""

        verbose_name = 'Contact_us'
        verbose_name_plural = 'Contact_uss'

    def __str__(self):
        """Unicode representation of Contact_us."""
        pass




