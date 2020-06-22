# USE CASE - VIEW APPLICATION
# NAME - MASOOM RAJ
# ROLL - B18CSE032
# IIT, JODHPUR
# Testing File

# import local files
from index import ViewApplication
from database import Database
# module for testing used - "unittest"
import unittest

# Stub class for testing purpose


class stub:
    # Static variables of stub class to access without creating object
    verificationError = "An error occured. Could not verify"
    viewApplicationError = "An error occured. Please try again"
    notAuthorisedError = "User not authorised to view Applications"
    genuineUser = {"name": "Account1", "email": "officeOfAccounts@gmail.com"}
    fakeUser = {"name": "FakeUser", "email": "fakeUser@gmail.com"}


# Creating an object of ViewApplication as genuine user
genuineUserAccount = ViewApplication(stub.genuineUser)
# Creating an object of ViewApplication as fake user
fakeUserAccount = ViewApplication(stub.fakeUser)


# FOR TEST PURPOSE - Created a dummy genuine account and an application

# db = Database()
# db.addUser(stub.genuineUser["name"], stub.genuineUser["email"])
# db.addApplication("This is a dummy application for testing purpose")


class Test(unittest.TestCase):
    # Test for connection Error to database while creating Class of Genuine User
    def test_connection_to_db_classCreation_Genuine(self):
        self.assertNotEqual(ViewApplication(
            stub.genuineUser), stub.verificationError)

    # Test for connection Error to database while creating Class of Fake User
    def test_connection_to_db_classCreation_Fake(self):
        self.assertNotEqual(ViewApplication(
            stub.fakeUser), stub.verificationError)

    # Test for connection Error to database while accessing "viewApp" function of Genuine User
    def test_connection_to_db_viewApp_Genuine(self):
        self.assertNotEqual(genuineUserAccount.viewApp(),
                            stub.viewApplicationError)

    # Test for connection Error to database while accessing "viewApp" function of Fake User
    def test_connection_to_db_viewApp_Fake(self):
        self.assertNotEqual(fakeUserAccount.viewApp(),
                            stub.viewApplicationError)

    # Test for viewing application as a genuine user
    def test_viewApplications_Genuine(self):
        self.assertNotEqual(genuineUserAccount.viewApp(),
                            stub.notAuthorisedError)

    # Test for viewing application as a fake user (check for thrown error)
    def test_viewApplications_Fake(self):
        self.assertEqual(fakeUserAccount.viewApp(),
                         stub.notAuthorisedError)
