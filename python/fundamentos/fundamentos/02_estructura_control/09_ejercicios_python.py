""" 1. Números Pares Dinámicos
Desarrolla un programa que solicite al usuario cuántos números pares desea ver ($n$). 
El programa debe imprimir los primeros $n$ números pares positivos."""

def numerosDinamicos():
   n = int(input("Cuantos pares deseas ver: "))
   pares = []
   for i in range (1, (n * 2) + 1):
    if i % 2 == 0:
      pares.append(i)
   print(f"Mostrando pares: {pares}")

""" 2. Verificador de Edad y Acceso
Pide al usuario su año de nacimiento. Calcula su edad y muestra si es mayor de edad (18+).
Si tiene menos de 18, indica cuántos años le faltan para la mayoría de edad. """

def verificarEdad():
 nacimiento = int(input("Ingrese su año de nacimiento: "))
 anio_actual = 2026
 calculo = anio_actual - nacimiento

 if calculo >= 18:
   print("Eres mayor de edad")
 else:
   faltan = 18 - calculo
   print("Eres menor de edad")
   print("Te faltan", faltan, "años para ser mayor de edad")

"""3. Calculadora de Descuentos
Solicita el precio de un producto y la cantidad comprada. Si el total supera los $100, 
aplica un 15% de descuento. Muestra el subtotal, el descuento aplicado y el total final."""

def aplicarDescuento():
 precio = float(input("Ingrese el precio solicitado del producto: "))
 cantidad = int(input("Ingrese la cantidad de productos que compró: "))
 producto = precio * cantidad

 if producto >= 100:
   descuento = producto * 0.15
 else:
   descuento = 0
   total = producto - descuento
   print(f"El subtotal es: ${producto}. el descuento aplicado es: ${descuento} y el total final es: ${total}")

# 4. Clasificador de Números
# Pide un número al usuario e indica si es: Positivo-Par, Positivo-Impar, Negativo-Par, 
# Negativo-Impar o Cero.

def clasificadorNum():
  num = int(input("Ingrese un número: "))
  if num > 0:
    if num % 2 == 0:
      print("Positivo-par")
    elif num % 2 == 1:
      print("Positivo-impar")

# II. Iteraciones y Bucles (Intermedio)

# 5. Tabla de Multiplicar Personalizada
# Solicita un número entero y muestra su tabla de multiplicar del 1 al 12, 
# pero solo muestra los resultados que sean múltiplos de 3.

def tablaMultiplicar():
  num = int(input("Ingrese número a trabajar: "))
  for i in range (1, 13):
    resultado = num * i
    if resultado % 3 == 0:
      print(f"Del {num} solo estos números son divisibles por 3: {resultado}")

# 6. Sumatoria con Centinela
# Crea un programa que pida números continuamente y los sume. El ciclo debe terminar cuando el
#  usuario ingrese un número negativo. Al final, muestra la suma total (sin incluir el negativo).
def sumaCentinela():
   suma_total = 0
   while True:
      n = float(input("Ingresarun numero (negativo para salir):"))
      if n < 0:
         break
      suma_total += n
      print(f"La suma total es: {suma_total}")

   

# 7. Contador de Vocales
# Pide al usuario una frase o palabra. Utiliza un bucle para recorrer la cadena y contar
#  cuántas vocales tiene en total.

def contadorVocales():
   texto = input("Ingresa una palabra").lower()
   vocales = 0
   for i in range(len(texto)):
      #repetir la condicion con cada vocal
      if texto[i] == "a" or texto[i] == "e" or texto[i] == "i" or texto[i] == "o" or texto[i] == "u":
         vocales += 1 
      elif texto[i] == "á" or texto[i] == "é" or texto[i] == "í" or texto[i] == "ó" or texto[i] == "ú":
         vocales += 1
   print(f"La cadena '{texto}' tiene {vocales} vocales en total")

# 8. Validación de Contraseña
# Define una contraseña en una variable. Pide al usuario que la intente adivinar
#  Tienes un máximo de 3 intentos; si falla los 3, bloquea el acceso.

def validarContraseña():
   contraseña = 14722
   intentos = 3
   while intentos >0:
      ingreso = int(input("adivine la contraseña"))
      
      if ingreso == contraseña:
         print("Acceso concedido")
         break
      else:
         intentos -=1
         
         if intentos == 2:
            print("Contarseña incorrecta (Quedan 2 intentos...)")
         elif intentos == 1:
            print("Contarseña incorrecta (Quedan 1 intentos...)")
         else:
            print("Contarseña Incorrecta (Acceso bloqueado)")

# III. Manejo de Arreglos / Listas (Avanzado)

# 9. Registro de Nombres
# Crea un arreglo vacío. Pide al usuario que ingrese 5 nombres. Guárdalos en el arreglo y, 
# al final, imprímelos en orden inverso al que fueron ingresados.

def registroNombres():
   nombres = []
   maxi = 0
   
   while maxi < 5:
      inp = input(f"")

# 10. Promedio de Notas
# Solicita al usuario cuántas notas desea ingresar. Almacena cada nota en un arreglo. 
# Al finalizar, calcula y muestra el promedio, la nota más alta y la más baja.

def promedioNotas():
   cantidad = int(input("Ingresa notas"))
   notas = []
   for i in range(cantidad):
      nota = float(input(f"Nota {i+1}:"))
      notas.append(nota)
      
      promedio = sum(notas) / len(notas)
      print(f"Promedio: {promedio}")
      print(f"Nota mas alta: {max(notas)}")
      print(f"Nota mas baja: {min(notas)}")
   

