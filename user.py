import os
import getpass

# User class
class User:
        # Constructor
        def __init__(self):				
		
		# Return actual linux user connected
		def getUsername(self):
			return getpass.getuser()

		# Return user filepath
		def getFilepath(self):
			return os.environ['HOME']


# If run as main ...
if __name__ == '__main__':
    # Test zone
	
