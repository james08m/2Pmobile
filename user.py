import os
import getpass

# User class
class User:
	# Constructor
	#def __init__(self):				
		
	# Return actual linux user connected
	@staticmethod
	def getUsername():
		return getpass.getuser()
	
	# Return user filepath
	@staticmethod
	def getFilepath():
		return os.environ['HOME']
