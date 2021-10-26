from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Tweet(models.Model):
    contentTweet = models.TextField()
    userTweet = models.CharField(max_length=255)

    created_by = models.ForeignKey(User, related_name='tweets', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)