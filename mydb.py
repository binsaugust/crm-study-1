import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='1975#jesusBless'
)

cursorObject = dataBase.cursor()
cursorObject.execute(
    "CREATE DATABASE crmstudy"
)

