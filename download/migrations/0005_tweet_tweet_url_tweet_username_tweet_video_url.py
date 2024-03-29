# Generated by Django 4.1.4 on 2022-12-27 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0004_rename_tweets_tweet'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='tweet_url',
            field=models.URLField(default='', max_length=2100),
        ),
        migrations.AddField(
            model_name='tweet',
            name='username',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='tweet',
            name='video_url',
            field=models.URLField(default='', max_length=2100),
        ),
    ]
