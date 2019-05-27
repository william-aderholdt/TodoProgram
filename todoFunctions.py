#this will operate todo list functions.

import sqlite3

"""
This function creates a new todo item for the user. 
"""
def createTodo():

    connection = sqlite3.connect("myTable.db")
    crsr = connection.cursor()

    #crsr.execute(command)

    connection.commit()
    connection.close()
    return

"""
This function deletes a todo item for the user. 
"""
def deleteTodo():

    connection = sqlite3.connect("myTable.db")
    crsr = connection.cursor()

    #crsr.execute(command)
    
    connection.commit()
    connection.close()
    return

"""
This function updates a todo item for the user.
"""
def updateTodo():
    connection = sqlite3.connect("myTable.db")
    crsr = connection.cursor()

    #crsr.execute(command)
    
    connection.commit()
    connection.close()
    return



# William Aderholdt, May 27th, 2019