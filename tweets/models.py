from django.db import models


class Tweet(models.Model):
    content = models.TextField(null=True, blank=True)
    count = models.IntegerField(null=True, blank=True, default=0)
    # image = models.ImageField(upload_to='images/', null=True, blank=True)
