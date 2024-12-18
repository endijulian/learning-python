import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Higway 21")

# mycursor.execute(sql, val)

# mydb.commit()
# print(mycursor.rowcount, "record inserted")


### Insert Multiple Rows ###

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]


# sql = "INSERT INTO users (name, fav) VALUES (%s, %s)"
# val = [
#   ('John', '1'),
#   ('Peter', '2'),
#   ('Amy', '3'),
#   ('Hannah', '4'),
#   ('Michael', '5')
# ]


sql = "INSERT INTO product (name) VALUES (%s)"
val = [
  ('Chocolate Heaven',),
  ('Tasty Lemons',),
  ('Vanilla Dreams',),
  ('Anggur Merah',),
  ('Anggur Putih',)
]


mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted")


### Get Inserted ID ###
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("Michelle", "Blue Village")
# mycursor.execute(sql, val)

# mydb.commit()

# print("1 record inserted, ID:", mycursor.lastrowid)