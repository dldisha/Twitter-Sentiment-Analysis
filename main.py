import sys,tweepy,csv,re
from textblob import TextBlob
import matplotlib.pyplot as plt


def percentage(part, whole):
    return 100 * float(part) / float(whole)

#Establishing relationship with API
consumerKey = "Your API key"
consumerSecret = "Your API key"
accessToken = "Your API key"
accessTokenSecret = "Your API key"
#Authenticating
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

# input for term to be searched and how many tweets to search
searchTerm = input("Enter Keyword/Tag to search about: ")
NoOfTerms = int(input("Enter how many tweets to search: "))

# searching for tweets
tweets = tweepy.Cursor(api.search, q=searchTerm, lang="en").items(NoOfTerms)

# creating some variables to store info
polarity = 0
positive = 0
negative = 0
neutral = 0

# iterating through tweets fetched
for tweet in tweets:
     # print (tweet.text.translate(non_bmp_map))    #print tweet's text
     analysis = TextBlob(tweet.text)
     # print(analysis.sentiment)  # print tweet's polarity
     polarity += analysis.sentiment.polarity  # adding up polarities to find the average later

     if (analysis.sentiment.polarity == 0):  # adding reaction of how people are reacting to find average later
         neutral += 1
     elif (analysis.sentiment.polarity > 0.00):
         positive += 1
     elif (analysis.sentiment.polarity < 0.00):
         negative += 1


# finding average of how people are reacting
positive = percentage(positive, NoOfTerms)
negative = percentage(negative, NoOfTerms)
neutral = percentage(neutral, NoOfTerms)

positive = format(positive, '.2f')
negative = format(negative, '.2f')
neutral = format(neutral, '.2f')

# printing out data
print("How people are reacting on " + searchTerm + " by analyzing " + str(NoOfTerms) + " tweets.")
print()
print("General Report: ")

if (polarity == 0):
    print("Neutral")
elif (polarity > 0):
    print("Positive")
elif (polarity < 0):
    print("Negative")


#plotting graph
labels = ['Positive [' + str(positive) + '%]', 'Neutral [' + str(neutral) + '%]', 'Negative [' + str(negative) + '%]']
sizes = [positive, neutral, negative]
colors = ['green', 'blue', 'red']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title('How people are reacting on ' + searchTerm + ' by analyzing ' + str(NoOfTerms) + ' Tweets.')
plt.axis('equal')
plt.tight_layout()
plt.show()
