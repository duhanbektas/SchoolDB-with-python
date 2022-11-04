SchoolDB



Your own password needs to be passed to connection.py;

import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",    #YOUR OWN DB HOSTNAME
    user = "root",         #YOUR OWN DB USER
    password = "password", #YOUR OWN DB PASSWORD
    database = "schooldb"  #YOUR OWN DB NAME
)

