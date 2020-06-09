import requests
import datetime
import random
import tweepy
import time

dt = datetime.datetime.today()

response = requests.get(f"https://byabbe.se/on-this-day/{dt.month}/{dt.day}/events.json")
data = response.json()
events = data['events']
print(events)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
for event in random.sample(list(events), 5):
    message = f"On this day in {event['year']}: {event['description']}\n#History #OnThisDay"
    print(message)
    api.update_status(status=message)
    time.sleep(7200)
