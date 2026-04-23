"""
Funciones básicas 1.
"""

# 1. Función que retorna la cantidad de logros desbloqueados en un videojuego.
def total_logros_desbloqueados():
    return 7

print(total_logros_desbloqueados())

#variables / valores

#salidas: 7
# 2. Función que indica la cantidad de mensajes enviados en un grupo de chat de tu juego online.
def mensajes_en_chat():
    return 2450

#variables / valores

#salidas: 2450

# 3. Intentamos sumar el resultado de una función que no existe al de 'mensajes_en_chat'.
def cantidad_de_dias_en_el_anio():
 print(cantidad_de_dias_en_el_anio() + mensajes_en_chat())


# Función que podría retornar la temporada en que alcanzaste un rango especial en un MOBA (por ejemplo, 2022 o 2021).
def temporada_rango_especial():
    return 2022
    return 2021  # ¿Se llega a ejecutar esta línea?

print(temporada_rango_especial())

#variables / valores

#print no se ejecuta ya que no está definido
#salidas: 2022
#return 2021 no se ejecuta ya que es inaccesible

# 4. Cantidad de listas de reproducción que sigues en una plataforma de música.
# Observa que la función 'retorna' 12, pero hay un print(15) después. ¿Se ejecuta?
def total_playlists():
    return 12
    print(15)

print(total_playlists())

#variables / valores

#salidas: 12
#print no se ejecuta, ya que no esta definido 


# 5. Función que muestra el número de episodios vistos de tu serie favorita,
# pero únicamente imprime su valor, sin retornarlo.
def episodios_serie_favorita():
    print(24)

x = episodios_serie_favorita()
print(x)

# variables / valores
# x         / None 
# salidas: 24

# 6. Función que "suma" los puntos obtenidos al compartir y al dar 'like' en una red social.
# Pero la función utiliza print en lugar de return. ¿Cómo afecta eso si queremos combinar los resultados?
def suma_puntos(a, b):
    print(a + b)

print(suma_puntos(10, 5) + suma_puntos(4, 3))

# variables / valores
# a         / 10 - 4
# b         / 5 - 3
# Salida: 15 , 7
#La funcion genera error ya que no tiene return


# 7. Función para concatenar dos "tags" de redes sociales, aunque se concatenan en orden inverso.
def combinar_tags(tag1, tag2):
    return str(tag2) + str(tag1)

print(combinar_tags("#Verano", "#Diversión"))

#variables / valores
# tap1     / #Verano
# tap2     / #Diversion
# salida   #DiversionVerano

# 8. Supongamos que 'a' representa el conteo de reproducciones de un video viral.
# Dependiendo del valor, devuelve un número distinto (p. ej., un ID de categoría).
def conteo_reproducciones_video():
    a = 560000
    print(a)
    if a < 180000:
        return 33
    else:
        return 46
    return 21  # ¿Se alcanza a ejecutar?

print(conteo_reproducciones_video())

# variables / valores
# a         / 560000
# si es menor 180000
# salida: 33
# Si es mayor
#salida: 46
#return 21 no se ejecuta ya que esta inaccesible estructuralmente.


# 9. Duración de una suscripción premium: 365 días (si se cumplen ciertas condiciones) o 12 meses.
# El tercer 'return' (52 semanas) está después del else. ¿Lo veremos?
def duracion_suscripcion(a, b):
    if a < b:
        return 365
    else:
        return 12
    return 52

print(duracion_suscripcion(1, 3))
print(duracion_suscripcion(7, 4))
print(duracion_suscripcion(7, 4) + duracion_suscripcion(1, 3))

#variables / valores
# a        / 1 7 7
# b        / 3 4 4
#salidas: 365, 12, 377 
# return 52 no se ejecuta ya que esta inaccesible estructuralmente.


# 10. Suma de propinas que recibes en un juego de simulación (p.ej. "Cafetería Virtual").
# Nota que hay dos return, pero el segundo no se ejecuta nunca.
def suma_propinas(a, b):
    return a + b
    return 157

print(suma_propinas(3, 4))

#variables / valores
# a        / 3
# b        / 4
#salida: 7
#return 157 no está accesible estructuralmente

# 11. Variable global que cuenta cuántas horas de juego llevas en total.
# Dentro de la función se define otra variable con el mismo nombre.
horas_de_juego = 150
print(horas_de_juego)

def mostrar_horas_local():
    horas_de_juego = 350
    print(horas_de_juego)

print(horas_de_juego)
mostrar_horas_local()
print(horas_de_juego)

#variables / valores
# hora de juego / 150 - 350
#salida: 150, 150, 350, 350

# 12. Similar al anterior, pero la función retorna el valor local 'horas_de_juego'.
horas_de_juego = 150
print(horas_de_juego)

def mostrar_horas_local():
    horas_de_juego = 350
    print(horas_de_juego)
    return horas_de_juego

print(horas_de_juego)
mostrar_horas_local()
print(horas_de_juego)

# variables / valoress

# hora de juego / 150 - 350
#salida: 150, 150,350, 350, 350


# 13. Ahora reasignamos la variable global con el valor que retorna la función.
horas_de_juego = 150
print(horas_de_juego)

def mostrar_horas_local():
    horas_de_juego = 350
    print(horas_de_juego)
    return horas_de_juego

print(horas_de_juego)
horas_de_juego = mostrar_horas_local()
print(horas_de_juego)

# variables / valoress


# hora de juego / 150 - 350
#salida: 150, 350, 150, 350, 150, none, 150


# 14. Una función que primero muestra la cantidad de seguidores en tu canal, luego llama a otra función para mostrar "Likes".
def mostrar_seguidores():
    print("Seguidores: 300")
    mostrar_likes()
    print("Finalizando conteo")

def mostrar_likes():
    print("Likes: 120")

mostrar_seguidores()

# variables / valoress

# Salida: seguidores: 300, finalizando conteo, likes: 120


# 15. Función que muestra "Reproducciones" de un tema musical y recibe un valor de otra función,
# luego retorna un número que podría ser un "ID" final de procesamiento.
def mostrar_reproducciones():
    print("Reproducciones: 5000")
    a = calcular_incremento()
    print(a)
    return 4

def calcular_incremento():
    print("Incremento calculado: ")
    return 1

b = mostrar_reproducciones()
print(b)

# variables / valores
# a         / # 1
# b         / # 4

# Salida:  reproducciones 5000