import random
import time

# Parámetros
CANTIDAD = 10_000_000
MIN = -50_000_000
MAX = 50_000_000
ARCHIVO = "numeros.txt"

print("Generando números...")

inicio = time.time()

with open(ARCHIVO, "w") as f:
    for _ in range(CANTIDAD):
        numero = random.randint(MIN, MAX)
        f.write(str(numero) + "\n")

fin = time.time()

print("Proceso terminado.")
print("Tiempo total:", round(fin - inicio, 2), "segundos")

print("\nCargando datos en memoria...")

inicio_carga = time.time()

lista_numeros = []

with open(ARCHIVO, "r") as f:
    for linea in f:
        lista_numeros.append(int(linea.strip()))

fin_carga = time.time()

print("Carga completada.")
print("Tiempo de carga:", round(fin_carga - inicio_carga, 2), "segundos")
print("Cantidad de elementos cargados:", len(lista_numeros))
print("\nOrdenando lista...")

inicio_orden = time.time()

lista_ordenada = sorted(lista_numeros)

fin_orden = time.time()

print("Lista ordenada.")
print("Tiempo de ordenamiento:", round(fin_orden - inicio_orden, 2), "segundos")

print("\nCreando tabla hash (diccionario)...")

inicio_hash = time.time()

tabla_hash = {numero: True for numero in lista_numeros}

fin_hash = time.time()

print("Tabla hash creada.")
print("Tiempo de creación:", round(fin_hash - inicio_hash, 2), "segundos")

print("\n--- BÚSQUEDA LINEAL ---")

numero_buscar = int(input("Ingrese un número a buscar: "))

inicio_busqueda = time.time()

encontrado = False

for num in lista_numeros:
    if num == numero_buscar:
        encontrado = True
        break

fin_busqueda = time.time()

if encontrado:
    print("Número encontrado.")
else:
    print("Número NO encontrado.")

print("Tiempo de búsqueda:", round(fin_busqueda - inicio_busqueda, 6), "segundos")

print("\n--- BÚSQUEDA BINARIA ---")

numero_buscar = int(input("Ingrese un número a buscar: "))

inicio_binaria = time.time()

izquierda = 0
derecha = len(lista_ordenada) - 1
encontrado_binaria = False

while izquierda <= derecha:
    medio = (izquierda + derecha) // 2
    
    if lista_ordenada[medio] == numero_buscar:
        encontrado_binaria = True
        break
    elif lista_ordenada[medio] < numero_buscar:
        izquierda = medio + 1
    else:
        derecha = medio - 1

fin_binaria = time.time()

if encontrado_binaria:
    print("Número encontrado.")
else:
    print("Número NO encontrado.")

print("Tiempo búsqueda binaria:", round(fin_binaria - inicio_binaria, 6), "segundos")
print("\n--- BÚSQUEDA HASH ---")

numero_buscar = int(input("Ingrese un número a buscar: "))

inicio_hash_busqueda = time.time()

if numero_buscar in tabla_hash:
    print("Número encontrado.")
else:
    print("Número NO encontrado.")

fin_hash_busqueda = time.time()

print("Tiempo búsqueda hash:", round(fin_hash_busqueda - inicio_hash_busqueda, 6), "segundos")

print("\nEjecutando 1000 búsquedas automáticas (Lineal)...")

inicio = time.time()

for _ in range(1000):
    objetivo = random.randint(MIN, MAX)
    for num in lista_numeros:
        if num == objetivo:
            break

fin = time.time()

promedio_lineal = (fin - inicio) / 1000

print("Ejecutando 1000 búsquedas automáticas (Binaria)...")

inicio = time.time()

for _ in range(1000):
    objetivo = random.randint(MIN, MAX)
    
    izquierda = 0
    derecha = len(lista_ordenada) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        if lista_ordenada[medio] == objetivo:
            break
        elif lista_ordenada[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

fin = time.time()

promedio_binaria = (fin - inicio) / 1000

print("Ejecutando 1000 búsquedas automáticas (Hash)...")

inicio = time.time()

for _ in range(1000):
    objetivo = random.randint(MIN, MAX)
    _ = objetivo in tabla_hash

fin = time.time()

promedio_hash = (fin - inicio) / 1000

print("\n--- TABLA COMPARATIVA ---")

print(f"{'Estructura':<20}{'Tiempo Promedio (s)':<25}{'Complejidad'}")
print("-" * 60)
print(f"{'Lista (Lineal)':<20}{promedio_lineal:<25.8f}{'O(n)'}")
print(f"{'Lista Ordenada':<20}{promedio_binaria:<25.8f}{'O(log n)'}")
print(f"{'Tabla Hash':<20}{promedio_hash:<25.8f}{'O(1)'}")