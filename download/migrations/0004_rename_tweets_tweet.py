# Generated by Django 4.1.4 on 2022-12-27 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0003_remove_tweets_date_remove_tweets_download_count_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tweets',
            new_name='Tweet',
        ),
    ]