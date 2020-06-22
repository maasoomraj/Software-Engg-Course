# USE CASE - VIEW APPLICATION
# NAME - MASOOM RAJ
# ROLL - B18CSE032
# IIT, JODHPUR
# Firebase database for adding and getting accounts from database

# import firebase
from firebase import firebase


class Database:
    # Constructor
    def __init__(self):
        # Initialise firebase
        self.firebase = firebase.FirebaseApplication(
            'https://softwareengineering-29cde.firebaseio.com', None)

    # Function to add account
    def addUser(self, name, email):
        # sets given data of user to local variable
        data = {
            "name": name,
            "email": email
        }

        # try posting to firebase
        try:
            # attempt to add data to "Account" of database
            self.firebase.post('Accounts', data)
        except:
            # Handle Error
            print("An error occured. Please try again")

    # Function to get all accounts
    def getUser(self):
        # try connecting to firebase
        try:
            # get all accounts from database
            accounts = self.firebase.get('/Accounts', None)
            # return accounts from database
            return accounts
        except:
            # Handle Error
            print("An error occured. Please try again")

    # Function to add application
    def addApplication(self, application):
        # sets given details of application to local variable
        data = {
            "details": application
        }

        # try posting to firebase
        try:
            # attempt to add data to "Applications" of database
            self.firebase.post('Applications', data)
        except:
            # Handle Error
            print("An error occured. Please try again")

    # Function to get all accounts
    def getApplication(self):
        # try connecting to firebase
        try:
            # get all accounts from database
            applications = self.firebase.get('/Applications', None)
            # return accounts from database
            return applications
        except:
            # Handle Error
            print("An error occured. Please try again")
