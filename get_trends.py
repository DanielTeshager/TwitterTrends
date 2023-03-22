import tweepy
import os
import json
import sys
import geocoder

# API Keys and Tokens
consumer_key = os.environ['API_KEY']
consumer_secret = os.environ['API_SECRET_KEY']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

# Authorization and Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def get_twitter_trends_for_location(location):
    # Available Locations
    # available_loc = api.available_trends()
    # Trends for Specific Country
    g = geocoder.osm(location) # getting object that has location's latitude and longitude
    closest_loc = api.closest_trends(g.lat, g.lng)
    trends = api.get_place_trends(closest_loc[0]['woeid'])
    
    return trends 

if __name__ == "__main__":
    loc = sys.argv[1]     # location as argument variable 
    trends = get_twitter_trends_for_location(loc)
    print(json.dumps(trends, indent=1))
