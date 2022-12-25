from django.db import models

# Create your models here.

class Tweets(models.Model):
    tweet_url = models.URLField(max_length=2100)
    video_url = models.URLField(max_length=2100)
    img_url = models.URLField(max_length=2100)
    date = models.DateTimeField()
    download_count = models.IntegerField(default=0)
    username = models.CharField(max_length=100)



