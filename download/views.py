from django.shortcuts import render, redirect
import requests
import tweepy
import logging
import re
import pprint
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "download/index.html")

def download(request):
    logging.debug("downloadリクエスト")

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

        tweet = api.get_status(tweet_id, tweet_mode='extended', include_entities=True)
        media = tweet.extended_entities.get('media', [])

        # print("-----------------------------------------")
        # print(tweet.full_text)
        # print("-----------------------------------------")
        # pprint.pprint(tweet.extended_entities)
        # print("-----------------------------------------")

        for m in media:
            pprint.pprint(m)
            if m['type'] == 'video':

                video_urls = []

                for variant in m['video_info']['variants']:
                    if variant['content_type'] == 'video/mp4':
                        video_urls.append(variant['url'])
                        print("代入しました")
                        
                for url in video_urls:
                    print(url)
                    
                video_url = video_urls[0]

        #urlがあればダウンロードなければエラーメッセージを返す
        try:
            if video_url:

                #video = requests.get(video_url)
                # with open('video.mp4', 'wb') as f:
                #     f.write(video.content)

                return preview(request, video_url)
                
                # return render(request, "download/preview.html",
                #     context={
                #         "url":video_url,
                #     }
                # )
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

def preview(request, video_url):
    return render(request, "download/preview.html",
        context={
            "url":video_url,
        }
    )