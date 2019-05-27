#This module populates all current todo items.

import sqlite3

"""
Class creator.  Each entry on the todo list will be an object.
"""
class TodoClass:
    def __init__(self, title, dateDue, complete):
        self.title = title
        self.dateDue = dateDue
        self.complete = complete


"""
This function creates a dictionary with all current rows associated with 
the userID the user signed in with. 
"""
def pullTodos():

    connection = sqlite3.connect("myTable.db")
    crsr = connection.cursor()

    #crsr.execute(command)
    
    connection.commit()
    connection.close()
    return

"""
This function creates the object for each of the entries from
pullTodos from the TodoClass.
"""
def populateTodos():
    return

