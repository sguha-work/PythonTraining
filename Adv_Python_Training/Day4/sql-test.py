# before start coding install connecter using following command
# python3.7 -m pip install mysql-connector --user
print('==============================================================')
import mysql.connector
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="python-test-db-1"
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = [
        ('Peter', 'Lowstreet 4'),
        ('Amy', 'Apple st 652'),
        ('Hannah', 'Mountain 21'),
        ('Michael', 'Valley 345'),
        ('Sandy', 'Ocean blvd 2'),
        ('Betty', 'Green Grass 1'),
        ('Richard', 'Sky st 331'),
        ('Susan', 'One way 98'),
        ('Vicky', 'Yellow Garden 2'),
        ('Ben', 'Park Lane 38'),
        ('William', 'Central st 954'),
        ('Chuck', 'Main Road 989'),
        ('Viola', 'Sideway 1633')
    ]

    mycursor.executemany(sql, val)
    print('All data inserted')
    mydb.commit()
except:
    print('Unable to connect to database')
finally:
    print('Closing program')
    mydb.close()
print('==============================================================')
