import tweepy
import twitter_auth

auth = tweepy.OAuthHandler(twitter_auth.consumer_key, twitter_auth.consumer_secret)

try:
    print("Go to " + auth.get_authorization_url() + " and copy the verfier")
except tweepy.TweepError:
    print('Error! Failed to get request token.')

verifier = str(input('Verifier:').strip())

auth.request_token['oauth_token_secret'] = verifier

try:
    auth.get_access_token(verifier)
except tweepy.TweepError:
    print('Error! Failed to get access token.')

print('save these in twitter_auth.py:\n')
print('access_token = "' + auth.access_token + '"')
print('access_token_secret = "' + auth.access_token_secret + '"')