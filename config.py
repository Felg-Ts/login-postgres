from sqlite3 import Row
import psycopg2

def postgres():
    try:
        connection = psycopg2.connect(
            host="192.168.50.45",
            database="appweb-db",
            user="appwebuser",
            password="appwebpass"
        )
        print("Conexión realizada")
        cursor=connection.cursor()        
        cursor.execute("select * from users")
        row=cursor.fetchone()
        #print(row)
        return row
    except Exception as ex:
        print(ex)
    #finally:
    #    connection.close()
    #    print("Conexión finalizada.")


#config.cursor.execute("select * from users")
#config.rows=cursor.fetchall()
#for row in rows:
#    print (row)


