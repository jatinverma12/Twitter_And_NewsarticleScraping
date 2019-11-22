import tweepy
import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
consumer_key = "0bEh2WjzKqYh4hIvQS6VwqIjR" 
consumer_secret = "BsOx7vXuDJ0m0zczSqfw4xftwvDOkbKrRTdReF9pTxpAbGW2Ms"
access_token = "1169646755190693888-2EbkmiYHfc4D6g9pubqlGH1u4PWoaE"
access_token_secret = "2lCeBuYg8MNxCT85Bc5queSytSANJ6l62HJNpo5SB9J7D"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)  
api = tweepy.API(auth)
dic={}

class TweetListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)

def get_tweets(username): 
    tweets_no=200
    tweets = api.user_timeline(screen_name=username, count=tweets_no, tweet_mode='extended') 
    result=[]
    i=1
    for tweet in tweets:
        dic={
            
            "Tweet ID":tweet.id,
            "Tweet Text":tweet.full_text,
            "Tweet Date&Time":str(tweet.created_at),
            "Likes":tweet.favorite_count,
            "Retweet_count":tweet.retweet_count,
            "Users_mentions":list(map(lambda x: {"name":x['screen_name'],
            "User_id":x['id_str']},tweet.entities['user_mentions'])),
            "Hashtags":list(map(lambda x: x['text'],tweet.entities['hashtags']))
            
            }
        result.append(dic)
        i+=1
    return result
    print (dic)

def get_user_info(username):
    twitterStream = Stream(auth,TweetListener())
    user = api.get_user(username)
    result=get_tweets(username)
    data={
        
        "Profile Name":user.name,
        "Twitter ID":user.screen_name,
        "Bio":user.description,
        "Location":user.location,
        "URL":user.url,
        "Joined":str(user.created_at),
        "Following":str(user.friends_count),
        "Followers":str(user.followers_count),
        "Profile Image":user.profile_image_url_https,
        "Tweets":result
        
        }
    print ("User ID: ",user.screen_name)
    print ("Description: ",user.description)
    print ("No of Followers:",user.followers_count)
    print ("No of Tweets :",user.statuses_count)
    print ("Website Link :",user.url)
    with open('dainikTwitter.json', 'w') as f:
                json.dump(data, f, indent=2)

get_user_info('dainikbhaskar')