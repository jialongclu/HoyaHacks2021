import twint
import urllib.request 

class TweetFinder():
    config = None
    
    def __init__(self, tweet_id, companyName):
        self.config = twint.Config()
        self.config.Username = tweet_id
        self.config.Store_object = True
        self.config.Hide_output = True
        self.config.Filter_retweets = True
        self.config.Popular_tweets = True
        self.config.Search = companyName
        # TODO: Remove Limit for Demo
        self.Limit = 1

    def findFilteredTweets(self):
        twint.run.Search(self.config)
        listofTweets = twint.output.tweets_list[:8]
        return listofTweets
    
    def getUser(self):
        twint.run.Lookup(self.config)
        user = twint.output.users_list[0]
        return user

    def saveAvatarLocally(self, user):
        urllib.request.urlretrieve(user.avatar, "static/images/" + user.username + '.jpg')

        

    