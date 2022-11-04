SchoolDB



Your own password needs to be passed to connection.py;

import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "schooldb"
)

