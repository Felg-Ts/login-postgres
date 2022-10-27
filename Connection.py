import psycopg2

try:
    connection = psycopg2.connect(
        host="192.168.50.45",
        database="appweb-db",
        user="appwebuser",
        password="appwebpass"
    )

    print("Conexión realizada")
    cursor=connection.cursor()        
    cursor.execute("select version()")
    row=cursor.fetchone()
    print(row)
except Exception as ex:
    print(ex)




config.cursor.execute("select * from users")
config.rows=cursor.fetchall()
for row in rows:
    print (row)


finally:
    connection.close()
    print("Conexión finalizada.")