#!/usr/bin/python


from time import sleep
from datetime import datetime, timedelta
import serial


class phone:
	# Constructeur
	def __init__(self):
		self.SIGNAL = 0
		
	# Methode permettant d'appeller au numero passé en paramètre
	def call(self, number):
		print("Calling " + number);
		
		# Envoi la commande AT return et attent la réponse pour initialiser
		serialport.write("AT\r")
		response = serialport.readlines(None)

		# Envoi la commande AT dialog et attent la réponse pour commencer l'appelle
		serialport.write("ATD " + numberstring + ';\r')
		response = serialport.readlines(None)
		
		# Écrit la réponse dans le terminal
		print response
	
	# Méthode permettant d'envoyer un sms
	def sendSMS(self, number, message):

	# Méthode permettant de recevoir un sms et qui retourne le message et le numero de la source
	def receivSMS(self):


		
