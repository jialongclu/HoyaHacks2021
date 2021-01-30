from flask import Flask, render_template, request
from SearchForm import SearchForm
from TweetFinder import TweetFinder
from StockFinder import StockFinder
from SentimentAnalyzer import SentimentAnalyzer
from sqlalchemy import exc
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from TweetObject import TweetObject
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/HoyaHacks"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class TweetModel(db.Model):
    __tablename__ = 'tweets'

    tweet_id = db.Column(db.BigInteger(), primary_key=True)
    tweet = db.Column(db.String())
    tweet_sentiment = db.Column(db.Integer())
    tweet_name = db.Column(db.String())
    tweet_username = db.Column(db.String())
    tweet_likes = db.Column(db.Integer())
    tweet_datestamp = db.Column(db.String())
    day1Price = db.Column(db.Float())
    day2Price = db.Column(db.Float())
    day3Price = db.Column(db.Float())
    day4Price = db.Column(db.Float())
    day5Price = db.Column(db.Float())
    company = db.Column(db.String())

    def __init__(self, tweet_id, tweet, tweet_sentiment, tweet_name, tweet_username, tweet_likes, 
    tweet_datestamp, day1Price, day2Price, day3Price, day4Price, day5Price, company):
        self.tweet_id = tweet_id
        self.tweet = tweet
        self.tweet_sentiment = tweet_sentiment
        self.tweet_name = tweet_name
        self.tweet_username = tweet_username
        self.tweet_likes = tweet_likes
        self.tweet_datestamp = tweet_datestamp
        self.day1Price = day1Price
        self.day2Price = day2Price
        self.day3Price = day3Price
        self.day4Price = day4Price
        self.day5Price = day5Price
        self.company = company

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/displayTweets', methods=['GET', 'POST'])
def displayTweets():
    form = SearchForm(request.form)
    if request.method == 'POST' and form.validate():
        twitterUser = str(form.username.data)
        companyName = str(form.company.data)
        users = TweetModel.query.filter(TweetModel.tweet_username == twitterUser, TweetModel.company == companyName).all()
        ret = []
        for user in users:
            tweetObject = TweetObject(user.tweet_name, user.tweet_username, user.tweet_datestamp, user.tweet_likes, user.tweet, user.tweet_id)
            ret.append(tweetObject)
        if len(ret) > 0:
            return render_template('displayTweets.html', data=ret)

        # Handling Twitter
        finder = TweetFinder(twitterUser, companyName)
        filteredTweets = finder.findFilteredTweets()
        user = finder.getUser()
        finder.saveAvatarLocally(user)
        sentimentAnalyzer = SentimentAnalyzer()
        stockFinder = StockFinder(companyName)
        hasTicker = stockFinder.hasTicker()
        ret = []

        if hasTicker == False:
            return "COULD NOT FIND COMPANY. RETRY!"

        for t in filteredTweets:
            if len(ret) >= 8:
                break
            todaysDate = datetime.datetime.strptime(datetime.datetime.today().strftime('%Y-%m-%d'), '%Y-%m-%d')
            tenDaysBeforeToday = todaysDate - datetime.timedelta(days=10)
            normalizedDate = datetime.datetime.strptime(t.datestamp, "%Y-%m-%d")

            if normalizedDate <= tenDaysBeforeToday:
                ret.append(t)
                try:
                    sentimentAnalyzer = SentimentAnalyzer()
                    sentiment = sentimentAnalyzer.getSentiment(t.tweet)
                    score = sentimentAnalyzer.checkSentiment(sentiment)
                    
                    stockPrices = stockFinder.getStockPrice(t.datestamp)

                    saveData = TweetModel(tweet_id=t.id, tweet=t.tweet, tweet_sentiment=score, tweet_name=t.name, 
                    tweet_username=t.username, tweet_likes=t.likes_count, tweet_datestamp=t.datestamp, 
                    day1Price=stockPrices[0], day2Price=stockPrices[1], day3Price=stockPrices[2], day4Price=stockPrices[3], day5Price=stockPrices[4], company=companyName)
                    db.session.add(saveData)
                    db.session.commit()
                except exc.SQLAlchemyError as e:
                    pass
        return render_template('displayTweets.html', data=ret)
    return 'Wrong'


@app.route('/tweetProfile', methods=['GET', 'POST'])
def tweetProfile():
    if request.method == 'POST':
        data = TweetModel.query.get(request.form['id'])
        JSON = {'company': data.company, 'id': request.form['id'], 'sentiment': data.tweet_sentiment, "username": data.tweet_username,
        "one":data.day1Price, "two": data.day2Price, "three":data.day3Price, "four": data.day4Price, "five": data.day5Price, "tweet": data.tweet}
        return render_template('tweetProfile.html', data=JSON)

if __name__ == '__main__':
    app.run(debug=True)