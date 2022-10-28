#Librerías
from flask import Flask,render_template
#from config import postgres
import psycopg2

app = Flask(__name__)	

#Formulario inicio de la aplicación

@app.route('/',methods=["GET"])
def inicio():
    return render_template("inicio.html",titulo="Inicio")

#Página despues de inicio.

@app.route('/ids/<appd>',methods=["Post"])
def ids(appd):

    if appd == "dma":

        listadatos = []

        rutaid = "/dma/"
        titulo = "Current weather data"
        titulo2 = "Current weather data"

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
            row=cursor.fetchall()
            for rows in row:
                listadatos.append(rows)            
            #print(row)
        except Exception as ex:
            print(ex)
        #finally:
        #    connection.close()
        #    print("Conexión finalizada.")

        #for rows in postgres():
        #     listadatos.append(rows)

        #cursor=config.connection.cursor()        
        #cursor.execute("select version()")
        #row=cursor.fetchone()
        #print(row)

        #connection.cursor.execute("select * from users")
        #connection.rows=connection.cursor.fetchall()
        #for row in connection.rows:
        #    print (row)

        if len(listadatos) == 0:
            return render_template("error404.html",titulo="Error404",titulo2="Error404",errormesaje="Los caracteres introducidos no coinciden con ningún nombre. Recuerde que la primera letra de la ciudad tiene que ser en mayúsculas",urlform="/forms/dma")

        return render_template("ids.html",titulo=titulo,titulo2=titulo2,listadatos=listadatos,rutaid=rutaid)

if __name__ == '__main__':
    app.run("0.0.0.0",5000,debug=True)