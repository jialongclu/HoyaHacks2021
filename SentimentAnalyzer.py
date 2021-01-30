from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class SentimentAnalyzer():
    analyzer = SentimentIntensityAnalyzer()

    def getSentiment(self, sentence):
        return self.analyzer.polarity_score(sentence)

    def checkSentiment(self, sentiment):
        if sentiment >= 0.05:
            return 1
        elif sentiment > -0.05 and sentiment < 0.05:
            return 0
        elif sentiment <= -0.05:
            return -1