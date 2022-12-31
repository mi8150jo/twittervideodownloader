from django.contrib import admin
from .models import Tweet
# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "tweet_id", "download_count", "date")

admin.site.register(Tweet, TweetAdmin)