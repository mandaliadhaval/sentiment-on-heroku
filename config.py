class Config(object):
    SITE_NAME = 'Sentiment Analysis on Movie Reviews'
    SITE_SLUG_NAME = 'imdb-sentiment-analysis'
    TAGLINES = ['Sentiment Analysis using Deep Learning']
    SITE_DESCRIPTION = 'Sentiment analysis on movie reviews'
    SITE_KEYWORDS = 'sentiment analysis, imdb, movie, review, nlp, deep learning'
    ADMINS = ['dhavalmandalia@gmail.com']

class DevelopmentConfig(Config):
    DOMAIN = 'localhost=14000'
    ASSET_DOMAIN = 'localhost=14000'

class ProductionConfig(Config):
    DOMAIN = 'imdb-sentiment-analysis.herokuapp.com'
    ASSET_DOMAIN = 'imdb-sentiment-analysis.herokuapp.com'
