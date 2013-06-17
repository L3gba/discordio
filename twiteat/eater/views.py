from models import *
from django.shortcuts import render_to_response
import tweepy


consumer_token = "ijhjcBvojStjFkLiNR2yA"
consumer_secret = "O8lXWJCrPjnJMAYEPcT3QADNl9LVL0lqAzVcMmM5ts"
key = "259638337-CS8SjeKrJJ8sDUkEGIroUA6RiRCbYjyqJxGIc8mz"
secret = "8Hxmmnl4CnmEwTDS5P1bCqIbIOHjuz6TA3ydGXGuE"

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

def main(request):
    users = User.objects.all()
    user_pack = {}
    
    for user in users:
        tweets = api.user_timeline(user.short_name)
        user_tweets = []
        for status in tweets:
            date = status.created_at
            text = status.text
            for link in status.entities['urls']:
                url = link['expanded_url']
            user_tweets.append((date, text, url))
        user_pack[user] = user_tweets
            
        
        
    #for user in users:
    #   tweets = api.user_timeline(user.short_name)
    #   tweet_dict = {user:{}}
    #   for status in tweets:
    #       tweet_dict[user] = {status.created_at:status.text}
            
    return render_to_response("list.html", dict(user_pack = user_pack))