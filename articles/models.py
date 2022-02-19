from djangonautic.settings import TIME_ZONE
from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def snippet(self):
        return f"{self.body[:50]}..."