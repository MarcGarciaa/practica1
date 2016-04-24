#database
#Encompassing all code related to database handling, should provide classes for
#major ‘entities’. Must provide, at least:
#• User: users of the system, must have fields:
#– name: Name
#– tagid: ID of NFC Tag (string)
#– username: Telegram User Name
#User class must provide, at least getter/setter methods for all major attributes:
#• get_name / set_name, etc.
#In addition to:
#• save(): save to DB

import sqlite3

class Database(object):
    """docstring for Database"""
    def __init__(self):
        super(Database, self).__init__()
        self.conn = sqlite3.connect("database.db")
        self.curs = self.conn.cursor()
        self.curs.execute('''CREATE TABLE Drunks(
                    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, #ID table
                    `name` TEXT,            #Drunk's name
                    `tagid` TEXT,           #ID of NFC Tag
                    `username` TEXT)''')    #Telegram User Name
        self.conn.close()

        #FAlta donarli per algun medi el name, tagid, username"

    def get_name(self, name):
        self.conn = sqlite3.connect("database.db")
        self.curs = self.conn.cursor()
        self.curs.execute=("SELECT * FROM Drunks WHERE name = :name,
                            {"name": name})
        a = self.curs.fetchall()
        self.conn.close()
        return a

    def set_name(self, name, tagid, username):
        self.conn = sqlite3.connect("database.db")
        self.curs = self.conn.cursor()
        self.curs.execute=("insert into Drunks (name, tagid, username) values (?,?,?)",
                            (name,
                             tagid,
                             username))
        self.conn.commit()
        self.conn.close()
        pass

    def save():
        pass
