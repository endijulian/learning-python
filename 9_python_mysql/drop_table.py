import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()

# sql = "DROP TABLE customers_test"
sql = "DROP TABLE IF EXISTS customers_test"
mycursor.execute(sql)