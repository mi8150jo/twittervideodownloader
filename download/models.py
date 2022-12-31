from django.db import models
from datetime import datetime
import pytz
# Create your models here.

class Tweet(models.Model):
    tweet_id = models.BigIntegerField(default=0)
    tweet_url = models.URLField(max_length=2100, default="")
    video_url = models.URLField(max_length=2100, default="")
    img_url = models.URLField(max_length=2100, default="")
    date = models.DateTimeField(default=None)
    download_count = models.IntegerField(default=1)
    username = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"{self.tweet_id}"



