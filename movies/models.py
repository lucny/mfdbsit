from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns


class Film(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    titul = models.CharField(max_length=200)
    rok = models.IntegerField()

    def __str__(self):
        """String for representing the Model object."""
        return self.titul


