# Generated by Django 4.1.4 on 2022-12-27 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0006_tweet_date_tweet_download_count_tweet_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='date',
            field=models.DateTimeField(default=None),
        ),
    ]
