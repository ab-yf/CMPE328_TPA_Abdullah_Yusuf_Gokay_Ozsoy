#  ----------------------------------------------------- 
#  Title: Sentiment Analysis through Twitter
#  Author: Abdullah Yusuf, Gökay Özsoy
#  ID: 99975171716, 14057733156
#  Class: CMPE 328 - Cloud Computing
#  Assignment: Group Project

#  Description: This program access Tweets regarding our desired keyword(s) 
#  through Tweepy, tokenizes it, analyses the tweets and then writes the 
#  tweets to a CSV file after displaying graphically what people think about 
#  our keyword(s)
#  -----------------------------------------------------


# Import TextBlob, Tweepy and MatPlotLib which are libraries for Python
# TextBlot is used for analysing the tweets based on their sentiments (positive, negative or neutral)
# Tweepy is used solely for importing tweets by establishing a connection with our Twitter API
# MatPlotLib is used ot plot our sentiment pie chart based on our tweets

import sys, tweepy, csv, re
import matplotlib
from textblob import TextBlob
import matplotlib.pyplot as plt
plt.plot()


class SentimentAnalysis:

    def __init__(self):
        self.tweets = []
        self.tweetText = []

# API Connection for Twitter 
# Fill in the below details based on your what Twitter has provided for your API

    def DownloadData(self):
        # authenticating
        ourconsumerKey = 'PgS3doGO1LAf2GRQ8W1JBXZYq'
        ourconsumerSecret = 'JaroXL8RRhh0297OPDlPBgpb8WlbuE9wmGMGcg0dPxW9U9wk2O'
        ouraccessToken = '955889656624709634-rBGJ2mo5tEaIl5Lg5CHDxUzgHwci54Y'
        ouraccessTokenSecret = 'DTbyh3OlpBm7LRiS62e2xwwT1zPhPlvHH3r8HN6ZKJf2Q'

        # Our authorization to establish a connection with Twitter through Tweepy
        auth = tweepy.OAuthHandler(ourconsumerKey, ourconsumerSecret)
        auth.set_access_token(ouraccessToken, ouraccessTokenSecret)
        ourApi = tweepy.API(auth)

        # Taking input from our user regarding what they want to search, and how many tweets do they want to go through

        searchTerm = input("Enter your desired keywords/hashtag which you would like to research: ")
        NoOfTerms = int(input("Enter the amount of tweets which you would like to analyse in your desired category: "))

        # We are commencing our search here for the tweets.
        self.tweets = tweepy.Cursor(ourApi.search, q=searchTerm, lang = "en").items(NoOfTerms)

        # We are openening/creating a file to which we will save our tweets to.
        csvFile = open('result.csv', 'a')

        # We are using a CSV writer to write our tweets to it.
        csvWriter = csv.writer(csvFile)
        


        # These are intialized variables which will be used to store values for polarity of the tweets.
        
        polarity = 0
        positive = 0
        weaklypositive = 0
        stronglypositive = 0
        negative = 0
        weaklynegative = 0
        stronglynegative = 0
        neutral = 0


        # iterating through tweets fetched
        for tweet in self.tweets:
            #Append to temp so that we can store in csv later. I use encode UTF-8
            self.tweetText.append(self.cleanTweets(tweet.text).encode('utf-8'))
            # print (tweet.text.translate(non_bmp_map))    #print tweet's text
            analysis = TextBlob(tweet.text)
            # print(analysis.sentiment)  # print tweet's polarity
            polarity += analysis.sentiment.polarity  # adding up polarities to find the average later

            if (analysis.sentiment.polarity == 0):  # adding reaction of how people are reacting to find average later
                neutral += 1
            elif (analysis.sentiment.polarity > 0 and analysis.sentiment.polarity <= 0.3):
                weaklypositive += 1
            elif (analysis.sentiment.polarity > 0.3 and analysis.sentiment.polarity <= 0.6):
                positive += 1
            elif (analysis.sentiment.polarity > 0.6 and analysis.sentiment.polarity <= 1):
                stronglypositive += 1
            elif (analysis.sentiment.polarity > -0.3 and analysis.sentiment.polarity <= 0):
                weaklynegative += 1
            elif (analysis.sentiment.polarity > -0.6 and analysis.sentiment.polarity <= -0.3):
                negative += 1
            elif (analysis.sentiment.polarity > -1 and analysis.sentiment.polarity <= -0.6):
                stronglynegative += 1


        # Write the tweets to a CSV file, then close the file.
        csvWriter.writerow(self.tweetText)
        csvFile.close()

        # Finding an average of how the people are reacting to our keywords
        positive = self.percentages(positive, NoOfTerms)
        weaklypositive = self.percentages(weaklypositive, NoOfTerms)
        stronglypositive = self.percentages(stronglypositive, NoOfTerms)
        negative = self.percentages(negative, NoOfTerms)
        weaklynegative = self.percentages(weaklynegative, NoOfTerms)
        stronglynegative = self.percentages(stronglynegative, NoOfTerms)
        neutral = self.percentages(neutral, NoOfTerms)

        # finding average reaction
        polarity = polarity / NoOfTerms

        # printing out data
        print("How people are reacting on " + searchTerm + " by analyzing " + str(NoOfTerms) + " tweets.")
        print()
        print("General Report: ")

        if (polarity == 0):
            print("Neutral")
        elif (polarity > 0 and polarity <= 0.3):
            print("Weakly Positive")
        elif (polarity > 0.3 and polarity <= 0.6):
            print("Positive")
        elif (polarity > 0.6 and polarity <= 1):
            print("Strongly Positive")
        elif (polarity > -0.3 and polarity <= 0):
            print("Weakly Negative")
        elif (polarity > -0.6 and polarity <= -0.3):
            print("Negative")
        elif (polarity > -1 and polarity <= -0.6):
            print("Strongly Negative")

        print()
        print("Detailed Report: ")
        print(str(positive) + "% people thought it was positive")
        print(str(weaklypositive) + "% people thought it was weakly positive")
        print(str(stronglypositive) + "% people thought it was strongly positive")
        print(str(negative) + "% people thought it was negative")
        print(str(weaklynegative) + "% people thought it was weakly negative")
        print(str(stronglynegative) + "% people thought it was strongly negative")
        print(str(neutral) + "% people thought it was neutral")

        self.plotourPieChart(positive, weaklypositive, stronglypositive, negative, weaklynegative, stronglynegative, neutral, searchTerm, NoOfTerms)


    def cleanTweets(self, tweet):
        # Remove Links, Special Characters etc from tweet (a form of tokenization)
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())

    # Our function to calculate the percentages
    def percentages(self, part, whole):
        temp = 100 * float(part) / float(whole)
        return format(temp, '.2f')

    def plotourPieChart(self, positive, wpositive, spositive, negative, wnegative, snegative, neutral, searchTerm, noOfSearchTerms):
        labels = ['Positive [' + str(positive) + '%]', 'Weakly Positive [' + str(wpositive) + '%]','Strongly Positive [' + str(spositive) + '%]', 'Neutral [' + str(neutral) + '%]',
                  'Negative [' + str(negative) + '%]', 'Weakly Negative [' + str(wnegative) + '%]', 'Strongly Negative [' + str(snegative) + '%]']
        sizes = [positive, wpositive, spositive, neutral, negative, wnegative, snegative]
        colors = ['yellowgreen','lightgreen','darkgreen', 'gold', 'red','lightsalmon','darkred']
        patches, texts = plt.pie(sizes, colors=colors, startangle=90)
        plt.legend(patches, labels, loc="best")
        plt.title('How people are reacting on ' + searchTerm + ' after the analysis of ' + str(noOfSearchTerms) + ' Tweets.')
        plt.axis('equal')
        plt.tight_layout()
        plt.show()


if __name__== "__main__":
    sa = SentimentAnalysis()
    sa.DownloadData()
