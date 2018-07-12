from keys import consumer_key,consumer_secret,access_token,access_secret,key_list
import re
import tweepy
from tweepy import OAuthHandler
import time
from time import sleep
import textblob
from textblob import TextBlob
from collections import Counter
import nltk
from nltk.corpus import *
from paralleldots import set_api_key,get_api_key
from paralleldots import *


oauth=tweepy.OAuthHandler(consumer_key,consumer_secret)
oauth.set_access_token(access_token,access_secret)
api=tweepy.API(oauth)



#retrive tweets
def retrieve_tweets():
    stuff = api.user_timeline(screen_name='ippatel', count=100, include_rts=True)
    for status in stuff:
        print("Tweets are:- ", status.text)



#user followers count
def followers_count():
    user=api.get_user('@vivek_shivam007')
    print(user.screen_name)
    print("Followers are:- ",user.followers_count)


def status_update():
    text=input("Update your status:-")
    status_update=api.update_status(status=text)
    print(status_update)


def loc_of_tweets():
    tweets=input("Enter name who's location you want to search:")
    tweettt=api.search(tweets)
    for search_results in tweettt:
        print("Location:-",search_results.user.location)
        print("Time_Zone:-",search_results.user.time_zone)
        print("Language",search_results.user.lang)


#to analyse the top usage of the tweet
def Top_used_words():
    nltk.download('stopwords')
    text='my name is Akshita sharma and i am a student of btech cse and i am happy'
    stop_words = set(stopwords.words('english'))
    print(stop_words)
    list1=text.split()
    print(list1)
    for word in list1:
        if word not in stop_words:
            print(word)
    count = Counter(list1).most_common(3)
    print("Top Used Words:- ",count)


#sentiment analyses
def sentiment_analysis():
    set_api_key(key_list)
    get_api_key()

    user=api.get_user('vivek_shivam007')
    stuff = api.user_timeline(screen_name = 'ippatel', count=10, include_rts = True)
    print("Sentiment Analysis Result:-")
    for status in stuff:
        text = status.text
        sentiment_value = sentiment(text)
        print(sentiment_value['sentiment'])

def exit():
    print("You press exit.")
    quit()

def compare():
    a,b,c,d=input().split()
    tweets1=api.user_timeline(screen_name=a)
    tweets2=api.user_timeline(screen_name=b)
    s1=''
    s2=''
    for tweet in tweets1:
        s1+=tweet.text
    print(s1.count(c))
    for tweet in tweets2:
        s2+=tweet.text
    print(s2.count(d))

def display():
    print("1.Retrive Tweets.")
    print("2.Count Followers.")
    print("3.Update Status.")
    print("4.Location Of Tweets.")
    print("5.Top Used Words In Tweet.")
    print("6.Sentiment Analysis.")
    print("7.Compare.")
    print("8.Exit")
    a=int(input("Enter Your Choice:- "))
    if(a==1):
        retrieve_tweets()
        display()
    elif(a==2):
        followers_count()
        display()
    elif(a==3):
        status_update()
        display()
    elif(a==4):
        loc_of_tweets()
        display()
    elif(a==5):
        Top_used_words()
        display()
    elif(a==6):
        sentiment_analysis()
        display()
    elif(a==7):
        compare()
        display()
    elif(a>7):
        exit()
display()