import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = 'D5swSkP3WuOA5lne0SJ1Bs32B'
consumer_secret = 'GDzkrkE1uiyIvxMueyrE1TNUY8Qfpkv2iY7fj6BmfAV5QDFZdT'
access_token = '744521717972877312-Bu47q61qP38f72cIWmTqwSPj6DTXZp0'
access_token_secret = '2vpaA7PxT8O9jMH4U3Ths6JtUaPjCBCYevnPaWoSOZnay'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('ua.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#OPPOF7",count=100,lang="en",since="2018-03-25").items():
    print (tweet.text)
    csvWriter.writerow([tweet.text.encode('utf-8')])
