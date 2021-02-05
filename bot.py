import tweepy
from keys import api_key, api_secret_key, access_token, access_token_secret
import requests
import json 
import time

url = "https://icanhazdadjoke.com/"

def auth():
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

def get_data():
    headers = {
        'Accept': 'application/json'
    }
    data = requests.get(url, headers=headers)
    data = json.loads(data.content)
    return data['joke']

def new_tweet():
    # id = read_id()
    api = auth()
    data = get_data()
    
    print(data)
    b = api.update_status(data)
    print("SUCCESS")

while True:
    new_tweet()
    time.sleep(60*60)
    