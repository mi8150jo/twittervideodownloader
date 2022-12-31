from django.shortcuts import render, redirect
import tweepy
import logging
import re
import pprint
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Tweet
from datetime import datetime
import pytz

# Create your views here.
def index(request):
    return render(request, "download/index.html")

def download(request):
    print("downloadリクエスト")

    if request.method == "POST":
        print("urlを受け取りました")

        #key設定
        consumer_key        = 'g1pvtJMaOaWP3O2FacNwnffmo'
        consumer_secret     = 'AJCZ08PxQhYOYctWalPrgfdEi7vwgvypvv4GfXKWqgYPw9O8HB'
        access_token        = '982246350271033344-wSqRQMOaUJrXBBK8L1wgjiNtLHz7m2D'
        access_token_secret = 'lNnLC78KvMnE3NWHznlL7C0iG9y4LOvHq6PR8ULTZdgel' 

        #認証
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        # 動画URLを取得
        tweet_url = request.POST.get("url")
        # URLからツイートIDを抽出する正規表現
        pattern = r"https://twitter\.com/[^/]+/status/(\d+)"

        #urlからtweetIDを抽出
        match = re.search(pattern, tweet_url)
        if match:
            tweet_id = match.group(1)
            print("This is id : " + tweet_id)

        tweet = api.get_status(tweet_id, tweet_mode='extended', include_entities=True)
        media = tweet.extended_entities.get('media', [])

        username = tweet.user.name

        # print("-----------------------------------------")
        # pprint.pprint(tweet, width=4)
        # print("-----------------------------------------")
        # pprint.pprint(tweet.extended_entities)
        # print("-----------------------------------------")

        for m in media:
            print("This is Username : " + username)

            url = m['url']
            print("This is URL : " + url)

            media_url_https = m['media_url_https']
            print("This is media_url_https : " + media_url_https)

            if m['type'] == 'video':
                #dictからvideo_urlの取得
                for variant in m['video_info']['variants']:
                    if variant['content_type'] == 'video/mp4':
                        # info1 = "video_url"
                        # info2 = "bitrate"
                        video_url = variant['url']
                        print(video_url)
                        # bitrate = variant['bitrate']
                        # video_urls = {info1:video_url, info2:bitrate}
                        # print(video_urls)

                # for url in video_urls:
                #     print(url)
                
                # video_url = video_urls
                
        

        #urlがあればダウンロードなければエラーメッセージを返す
        try:
            if video_url:
                print("video_urlがあります")
                records = Tweet.objects.all()
                #データベースに既に同じtweet_idがあればカウントを増やす、なければツイート情報を新しく保存する
                for record in records:
                    print(record)
                    if record.tweet_id == int(tweet_id):
                        print("データベースに重複を発見")
                        record.download_count += 1
                        record.save()
                        return HttpResponseRedirect(reverse("preview", kwargs={"id": record.id}))
                        
                print("新規保存します")
                t = Tweet(
                    tweet_id = tweet_id,
                    tweet_url = tweet_url, 
                    video_url = video_url, 
                    img_url = media_url_https,
                    date = datetime.now(pytz.timezone('Asia/Tokyo')),
                    username = username,
                )
                t.save()

                return HttpResponseRedirect(reverse("preview", kwargs={"id": t.id}))

        except(UnboundLocalError):
            return render(request, "download/download.html",
                context={
                    "message":"無効なurlです。",
                }
            )
        except:
            return render(request, "download/download.html",
                context={
                    "message":"無効なurlです。",
                }
            )

    return render(request, "download/download.html",
        context={
        }
    )

def preview(request, id):
    print("previewリクエスト")
    obj = Tweet.objects.get(pk=id)
    tweet_id = obj.tweet_id
    video_url = obj.video_url
    img_url = obj.img_url
    date = obj.date
    download_count = obj.download_count
    username = obj.username

    return render(request, "download/preview.html",
        context={
            "tweet_id":tweet_id,
            "url":video_url,
            "img_url":img_url,
            "date":date,
            "download_count":download_count,
            "username":username,
      
        }
    )