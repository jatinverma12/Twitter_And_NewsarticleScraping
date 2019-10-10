import tweepy
import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
consumer_key = 'MNi7ljDfSVjlBJ0cFaPqNJRE3'
consumer_secret = '52T044FJHFCEluR41axGEkIlNDHbLTDm1wivzvFcPEjJfFBM36K'
access_token = '1168161739252232193-dXDzMqEcWZVeeqJ6VYoFT7vi9POcp1'
access_token_secret = 'cPfEegp6u12HbdD5TvWA3iJf8cn5v1U9sffwYAllUgCec'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)  
api = tweepy.API(auth)

def get_tweets(username): 
        number_of_tweets=200
        tweets = api.user_timeline(screen_name=username, count=number_of_tweets) 
        tmp=[]
        i=1
        tweets_for_json = {tweet.text for tweet in tweets}
        tmp.append("TWEETS")
        for j in tweets_for_json: 
            tmp.append(str(i)+") "+j)
            i=i+1
        with open('TOI.json', 'w') as f:
            json.dump(tmp, f, indent=2)

class TweetListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)
def get_user_info(username):
    data=[]
    twitterStream = Stream(auth,TweetListener())
    user = api.get_user('timesofindia')
    print ("User ID: ",user.screen_name)
    print ("Description: ",user.description)
    print ("No of Followers:",user.followers_count)
    print ("No of Tweets :",user.statuses_count)
    print ("Website Link :",user.url)
    data.append("User ID: "+user.screen_name)
    data.append("Description: "+user.description)
    data.append("No of Followers:"+str(user.followers_count))
    data.append("No of Tweets :"+str(user.statuses_count))
    data.append("Website Link :"+user.url)
    with open('TOI2.json', 'w') as f:
                json.dump(data, f, indent=2)

def main():
    ch=int(input("1. For user info\n2. For user Timeline\nEnter Your Choice : "))
    if ch==1:
        get_user_info("DainikBhaskar") 
    elif ch==2:
        get_tweets("DainikBhaskar") 
    else:
        print("Invalid Input")
 
# main CALLING 
if __name__ == '__main__': 
    main()
    