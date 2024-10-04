import mysql.connector

try:
    dbcon=mysql.connector.connect(host="localhost",user='root',password='root',database='8am') 
    cursor = dbcon.cursor()
    cursor.execute('insert into user values(103,"priyanka","New Delhi");')
    #commit is missing
    dbcon.commit()
    print("Inserted successfully")
except mysql.connector.Error as err:

    print(err) 
    
finally:
    cursor.close()
    dbcon.close()