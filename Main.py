import asyncio
import socket
import time
import datetime
import sys
import requests
import tweepy
import cozmo
import Login
import TweetIt
from timeit import default_timer
from cozmo.util import degrees, distance_mm, speed_mmps


##############################
# Initialisation :
seconds = 0
speed = 0
largeur = 0
longueur = 0
nombreTours = 0




##############################
# Stream Listener :
class TwitterStreamListener(tweepy.StreamListener):

	def on_status(self, status):
		get_tweet(status)

	# Voir liste des codes d'erreur Twitter : https://dev.twitter.com/overview/api/response-codes
	def on_error(self, status_code):
		if status_code == 403:
			print("403 - Forbidden")
			return False
		if status_code == 404:
			print("404 - Not found")
			return False




##############################
# Récupération tweet (stream)

def get_tweet(tweet):

	message = tweet.text
	messageSplitted = message.split(" ")

	# Debug :
	print("Message : " + message)
	print("Nom expediteur\t: " + tweet.user.screen_name)


	# ##############################
	# # Analyse des messages reçus :
	#
	# if (messageSplitted[1] == "say"):
    #             print("Cozmo va dire : ")
    #             messageSplitted.remove("@TestBot96875418")
    #             messageSplitted.remove("say")
    #             textToSay = " ".join(messageSplitted)


	##############################
	# Démarrage du parcours :

	if (messageSplitted[1] == "start"):

				# Initialisation
				temp = messageSplitted[2].split("x")
				global longueur
				longueur = temp[0]
				global largeur
				largeur = temp[1]
				global nombreTours
				nombreTours = messageSplitted[3]
				global speed
				speed = messageSplitted[4]

				# Debug
				print("Longueur : " + longueur)
				print("Largeur : " + largeur)
				print("Nombre de tours : " + nombreTours)
				print("Vitesse : " + speed)

				# Démarrage
				cozmo.run_program(cozmo_program)




###############################
# Execution du code via Cozmo :

def cozmo_program(robot: cozmo.robot.Robot):
	i = 0
	now = datetime.datetime.now()
	start = datetime.datetime.now()
	while i != int(nombreTours):
		robot.drive_straight(distance_mm(longueur), speed_mmps(speed)).wait_for_completed()
		robot.turn_in_place(degrees(90)).wait_for_completed()
		robot.drive_straight(distance_mm(largeur), speed_mmps(speed)).wait_for_completed()
		robot.turn_in_place(degrees(90)).wait_for_completed()
		robot.drive_straight(distance_mm(longueur), speed_mmps(speed)).wait_for_completed()
		robot.turn_in_place(degrees(90)).wait_for_completed()
		robot.drive_straight(distance_mm(largeur), speed_mmps(speed)).wait_for_completed()
		robot.turn_in_place(degrees(90)).wait_for_completed()
		i += 1
		if (i == 1):
			TweetIt.TweetIt(str(now.hour) + "h" + str(now.minute) + " : Je viens de terminer mon premier tour")
			robot.say_text(str(now.hour) + "h" + str(now.minute) + " : Je viens de terminer mon premier tour").wait_for_completed()
		elif (i == 2):
			TweetIt.TweetIt(str(now.hour) + "h" + str(now.minute) + " : Je viens de terminer mon deuxième tour")
			robot.say_text(str(now.hour) + "h" + str(now.minute) + " : Je viens de terminer mon deuxième tour").wait_for_completed()
		elif (i == 3):
			TweetIt.TweetIt(str(now.hour) + "h" + str(now.minute) + " : Je viens de terminer mon troisième tour")
			robot.say_text(str(now.hour) + "h" + str(now.minute) + " : Je viens de terminer mon troisième tour").wait_for_completed()
		elif (i == 4):
			TweetIt.TweetIt(str(now.hour) + "h" + str(now.minute) + " : Je viens de terminer mon quatrième tour")
			robot.say_text(str(now.hour) + "h" + str(now.minute) + " : Je viens de terminer mon quatrième tour").wait_for_completed()
		elif (i == 5):
			TweetIt.TweetIt(str(now.hour) + "h" + str(now.minute) + " : Je viens de terminer mon cinquième tour")
			robot.say_text(str(now.hour) + "h" + str(now.minute) + " : Je viens de terminer mon cinquième tour").wait_for_completed()
		elif (i == 6):
			TweetIt.TweetIt(str(now.hour) + "h" + str(now.minute) + " : Je viens de terminer mon sixième tour")
			robot.say_text(str(now.hour) + "h" + str(now.minute) + " : Je viens de terminer mon sixième tour").wait_for_completed()
		elif (i == 7):
			TweetIt.TweetIt(str(now.hour) + "h" + str(now.minute) + " : Je viens de terminer mon septième tour")
			robot.say_text(str(now.hour) + "h" + str(now.minute) + " : Je viens de terminer mon septième tour").wait_for_completed()
		elif (i == 8):
			TweetIt.TweetIt(str(now.hour) + "h" + str(now.minute) + " : Je viens de terminer mon huitième tour")
			robot.say_text(str(now.hour) + "h" + str(now.minute) + " : Je viens de terminer mon huitième tour").wait_for_completed()
		elif (i == 9):
			TweetIt.TweetIt(str(now.hour) + "h" + str(now.minute) + " : Je viens de terminer mon neufième tour")
			robot.say_text(str(now.hour) + "h" + str(now.minute) + " : Je viens de terminer mon neufième tour").wait_for_completed()
		elif (i == 10):
			TweetIt.TweetIt(str(now.hour) + "h" + str(now.minute) + " : Je viens de terminer mon dixième tour")
			robot.say_text(str(now.hour) + "h" + str(now.minute) + " : Je viens de terminer mon dixième tour").wait_for_completed()

	end = datetime.datetime.now()
	delta = end - start
	seconds = delta.seconds
	TweetIt.TweetIt(str(now.hour) + "h" + str(now.minute) + " : J'ai terminé le parcours en " + str(seconds) + " secondes")
	robot.say_text("J'ai terminé le parcours en " + str(seconds) + " secondes").wait_for_completed()
	sys.exit("Fin du parcours")



if __name__ == '__main__':

	# Authentication :
	auth = tweepy.OAuthHandler(Login.consumer_key, Login.consumer_secret)
	auth.secure = True
	auth.set_access_token(Login.access_token, Login.access_token_secret)

	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=10, retry_delay=5, retry_errors=5)

	streamListener = TwitterStreamListener()
	myStream = tweepy.Stream(auth=api.auth, listener=streamListener)

	myStream.filter(track=['TestBot96875418'], async=True)
