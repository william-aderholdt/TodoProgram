#this will allow a user to create a new account or login.

import sqlite3


"""
This function creates a new user entry in the database.
"""
def createUser():

    connection = sqlite3.connect("myTable.db")
    crsr = connection.cursor()

    #crsr.execute(command)

    connection.commit()
    connection.close()
    return

"""
This function allows an existing user to login. 
"""
def loginUser():

    connection = sqlite3.connect("myTable.db")
    crsr = connection.cursor()

    #crsr.execute(command)

    connection.commit()
    connection.close()
    return

# William Aderholdt, May 27th, 2019