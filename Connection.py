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
finally:
    connection.close()
    print("Conexión finalizada.")
