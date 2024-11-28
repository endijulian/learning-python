import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345 Update", "Valley 345")

mycursor.execute(sql, val)

mydb.commit()
print(mycursor.rowcount, "record(s) affected")