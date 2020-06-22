Name - Masoom Raj
Roll - B18CSE032

Use Case - View Application

Files -

1. database.py -
    Since login module was connected, I made a dummy database on "Firebase"
    with account connected to "raj.8@iitj.ac.in", to add accounts, get accounts,
    add applications and view applications
2. index.py -
    Main file where it has a class of ViewApplication which verifies user authority
    and let them view applications else throws an error
3. tests.py -
    Testing file using "unittest", against dummy data in database. It covers connection
    to database and account of genuine and fake user.
    Total 6 test cases. (PASSED)
    Testing proof has been attached in './testProof'