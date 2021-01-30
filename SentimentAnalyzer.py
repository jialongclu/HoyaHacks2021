from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class SentimentAnalyzer():
    analyzer = SentimentIntensityAnalyzer()

    def getSentiment(self, sentence):
        return self.analyzer.polarity_scores(sentence)

    def checkSentiment(self, sentiment):
        if sentiment['compound'] >= 0.05:
            return 1
        elif sentiment['compound'] > -0.05 and sentiment['compound'] < 0.05:
            return 0
        elif sentiment['compound'] <= -0.05:
            return -1