from mysql.connector import pooling

# 1. Create a connection pool
dbconfig = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "testdb"
}

# Pool with max 5 connections
connection_pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=5,
    pool_reset_session=True,
    **dbconfig
)

# 2. Get a connection from the pool
conn = connection_pool.get_connection()

# 3. Create a cursor and run queries
cursor = conn.cursor()
cursor.execute("SELECT * FROM users ORDER BY name LIMIT 3")
for row in cursor.fetchall():
    print(row)

# 4. Release cursor + connection back to pool
cursor.close()
conn.close()   # ⚡ this does not kill connection, it returns it to the pool
