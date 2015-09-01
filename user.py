import os
import getpass

# User class
class User:
	# Constructor
	#def __init__(self):				
		
	# Return actual linux user connected
	@staticmethod
	def getUsername(self):
		return getpass.getuser()
	
	# Return user filepath
	@staticmethod
	def getFilepath(self):
		return os.environ['HOME']
