# USE CASE - VIEW APPLICATION
# NAME - MASOOM RAJ
# ROLL - B18CSE032
# IIT, JODHPUR
# View Application - main file

# import firebase
from database import Database


class ViewApplication:
    # constructor function
    def __init__(self, user):
        # pass user details to contructor
        self.user = user
        # initial verified set to false
        self.verified = False
        # verify user access to only accounts section
        self.verifyUser()

    def verifyUser(self):
        # Create object of database class
        db = Database()
        # Get all accounts
        try:
            accounts = db.getUser()
            # iterate through each account
            for i in accounts:
                # Check if user name and email matches given user
                if(accounts[i]["name"] == self.user["name"]):
                    if(accounts[i]["email"] == self.user["email"]):
                        # if user is from office of accounts then set verified to True
                        self.verified = True
        except:
            # if error occurs
            return("An error occured. Could not verify")

    def viewApp(self):
        if(self.verified):
            db = Database()
            try:
                applications = db.getApplication()
                return applications
            except:
                return("An error occured. Please try again")
        else:
            return("User not authorised to view Applications")
