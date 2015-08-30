__author__ = 'J08M'
import pickle
from utilities import *

# Log class
class Log:
    def __init__(self):
        self.logs = ["Create log"]
        self.size = 1

    # Add a string to the logs list
    def add(self, log):
        self.logs.append("[" + getTimeToSecondes() + "] " + log)
        self.size = len(self.logs)

    def display(self):
        for x in self.logs:
            print("[log] " + x)

    # Save log information in a .info file
    def save(self):
        with open('logdata.info', 'wb') as file:
            pickler = pickle.Pickler(file)
            pickler.dump(self) # save logs

    # Load log informations from .info file
    def load(self):
        with open('logdata.info', 'rb') as file:
            pickler = pickle.Unpickler(file)
            copy = pickler.load(); # Get saved log
            # Clone the log from saved one
            self.clone(copy)

    # Clone a user from another user passed by parameter
    def clone(self,copy):
        self.logs = copy.logs
        self.size = copy.size

# If run as main ...
if __name__ == '__main__':
    log = Log()
    log2 = Log()
    log.add("waiting...")
    log.add("test...")
    log.add("end...")
    log.save()
    log2.load()
    log2.display()