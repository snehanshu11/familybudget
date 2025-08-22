# Connect to database in Python
import mysql.connector as connector


mydb = connector.connect(host = "localhost", 
                        user = "root",
                        password = "", 
                        database = "" )

my_cursor = mydb.cursor()

#1. Create Databases
#my_cursor.execute("CREATE DATABASE testdb")

#2. Show Databases
my_cursor.execute("SHOW DATABASES")

for table in my_cursor:
    print(table[0])

my_cursor.execute("USE testdb")

#3. Create Table
#my_cursor.execute("CREATE TABLE  users (name VARCHAR(255), email VARCHAR(255), age INTEGER(10), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")

my_cursor.execute("describe users")

for user in my_cursor:
    print(user)

#4. Insert one record to table
#my_cursor.execute("INSERT INTO users (name,email,age) values(%s,%s,%s)",("snehanshu","snehanshu11@gmail.com",25)) 
#mydb.commit()

#5. Insert multiple records
#records =[(f"name{i}",f"email{i}@gmail.com",f"{i}") for i in range(10)]
#my_cursor.executemany("INSERT INTO users (name,email,age) values(%s,%s,%s)",records)
#mydb.commit()

#6. select data from table

# my_cursor.execute("select * from users")
# result = my_cursor.fetchall()
# print(f"NAME\t\tEMAIL\t\t\tAGE")
# print(f"----\t\t----\t\t\t----")
# for row in result:
#     print(f"{row[0]}\t{row[1]}\t{row[2]}")
# my_cursor.execute("select * from users")
# result = my_cursor.fetchone()
# print(f"Fetch One:{result}")
        
# 7. WHERE CLAUSE
# my_cursor.execute("SELECT * FROM users WHERE age >3 AND name like '%4'")
# print(my_cursor)
# result = my_cursor.fetchall()
# for row in result:
#     print(row)

#8. UPDATE CLAUSE
#my_cursor.execute("UPDATE USERS SET NAME='snehanshu' where age=5")
#mydb.commit()


# 9. LIMIT AND ORDER
my_cursor.execute("select * from users ORDER BY NAME  LIMIT 3 ")
result=my_cursor.fetchall()
for row in result:
    print(row)

# 10. DELETE RECORDS
my_cursor.execute("DELETE FROM USERS where age=0 ")
mydb.commit()

#Close Connection
#my_cursor.close()
#mydb.close()

