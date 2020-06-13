import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root"
)

print(mydb)

import cx_Oracle
connection = cx_Oracle.connect( "hr", userpwd, "dbhost.example.com/orclpdb1",
        encoding="UTF-8")
print(connection)
