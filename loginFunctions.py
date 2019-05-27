#this will allow a user to create a new account or login.

import sqlite3


"""
This function creates a new todo item for the user. 
"""
def createUser():

    connection = sqlite3.connect("myTable.db")
    crsr = connection.cursor()

    #crsr.execute(command)

    connection.commit()
    connection.close()
    return

"""
This function creates a new todo item for the user. 
"""
def loginUser():

    connection = sqlite3.connect("myTable.db")
    crsr = connection.cursor()

    #crsr.execute(command)

    connection.commit()
    connection.close()
    return

# William Aderholdt, May 27th, 2019