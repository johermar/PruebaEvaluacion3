import random

# Nombres de algunas naves espaciales
nombres_naves = [
    "Cometa Veloz", "Titán del Cosmos", "GX Marauder",
    "Estrella Errante", "GX Voyager", "Vagabundo Estelar", "Explorador del Abismo"
]

# Generar la lista de naves con características aleatorias
naves = [
    {"nombre": nombre,
        "longitud": random.randint(100, 400),  # Longitud entre 100 y 400
        "tripulantes": random.randint(10, 30),  # Tripulantes entre 10 y 30
        "pasajeros": random.randint(200, 700)   # Pasajeros entre 200 y 700
    } for nombre in nombres_naves
]

# Tareas:

# 1. Ordenar por nombre (ascendente) y luego por longitud (descendente)
naves_ordenadas = sorted(naves, key=lambda x: (x['nombre'], -x['longitud']))

# 2. Mostrar información de "Cometa Veloz" y "Titán del Cosmos"
naves_filtradas = [nave for nave in naves if nave['nombre'] in ["Cometa Veloz", "Titán del Cosmos"]]
print("Información de Cometa Veloz y Titán del Cosmos:")
for nave in naves_filtradas:
    print(nave)

# 3. Cinco naves con mayor cantidad de pasajeros
top_cinco_pasajeros = sorted(naves, key=lambda x: -x['pasajeros'])[:5]
print("\nCinco naves con mayor cantidad de pasajeros:")
for nave in top_cinco_pasajeros:
    print(nave['nombre'], "con", nave['pasajeros'], "pasajeros")

# 4. Nave con mayor cantidad de tripulación
max_tripulacion = max(naves, key=lambda x: x['tripulantes'])
print("\nNave con mayor cantidad de tripulación:", max_tripulacion['nombre'])

# 5. Naves que comienzan con "GX"
gx_naves = [nave for nave in naves if nave['nombre'].startswith("GX")]
print("\nNaves que comienzan con 'GX':")
for nave in gx_naves:
    print(nave['nombre'])

# 6. Naves para seis o más pasajeros
seis_mas_pasajeros = [nave for nave in naves if nave['pasajeros'] >= 6]
print("\nNaves para seis o más pasajeros:")
for nave in seis_mas_pasajeros:
    print(nave['nombre'])

# 7. La nave más pequeña y la más grande
nave_mas_pequena = min(naves, key=lambda x: x['longitud'])
nave_mas_grande = max(naves, key=lambda x: x['longitud'])
print("\nNave más pequeña:", nave_mas_pequena['nombre'], "Longitud:", nave_mas_pequena['longitud'])
print("Nave más grande:", nave_mas_grande['nombre'], "Longitud:", nave_mas_grande['longitud'])