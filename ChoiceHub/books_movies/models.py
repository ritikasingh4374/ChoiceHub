# books/models.py

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    themes = models.CharField(max_length=200, blank=True)
    character_vs_plot = models.CharField(max_length=50, choices=[('Character', 'Character-driven'), ('Plot', 'Plot-driven')], blank=True)
    writing_style = models.CharField(max_length=100, blank=True)
    setting = models.CharField(max_length=200, blank=True)
    mood = models.CharField(max_length=100, blank=True)
    api_source = models.CharField(max_length=100, default="Unknown")  # To track the source API
    cover_image = models.URLField(max_length=200, blank=True)  # URL for the book cover image
    description = models.TextField(blank=True)  # Full description of the book
    reviews = models.TextField(blank=True)  # Space for reviews or notes

    def __str__(self):
        return self.title
