import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()

# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

### Prevent SQL Injection ###
sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

# mycursor.execute(sql)
mycursor.execute(sql, adr)
mydb.commit()

print(mycursor.rowcount, "record(s) deleted")