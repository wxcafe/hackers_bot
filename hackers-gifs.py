#!/usr/bin/env python3

import os, random
from mastodon import Mastodon
import tweepy

tw_consumer_key = ""
tw_consumer_secret = ""
tw_access_token = ""
tw_access_token_secret = ""

mastodon_url = 'https://botsin.space'

tw_auth = tweepy.OAuthHandler(tw_consumer_key,tw_consumer_secret)
tw_auth.set_access_token(tw_access_token, tw_access_token_secret)
twitter = tweepy.API(tw_auth)

masto = Mastodon(client_id='app_tokens', access_token='log_in', api_base_url=mastodon_url)

gif_file = "./gifs/" + random.choice(os.listdir("./gifs/"))

gif = masto.media_post(gif_file)

try:
    masto.status_post(status="﻿  ", \
            media_ids=[gif], \
            visibility='unlisted',
            sensitive=None)
except:
    print("Failed to post to mastodon")

try:
    twitter.update_with_media(gif_file)
except:
    print("Failed to post to twitter")
