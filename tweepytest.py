# this file is for testing our api 
import tweepy

auth = tweepy.OAuthHandler('5rfdtlH5uiC66m7JfbheJRzrs', 'Isk41QlIdEQGdYasHxkrQI4uxH4pPb012MF1RGJRPdYiM5CEvg')
auth.set_access_token('727102653541552130-N51h0aT7Bvv641tU9tTtl2iTKoal2lZ', 't8KWz8P7MSvw2Vcp03QX8jnCZKJyYNgQ5fo2O0SqL2wnV')

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