# 11. Filtro de Arreglos
# Dado un arreglo de números generado por el usuario, crea un nuevo arreglo que 
# contenga solo los números que sean mayores a 50. Muestra ambos arreglos.

def flitroArreglo():
   cantidad = int(input("Cuantos números desea ingresar"))
   mayor50 = []
   nUser = []
   for i in range (1, cantidad):
      arrayUsuario = int(input("Ingrese un número"))
      nUser = arrayUsuario
      if arrayUsuario > 50:
         mayor50.append(arrayUsuario)
         print(f"Valores:ingresados por el usuario: {arrayUsuario} \nvalores mayor a")

# 12. Buscador de Elementos
# Crea una lista de 10 ciudades. Pide al usuario que ingrese el nombre de una 
# ciudad y el programa debe decir si la ciudad se encuentra en la lista y en qué índice (posición) está.

def buscarElemntos():
   ciudades = ["Santiago, Buenos Aires, Madrid, Cancún, Berlin, Tokyo, Moscú, Seattle, Barcelona, Sidney"]
   ciudad = input("Ingresar Ciudad (Con mayuscula al principio):")
   esta = ciudades.index(ciudad)
   if esta < len(ciudades):
      print(f"Tu ciudad está en el arreglo , en la posicion {esta}")
   else:
      print("Tu ciudad no está en el arreglo")

# IV. Retos de Lógica Combinada

# 13. Simulación de Inventario
# Crea dos arreglos: uno para nombres_productos y otro para precios. Permite al usuario ingresar
#  3 productos con sus precios. Luego, 
# muestra una lista formateada: Producto: [Nombre] - Precio: $[Valor].

def inventario():
   nombres_productos = []
   precio = float(input("Precio:"))
   nombres_productos.append(precio)
   print("\ninventario:")
   for i in range(3):
    print(f"Producto: {nombres_productos[i]} - Precio {precio[i]}")

# 14. Generador de Lista de Compras
# Usa un bucle while para que el usuario agregue artículos a una lista de compras. 
# El proceso termina cuando el usuario escribe "terminar". Al final, muestra la lista
#  ordenada alfabéticamente.

def listaCompras():
   lista = []
   while True:
      item = input("Articulo (o'terminar')")
      if item.lower() == "terminar":
         break
      lista.append(item)
   print(f"Ordenanda: {sorted(lista)}") 

# 15. Análisis de Temperaturas
# Solicita las temperaturas de los 7 días de la semana y guárdalas en un arreglo. Muestra:
# El promedio semanal.
# Cuántos días la temperatura fue superior a 25 grados.
# El día con la temperatura más baja (asumiendo que el índice 0 es Lunes).

def analisisTemperatura():
   dias = ["Lunes", "Marte", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
   diasSuperior = []
   total = 0
   baja = 100
   diaBaja = ""
   cant = 0
   
   while cant < 7:
      temps = float(input("Ingrese tempertura del dia {dia[cant]}:"))
      total += temps
      
      if temps < baja and temps < 25:
         baja = temps
         diaBaja = dias[cant]
      elif temps > 25:
         diasSuperior.append(dias[cant])
         
      cant += 1

continuar = True
while continuar:
   print("\n --- Ejercicios Python ---")
   print("\n --- 1- Ejercicios ---")
   print("\n --- 2- Ejercicios ---")
   print("\n --- 3- Ejercicios ---")
   print("\n --- 4- Ejercicios ---")
   print("\n --- 5- Ejercicios ---")
   print("\n --- 6- Ejercicios ---")
   print("\n --- 7- Ejercicios ---")
   print("\n --- 8- Ejercicios ---")
   print("\n --- 9- Ejercicios ---")
   print("\n --- 10- Ejercicios ---")
   print("\n --- 11- Ejercicios ---")
   print("\n --- 12- Ejercicios ---")
   print("\n --- 13- Ejercicios ---")
   print("\n --- 14- Ejercicios ---")
   print("\n --- 15- Ejercicios ---")

   opcion = input("\n ---- Elige una opción: (1-15) (0 para salir)")
   if opcion == "1":
      print("\nEjecutando ejercicio 1:")
      numerosDinamicos()
   elif opcion == "2":
      print("\nEjecutando ejercicio 2:")
      verificarEdad()
   elif opcion == "3":
      print("\nEjecutando ejercicio 3:")
      aplicarDescuento()
   elif opcion == "4":
      print("\nEjecutando ejercicio 4:")
      clasificadorNum()
   elif opcion == "5":
      print("\nEjecutando ejercicio 5:")
      tablaMultiplicar()
   elif opcion == "6":
      print("\nEjecutando ejercicio 6:")
      sumaCentinela()
   elif opcion == "7":
      print("\nEjecutando ejercicio 7:")
      contadorVocales()
   elif opcion == "8":
      print("\nEjecutando ejercicio 8:")
      validarContraseña()
   elif opcion == "9":
      print("\nEjecutando ejercicio 9:")
      registroNombres()
   elif opcion == "10":
      print("\nEjecutando ejercicio 10:")
      promedioNotas()
   elif opcion == "11":
      print("\nEjecutando ejercicio 11:")
      flitroArreglo()
   elif opcion == "12":
      print("\nEjecutando ejercicio 12:")
      buscarElemntos()
   elif opcion == "13":
      print("\nEjecutando ejercicio 13:")
      inventario()
   elif opcion == "14":
      print("\nEjecutando ejercicio 14:")
      listaCompras()
   elif opcion == "15":
      print("\nEjecutando ejercicio 15:")
      analisisTemperatura()
   elif opcion == "0":
      print("Saliendo...")
      continuar = False