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
        dbform = request.form.get("formdb")

        try:
            connection = psycopg2.connect(
            host="192.168.50.31",
            database=f"{dbform}",
            user=f"{usernameform}",
            password=f"{passform}"
            )
            print("Conexión realizada")
#            cursor=connection.cursor()       
#            #cursor.execute(f"select username from users where username='{usernameform}' and password=md5('{passform}')")
#            cursor.execute("select * from users;")
#            row=cursor.fetchall()
#            for rows in row:
#                listadatos.append(rows)
        except Exception as ex:
            #print(ex)
            return render_template("login.html",titulo="Login",errormesaje="usuario, contraseña o base de datos incorrecta")
        finally:
            connection.close()
            print("Conexión finalizada.")
    
        tabladept = []

        tablaemp = []

        
        rutaid = "/dma/"

        try:
            connection = psycopg2.connect(
            host="192.168.50.31",
            database=f"{dbform}",
            user=f"{usernameform}",
            password=f"{passform}"
            )
            print("Conexión realizada")
            cursor=connection.cursor()
            if dbform == 'scott':

                cursor.execute("select * from dept;")
                row=cursor.fetchall()
                for rows in row:
                    tabladept.append(rows)

                cursor.execute("select * from emp;")
                row=cursor.fetchall()
                for rows in row:
                    tablaemp.append(rows)

                #cursor.execute(f"select username,nombre,horas_semanales,profesor from users,modulos,matriculaciones where matriculaciones.alumnos=users.id and matriculaciones.modulos=modulos.nombre and users.username='{usernameform}'")
                #cursor.execute(f"select username,nombre,horas_semanales,profesor from users,modulos,matriculaciones where matriculaciones.alumnos=users.id and matriculaciones.modulos=modulos.nombre")
                #row=cursor.fetchall()
                #for rows in row:
                #    listadatos.append(rows)
                #nombre= listadatos[0][0]
        except Exception as ex:
            print(ex)
        finally:
            connection.close()
            print("Conexión finalizada.")

        if len(tablausers) == 0 or len(tablamod) == 0 or len(tablamat) == 0:
            return render_template("error404.html",titulo="Error404",titulo2="Error404",errormesaje="Error")

        return render_template("site.html",titulo="site",tabladept=tabladept,tablaemp=tablaemp,rutaid=rutaid,nombre=nombre)

if __name__ == '__main__':
    app.run("0.0.0.0",5000,debug=True)