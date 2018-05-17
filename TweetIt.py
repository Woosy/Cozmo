import tweepy
import Login

def TweetIt(tweet):

  # Fonction qui renvoie les informations de connexion
  def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

  # Fonction qui renvoie la connexion
  def getApi():
    return get_api(Login.getCfg())

  # Envoie du tweet
  status = getApi().update_status(status=tweet)

