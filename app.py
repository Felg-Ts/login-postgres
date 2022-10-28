#Librerías
from flask import Flask,render_template
import psycopg2

app = Flask(__name__)	

#Formulario inicio de la aplicación

@app.route('/',methods=["GET"])
def inicio():
    return render_template("login.html",titulo="Login")

#Página despues de inicio.

@app.route('/form/<appd>',methods=["POST"])
def ids(appd):

    if appd == "log":

        listadatos = []

        rutaid = "/dma/"

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
        finally:
            connection.close()
            print("Conexión finalizada.")

        if len(listadatos) == 0:
            return render_template("error404.html",titulo="Error404",titulo2="Error404",errormesaje="Los caracteres introducidos no coinciden con ningún nombre. Recuerde que la primera letra de la ciudad tiene que ser en mayúsculas",urlform="/forms/dma")

        return render_template("site.html",titulo="site",listadatos=listadatos,rutaid=rutaid)

if __name__ == '__main__':
    app.run("0.0.0.0",5000,debug=True)