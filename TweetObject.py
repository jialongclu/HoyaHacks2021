class TweetObject():
     name = None
     username = None
     datestamp = None
     likes_count = None 
     tweet = None
     id = None
     
     def __init__(self, name, username, datestamp, likes_count, tweet, id):
         self.id = id
         self.name = name
         self.username = username
         self.datestamp = datestamp
         self.likes_count = likes_count
         self.tweet = tweet

