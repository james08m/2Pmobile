import pickle

# User class
class User:
        # Constructor
        def __init__(self):
                self.username = "NONE"
                self.password = "NONE"
                self.lastlogin = "NONE"
                self.image_path = "images/user.png"				
        # Save class information in a .info file
        def save(self):
                with open('userdata.info', 'wb') as file:
                        pickler = pickle.Pickler(file)
                        pickler.dump(self) # save user	
        # Load user informations from .info file
        def load(self):
                with open('userdata.info', 'rb') as file:
                        pickler = pickle.Unpickler(file)
                        copy = pickler.load(); # Get saved user			
                        # Clone current user from saved user
                        self.clone(copy)
        # Clone a user from another user passed by parameter
        def clone(self,copy):
                self.id = copy.id
                self.username = copy.username
                self.password = copy.password
                self.lastlogin = copy.lastlogin
                self.image_path = copy.image_path

# If run as main ...
if __name__ == '__main__':
    # Make a void save and load it
	user = User()
	user.id = 000000
	user.username = "Beta"
	user.password = "beta01"
	user.lastlogin = "00/00/00"
	user.image_path = "images/user.png" 
	user.save() # Save user
	user2 = User()
	user2.load() # Load user
