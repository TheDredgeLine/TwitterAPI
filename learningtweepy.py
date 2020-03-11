import tweepy
import json
import csv
from datetime import date
from datetime import datetime
import time

def limit_handled(cursor, list_name):
    while True:
        try:
            yield cursor.next()
    # Catch Twitter API rate limit exception and wait for 15 minutes
        except tweepy.RateLimitError:
            print("\nData points in list = {}".format(len(list_name)))
            print('Hit Twitter API rate limit.')
            for i in range(3, 0, -1):
                print("Wait for {} mins.".format(i * 5))
                time.sleep(5 * 60)
    # Catch any other Twitter API exceptions
        except tweepy.error.TweepError:
            print('\nCaught TweepError exception')


# Connect to Twitter API using the secrets
auth = tweepy.OAuthHandler("ogtkSiN1qhgDxPAvOxdJBsnvt", "EwkM8Fw7E8bX0mZ6oeUjDM0cFMjR6NViJtYCAqdoXZ9GqKle8J")
auth.set_access_token("868473326-HN6XJ7c0RuVcnQMoABljQaPNTVnrUyVnnh5GS8Gf", "CmUejlmontXmjhAFwocSukBinH3lhuQzxwMGIDjqECL05")
api = tweepy.API(auth)

totaltime = time.process_time()
user = api.get_user('c9mang0')

myName = [user.screen_name]


myFollowers = []
for page in tweepy.Cursor(api.followers, screen_name='c9mang0', wait_on_rate_limit=True,count=200).pages():
    try:
        myFollowers.extend(page)
    except tweepy.TweepError as e:
        print("Going to sleep:", e)
        time.sleep(60)



filename = "testing.csv"

test = []
for item in myFollowers:
    test.append(item.screen_name.encode('utf8'))

with open(filename, 'w') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow([user.screen_name])
    #for friend in user.friends():
    csvwriter.writerow(test)
    # csvwriter.writerow(user.followers_count)

print(totaltime)


