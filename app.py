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
        validation = "0"
        usernameform = request.form.get("formusername")
        passform = request.form.get("formpass")
        dbform = request.form.get("formdb")

        while usernameform != 'scott' and  usernameform != 'appwebuser' and  usernameform != 'postgres':
            return render_template("login.html",titulo="Login",errormesaje="El usuario no existe")
        
        while validation == "0":
            
            if usernameform == 'scott' and passform == 'tigger' and dbform == 'scott':
                validation = "1"
                print('Error1')
            elif usernameform == 'appwebuser' and passform == 'appwebpass' and dbform == 'appweb-db':
                validation = "1"
                print('Error2')
            elif usernameform == 'postgres' and passform == 'postgres' and dbform == 'scott' or dbform == 'appweb-db':
                validation = "1"
                print('Error3')
            else:
                return render_template("login.html",titulo="Login",errormesaje="usuario, contraseña o base de datos incorrecta")

        try:
            connection = psycopg2.connect(
            host="192.168.50.31",
            database=f"{dbform}",
            user=f"{usernameform}",
            password=f"{passform}"
            )
            
connection = psycopg2.connect(host="192.168.50.31", database=f"{scott}", user=f"{scott}",password=f"{tigger}")

            print("Conexión realizada")
        except Exception as ex:
            #print(ex)
            return render_template("login.html",titulo="Login",errormesaje="usuario, contraseña o base de datos incorrecta")
        finally:
            connection.close()
            print("Conexión finalizada.")
    
        tabladept = []

        tablaemp = []

        tablausr = []

        tablamat = []

        tablamod = []

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

                if len(tabladept) == 0 or len(tablaemp) == 0:
                    return render_template("error404.html",titulo="Error404",titulo2="Error404",errormesaje="Error")

                return render_template("site-scott.html",titulo="scott",tabladept=tabladept,tablaemp=tablaemp,rutaid=rutaid)

            elif dbform == 'appweb-db':

                cursor.execute("select * from users;")
                row=cursor.fetchall()
                for rows in row:
                    tablausr.append(rows)

                cursor.execute("select * from modulos;")
                row=cursor.fetchall()
                for rows in row:
                    tablamod.append(rows)
            
                cursor.execute("select * from matriculaciones;")
                row=cursor.fetchall()
                for rows in row:
                    tablamat.append(rows)

                if len(tablausr) == 0 or len(tablamod) == 0 or len(tablamat) == 0:
                    return render_template("error404.html",titulo="Error404",titulo2="Error404",errormesaje="Error")

                return render_template("site-appweb.html",titulo="appweb",tablausr=tablausr,tablamat=tablamat,tablamod=tablamod,rutaid=rutaid)
        except Exception as ex:
            print(ex)
        finally:
            connection.close()
            print("Conexión finalizada.")

if __name__ == '__main__':
    app.run("0.0.0.0",5000,debug=True)