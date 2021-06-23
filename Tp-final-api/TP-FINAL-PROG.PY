import requests
#import json


def get_weather_city(ruta,parametros):
    req = requests.get(url=ruta,params=parametros)
    if req.status_code == 200:
        dic = req.json()
        return dic
    else:
        print('Error')




#Menu de aplicacion

opcion=''
while opcion!= 'MENU':
    print('Ingrese 1 para saber los datos actuales de la ciudad que desee')
    print('Ingrese 2 para saber los datos actuales segun sus coordenadas')
    print('Ingrese 3 para saber los datos de los proximos 4 dias de la ciudad que desee')
    print('Ingrese 4 para saber los datos de los proximos 4 dias ingresando coordenadas')
    print('Ingrese 0 para terminar')


    opcion = input('seleccione su opcion: ')


#Comienzo de aplicacion -OPCION 1-

    if(opcion == '1'):
        city= print('----Usted a elegido la opcion 1----')
        city = input('Porfavor, ingrese el nombre de la ciudad: ')

        parametros = {}
        parametros['q'] = city
        parametros['units'] = 'metric'
        parametros['lang'] = 'sv, se'
        parametros['appid'] = '0098d105da59cbba6bb5c81a767258af'

        urlbase = 'https://api.openweathermap.org/data/2.5/weather'


        urlfinal = get_weather_city(urlbase,parametros)

        print(urlfinal['main'])

        print()

#-OPCION 2 - Coordenadas

    elif(opcion == '2'):
        Saludo= print('----Usted a elegido la opcion 2----')
        lat= input("Porfavor, ingrese la latitud: ")
        lon =  input("Porfavor, ingrese la longitud: ")
        params  = {}
        params["lat"] = lat
        params["lon"] = lon
        params["units"] = "metric"
        params["appid"] = "0098d105da59cbba6bb5c81a767258af"

        url_base= "http://api.openweathermap.org/data/2.5/weather"

        clima = get_weather_city(url_base,params)

        print(clima['name'],clima["main"])

        print()


 # -OPCION 3- Datos de 4 dias
    elif (opcion == '3' ):
        Saludo= print('----Usted a elegido la opcion 3----')
        ciudad = input("Porfavor, Ingrese el nombre de la ciudad deseada, para mostrarle los datos de los proximos 4 dias: ")
        params  = {}
        params["q"] = ciudad
        params["appid"] = "0098d105da59cbba6bb5c81a767258af"


        url = "https://api.openweathermap.org/data/2.5/forecast"

        clima = get_weather_city(url,params)
        #para generar un espacio
        print()
        

        fecha = clima["list"][2]["dt_txt"]
        datos = clima["list"][2]
        print("En el dia",fecha,'en',ciudad, "el tiempo sera:")
        #para generar un espacio
        print()

        print (datos)
        #para generar un espacio
        print()

        fecha = clima["list"][10]["dt_txt"]
        datos = clima["list"][10]
        print("En el dia",fecha,'en',ciudad, "el tiempo sera:")
        #para generar un espacio
        print()

        print (datos)
        #para generar un espacio
        print()
        fecha = clima["list"][18]["dt_txt"]
        datos = clima["list"][18]
        print("En el dia",fecha,'en',ciudad, "el tiempo sera:")
        #para generar un espacio
        print()

        print (datos)
        #para generar un espacio
        print()

        fecha = clima["list"][26]["dt_txt"]
        datos = clima["list"][26]
        print("En el dia",fecha,'en',ciudad, "el tiempo sera:")
        #para generar un espacio
        print()

        print (datos)
        #para generar un espacio
        print()

# -OPCION 4 - Coordenadas de 4 dias.
    elif(opcion == '4'):
        Saludo= print('----Usted a elegido la opcion 4----')
        lat= input("Porfavor, ingrese la latitud: ")
        lon=  input("Porfavor, ingrese la longitud: ")
        params  = {}
        params["lat"] = lat
        params["lon"] = lon
        params["units"] = "metric"
        params["appid"] = "0098d105da59cbba6bb5c81a767258af"

        url_base = "https://api.openweathermap.org/data/2.5/forecast"

        clima = get_weather_city(url_base,params)


        fecha = clima["list"][2]["dt_txt"]
        datos = clima["list"][2]

        print("En dia",fecha,' en la latitud',lat,' y en la lon',lon," el tiempo sera:")
        #para generar un espacio
        print()
        print (datos)
        #para generar un espacio
        print()
        fecha = clima["list"][10]["dt_txt"]
        datos = clima["list"][10]
        print()  #para generar un espacio
    

        print("En dia",fecha,' en la latitud',lat,' y en la lon',lon," el tiempo sera:")
        #para generar un espacio
        print()
        print (datos)
        #para generar un espacio
        print()

        fecha = clima["list"][18]["dt_txt"]
        datos = clima["list"][18]
        print()  #para generar un espacio

        print("En dia",fecha,' en la latitud',lat,' y en la lon',lon," el tiempo sera:")
        #para generar un espacio
        print()
        print (datos)
        #para generar un espacio
        print()

        fecha = clima["list"][26]["dt_txt"]
        datos = clima["list"][26]
        print()  #para generar un espacio

        print("En dia",fecha,' en la latitud',lat,' y en la lon',lon," el tiempo sera:")
        #para generar un espacio
        print()
        print (datos)
        print()  #para generar un espacio


# -OPCION 5 - FIN DEL PROGRAMA.
    elif(opcion == '0'):
        print('----Usted a elegido la opcion 0----')
        print('Gracias por usar nuestros servicios.')
        print('Vuelva pronto.')
        print('El programa a finalizado.')

        print()  #para generar un espacio

    else:
        print('La opcion seleccionada es incorrecta.')
        print('Porfavor seleccione nuevamente una opcion.')

        print()  #para generar un espacio
