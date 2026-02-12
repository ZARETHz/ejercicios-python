partidas = [
    ("Alex", "Bosque", 120),
    ("Luis", "Desierto", 90),
    ("Alex", "Bosque", 150),
    ("Ana", "Ciudad", 200),
    ("Luis", "Bosque", 110)
]

puntos_jugador = {}    
conteo_jugador = {}    
uso_mapas = {}         
mapas_jugados = set()  

for registro in partidas:
    jugador = registro[0]
    mapa = registro[1]
    puntos = registro[2]

    if jugador not in puntos_jugador:
        puntos_jugador[jugador] = 0
    puntos_jugador[jugador] += puntos

    if jugador not in conteo_jugador:
        conteo_jugador[jugador] = 0
    conteo_jugador[jugador] += 1

    if mapa not in uso_mapas:
        uso_mapas[mapa] = 0
    uso_mapas[mapa] += 1


    mapas_jugados.add(mapa)


print(f"Puntos totales por jugador: {puntos_jugador}")
print(f"Mapas únicos jugados: {mapas_jugados}")


promedios = {}
for jugador in puntos_jugador:
    total_puntos = puntos_jugador[jugador]
    total_partidas = conteo_jugador[jugador]
    promedios[jugador] = total_puntos / total_partidas

print(f"Promedio por jugador: {promedios}")

mayor_uso = 0
mapa_ganador = ""

for mapa in uso_mapas:
    cantidad = uso_mapas[mapa]
    if cantidad > mayor_uso:
        mayor_uso = cantidad
        mapa_ganador = mapa

print(f"El mapa más usado fue: {mapa_ganador}")