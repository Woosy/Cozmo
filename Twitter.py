import tweepy
import Login

def main():

  # Fonction qui renvoie les informations de connexion
  def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)


  # Fonction qui renvoie la connexion
  def getApi():
    return get_api(Login.getCfg())


  # Contenu du tweet
  tweet = "Test 54465"
  # Envoie du tweet
  status = getApi().update_status(status=tweet)


if __name__ == "__main__":
  main()