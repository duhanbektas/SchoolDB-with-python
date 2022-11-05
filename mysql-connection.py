import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost", # 192.23.45.56 -- example // you need to obtain this from a hosting service with money-money-money of course.
    user = "root",
    password = "password",
    database = "node-app"
)

mycursor = mydb.cursor()


