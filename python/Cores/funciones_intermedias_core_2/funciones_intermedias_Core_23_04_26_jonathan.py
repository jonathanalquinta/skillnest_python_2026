# Ranking de puntajes de un torneo de eSports
puntajes = [ [1000, 1500, 2000], [300, 700, 1400] ]
#cambio puntajes


# Lista de creadores de contenido en una plataforma de streaming
streamers = [
   {"nombre": "GameNinjaPro", "seguidores": 250000},
   {"nombre": "PixelWarrior", "seguidores": 180000}
]


# Eventos en distintas ciudades del mundo
eventos = {
   "Estados Unidos": ["Los Ángeles", "Nueva York", "Las Vegas"],
   "España": ["Madrid", "Barcelona", "Valencia"]
}


# Coordenadas de la sede de un torneo internacional
ubicacion = [
   {"latitud": 34.052235, "longitud": -118.243683}
]

# cambio puntajes
puntajes[1][0] = 600
print(puntajes)

# en streamers cambio de nombre de GamerNinjaPro
streamers[0]["nombre"] = "EliteGamerX"
print(streamers)

#cambio de ciudades
eventos["Estados Unidos"][2] = "San francisco"
print(eventos)

# cambio de la sede de un torneo internacional
ubicacion[0]["latitud"] = 40.712776
print(ubicacion)

#Funciones para recorrer y representar datos
def iterar_diccionario(lista):
    for diccionario in lista:
         salida = ", ".join(f"{clave}: {valor}" for clave, valor in diccionario.items())
         print(salida)
iterar_diccionario(streamers)

def tomar_valores(clave, lista):
    for diccionario in lista:
        if clave in diccionario:
            print(diccionario[clave])
tomar_valores("nombre", streamers)
tomar_valores("seguidores", streamers)


def ver_informacion(diccionario):
    for clave, lista in diccionario.items():
        print(f"{len(lista)} {clave.upper()}")
        for elemento in lista:
            print(elemento)
categoria = {
    "juegos_populares": ["Fortnite", "Minecraft", "Valorant", "GTA V"],
    "ciudades_eventos": ["Nueva York", "Madrid", "Tokio"]}
ver_informacion(categoria)
print(categoria)