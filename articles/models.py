from djangonautic.settings import TIME_ZONE
from django.db import models
from django.db.models.fields import CharField


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # Add thumbnail later
    # add in author later

    def __str__(self):
        return self.title
    
    def snippet(self):
        return f"{self.body[:100]}..."