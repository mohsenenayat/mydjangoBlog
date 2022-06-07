from datetime import date
from email.policy import default
from turtle import title
from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(default='default.jpg',blank=True)

    def __str__(self):
        return self.title

    def kholase_matn(self):
        return self.body[:50] + ' ...'