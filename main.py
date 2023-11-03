import mysql.connector
from html.parser import HTMLParser

mydb = mysql.connector.connect(
    host="localhost", user="theprogrammer", password="Kalleanka9!", db="secureProject"
)

print(mydb)


