from django.shortcuts import render
import requests
import tweepy
import logging

# Create your views here.
def index(request):
    return render(request, "download/index.html")

def download(request):
    if request.method == "POST":
        logging.debug("urlを受け取りました")
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
        tweet = api.get_status(tweet_url)
        media = tweet.entities.get('media', [])
        for m in media:
            if m['type'] == 'video':
                video_url = m['video_info']['variants'][0]['url']
                logging.debug(video_url)

        #urlがあればダウンロードなければエラーメッセージを返す
        if video_url:
            video = requests.get(video_url)
            with open('video.mp4', 'wb') as f:
                f.write(video.content)
            video_url = None
        else:
            video_url = None
            return render(request, "download/download.html",
                context={
                    "message":"無効なurlです。",
                }
            )

    return render(request, "download/download.html",
        context={
        }
    )
