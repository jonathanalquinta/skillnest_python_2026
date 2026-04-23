#Evaluacion python funcioness intermedias
# 1. Cambiar el puntaje de Pedro a 75

datos = [
   {"nombre": "Carlos", "puntaje": 80},
   {"nombre": "María", "puntaje": 95},
   {"nombre": "Pedro", "puntaje": 70}
]

print(datos[2]["nombre"])
datos[2]["puntaje"] = 75
print(datos[2]["puntaje"])

# 2. Crear función que imprima:

def dato_carlos():
    for i in datos:
     print(f"{datos[0]['nombre']} obtuvo {datos[0]['puntaje']} puntos")
     break
dato_carlos()

# 3. Crear función que reciba "nombre" o "puntaje" e imprima solo esos valores

def tomar_dato(nombre):
    ingresar = input("Ingresa el dato:")
    for i in datos:
        if  ingresar == i["nombre"]:
            print(f"{i['nombre']} obtuvo {i['puntaje']} puntos")
tomar_dato("nombre")