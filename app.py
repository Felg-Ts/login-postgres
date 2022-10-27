#Librerías
from flask import Flask, request,render_template
import connection

app = Flask(__name__)	

#inicio de la aplicación

@app.route('/',methods=["GET"])
def inicio():
    return render_template("inicio.html",titulo="Inicio")

#Formularios para los 3 programas.

@app.route('/forms/<appd>',methods=["GET"])
def forms(appd):
    if appd == "dma":
        titulo = "Formulario de Current weather data"
        ruta = "/ids/dma"
        texto = "Nombre-de-una-ciudad"
        titulo2 = "Formulario de Current weather data"
        getform = "tdma"
    return render_template("forms.html",titulo=titulo,titulo2=titulo2,ruta=ruta,texto=texto,getform=getform)

#Resultados de los formualarios 1 y 2.

@app.route('/ids/<appd>',methods=["Post"])
def ids(appd):

# Pruebas

    if appd == "dma":

        listadatos = []

        rutaid = "/dma/"
        titulo = "Current weather data"
        titulo2 = "Current weather data"

        connection.cursor.execute("select * from users")
        connection.rows=connection.cursor.fetchall()
        for row in connection.rows:
            print (row)

        if len(connection.rows) == 0:
            return render_template("error404.html",titulo="Error404",titulo2="Error404",errormesaje="Los caracteres introducidos no coinciden con ningún nombre. Recuerde que la primera letra de la ciudad tiene que ser en mayúsculas",urlform="/forms/dma")

        return render_template("ids.html",titulo=titulo,titulo2=titulo2,rows=listadatos,rutaid=rutaid)

#Resultado programa 1

@app.route('/dma/<int:id>',methods=["GET"])
def dma(id):

    listadatos = []

    titulo = "Current weather data"
    titulo2 = "Current weather data"

    url = "https://api.openweathermap.org/data/2.5/weather"
    querystring = {"id":f"{id}","appid":"5a74fb5df668d605eaef2012ed31eed8","units":"metric","lang":"38"}
    headers = {
        'Cache-Control': 'no-cache'
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    if response.status_code==200:
        datos=response.json()
        listadatos.append(datos)

    if len(listadatos) == 0:
        return render_template("error404.html",titulo="Error404",titulo2="Error404",errormesaje="El id introducido no coincide con ninguna ciudad. Compruebe que está escrito correctamente",urlform="/forms/dma")
    
    return render_template("Current-weather-data.html",titulo=titulo,titulo2=titulo2,listadatos=listadatos)


if __name__ == '__main__':
    app.run("0.0.0.0",5000,debug=True)