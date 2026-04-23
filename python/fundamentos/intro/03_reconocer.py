"""
Este archivo demuestra varios conceptos básicos en Python.
Completa los comentarios en cada línea para relacionarlos
con los conceptos enumerados en 'reconocer.md'.
"""


import random #importacion de libreria para procesos Aleatorias


nombre = "Frida Kahlo" #Creacion de una variable tipo string y se asigna un valor.
print(type(nombre)) #Type() = metodo para mostrar el tipo de una variable.
print(len(nombre)) #len() = devuelve el largo de una variable.


edad = 25 #Creacion de variable tipo numerico (Tipo int).


if edad < 18: #Se establece condicional if .
   print("Eres menor de edad.") #Imprime mensaje.
elif edad == 18: #Se estanlece subcondicion elif(else if).
   print("Tienes 18 años.") #Imprime mensaje.
else: #Cierre de condicion (Si no se cumplen las anteriores).
   print("Eres mayor de edad.") #Imprime mensaje.


frutas = ["manzana", "pera", "fresa"] #Se crea un Array con valores ya registrados.
print(frutas[0]) #Mostramos la primera posicion del arreglo.
frutas[0] = "banana" #A la posicion 0 del arreglo se le entrega el valor de "banana".
frutas.append("uva") #Se le agrega "uva" al final del Arreglo.
frutas.remove("pera") #Se remueve "pera" del Arreglo.


dimensiones = (200, 50) #Creamos una variable tipo tupla (variable inmutable).
print(dimensiones[0]) #Imprime la posicion 0 de la variable creada.


persona = { #Variable tipo object (va con llaves{}).
   "nombre": "Carlos", #Se establece un item y su respectivo valor.
   "edad": 30 #Se establece un item y su respectivo valor.
}
print(persona["nombre"]) #Imprime el valor del item (ej: "Carlos").
persona["edad"] = 31 #Se modifica el valor del item edad a 31.
persona["ciudad"] = "Santiago" #Se agrega un nuevo item con un valor.
del persona["ciudad"] #Se elimina el item completo.


for i in range(5): #For range: Se crea bucle en rango desde 0 a 5.
   if i == 2: #Se establece condicion if == 2.
       continue #Continue ignora el proceso y continua.
   if i == 4: #Se establece condicion if i == 4.
       break #Si i = 4 se romple el bucle.
   print(i) #Imprime valor de i en cada iteracion.(hasta 4).


contador = 0 #Se crea una variable Contador tipo numerica(int).
while contador < 3: #Se crea bucle While con una condición.
   print(f"while contador es: {contador}") #Imprime el contador en un mensaje concatenado con f"" string. 
   contador += 1 #Incrementa el valor en 1 en cada iteracion.


def saludar_usuario(nombre): #Def- Palabra reservada para crear una funcion.
   return f"Hola, {nombre}" #Devuelve un valor de la funcion.



print(saludar_usuario("Francisca")) #Se imprime "Hola Francisca" - return de la funcion.