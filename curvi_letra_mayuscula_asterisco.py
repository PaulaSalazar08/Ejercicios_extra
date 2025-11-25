#Escriba un programa contenga una función llamada curvi(letra_mayuscula). Curvi recibe
#una letra mayúscula y devuelve 0 si la letra no contiene curvas y 1 si las contiene. Por
#ejemplo A no contiene curvas pero B si las contiene. Incluya la letra Ñ. Si la letra es
#minúscula devuelve siempre 0.

#Cuando nos piden una función nos piden otra función a parte.
def curvi(letra):
    respuesta=0
    lista_curvi="BCDGJÑOPQRSU"
    if(letra in lista_curvi):
        respuesta=1
    return(respuesta)

def programa_2():
    palabra=raw_input("Introduce una palabra: ")
    palabra_asteriscos=""
    longitud=len(palabra)
    suma=0
    cont=0
    for cont in range(0,longitud):
        suma=suma+curvi(palabra[cont])
        if(curvi(palabra[cont])==1):
            palabra_asteriscos=palabra_asteriscos+"*"
        else:
            palabra_asteriscos=palabra_asteriscos+palabra[cont]
    print("La palabra "+palabra+" tiene "+str(suma)+" letras curvis")
    print("Palabra modificada: "+palabra_asteriscos)

programa_2()
