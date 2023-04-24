import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="OJHacker@23",
    database="mydatabase1"
)
mycursor = mydb.cursor()



mycursor.execute("SELECT * FROM customers")
#mycursor.execute("SELECT name, address FROM customers")
myresult = mycursor.fetchall()
# myresult = mycursor.fetchone()
for x in myresult:
    #print(x)
    pass



sql = "SELECT * FROM customers WHERE address='Park Lane 38'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)