import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()

### JOIN ###
# sql = "SELECT \
#         users.name AS user, \
#         product.name AS favorite \
#         FROM users \
#         INNER JOIN product ON users.fav = product.id"

# mycursor.execute(sql)
# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)


### LEFT JOIN ###
# sql = "SELECT \
#         users.name AS user, \
#         product.name AS favorite \
#         FROM users \
#         LEFT JOIN product ON users.fav = product.id"

# mycursor.execute(sql)
# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)


### RIGHT JOIN ###
sql = "SELECT \
        users.name AS user, \
        product.name AS favorite \
        FROM users \
        RIGHT JOIN product ON users.fav = product.id"

mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)