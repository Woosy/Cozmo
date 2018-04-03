import tweepy
import socket
import requests
import time
import Login


class TwitterStreamListener(tweepy.StreamListener):

	def on_status(self, status):
		get_tweet(status)

	# Liste des codes d'erreur Twitter : https://dev.twitter.com/overview/api/response-codes
	def on_error(self, status_code):
		if status_code == 403:
			print("403 - Forbidden")
			return False
		if status_code == 404:
			print("404 Not Found !")
			return False
		if status_code == 429:
			print("Too Many Requests")
			return False


def get_tweet(tweet):
	message = tweet.text
	messageSplitted = message.split(" ")

	print("Message : " + message)
	print("Nom expediteur\t: " + tweet.user.screen_name)
	#print("Status fav\t: " + str(tweet.favorited))
	#print("Nombre de fav\t: " + str(tweet.favorite_count))
	#print("Nom expediteur\t: " + tweet.user.name)
	if (messageSplitted[1] == "say"):
                # Appel de la fonction qui fait dire à Cozmo le texte
                print("Cozmo va dire : ")
                messageSplitted.remove("@TestBot96875418")
                messageSplitted.remove("say")
                temp = " ".join(messageSplitted)
                print(temp)



if __name__ == '__main__':

	# Authentication :
	auth = tweepy.OAuthHandler(Login.consumer_key, Login.consumer_secret)
	auth.secure = True
	auth.set_access_token(Login.access_token, Login.access_token_secret)

	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=10, retry_delay=5, retry_errors=5)

	streamListener = TwitterStreamListener()
	myStream = tweepy.Stream(auth=api.auth, listener=streamListener)

	myStream.filter(track=['TestBot96875418'], async=True)