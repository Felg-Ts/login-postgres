#Librerías
from flask import Flask,render_template,request
import psycopg2

app = Flask(__name__)	

#Formulario inicio de la aplicación

@app.route('/',methods=["GET"])
def inicio():
    return render_template("login.html",titulo="Login",errormesaje=" ")

#Página despues de inicio.

@app.route('/form/<appd>',methods=["POST"])
def ids(appd):

    if appd == "log":
        
        listadatos = []
        usernameform = request.form.get("formusername")
        passform = request.form.get("formpass")

        try:
            connection = psycopg2.connect(
            host="192.168.50.45",
            database="appweb-db",
            user="appwebuser",
            password="appwebpass"
            )
            print("Conexión realizada")
            cursor=connection.cursor()        
            cursor.execute(f"select * from users where username='{usernameform}' and password='{passform}'")
            row=cursor.fetchall()
            for rows in row:
                listadatos.append(rows)
        except Exception as ex:
            print(ex)
        finally:
            connection.close()
            print("Conexión finalizada.")
    
        if len(listadatos) == 0:
                return render_template("login.html",titulo="Login",errormesaje="usuario o contraseña incorrecto")

        else:
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
                cursor.execute(f"select username,nombre,horas_semanales,profesor from users,modulos,matriculaciones where matriculaciones.alumnos=users.id and matriculaciones.modulos=modulos.nombre and users.username={usernameform}")
                row=cursor.fetchall()
                for rows in row:
                    listadatos.append(rows)
                nombre= listadatos[0][0]
            except Exception as ex:
                print(ex)
            finally:
                connection.close()
                print("Conexión finalizada.")

            if len(listadatos) == 0:
                return render_template("error404.html",titulo="Error404",titulo2="Error404",errormesaje="Los caracteres introducidos no coinciden con ningún nombre. Recuerde que la primera letra de la ciudad tiene que ser en mayúsculas",urlform="/forms/dma")

            return render_template("site.html",titulo="site",listadatos=listadatos,rutaid=rutaid,nombre=nombre)

if __name__ == '__main__':
    app.run("0.0.0.0",5000,debug=True)