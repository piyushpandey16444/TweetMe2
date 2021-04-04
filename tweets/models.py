from django.db import models


class Tweet(models.Model):
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
