# 1. ENTRADA
print("--- CALCULADORA DE TARIFA DE VIAJE ---")
# Se solicita la distancia y el tiempo. 
distancia_km = float(input("Ingrese la distancia total del viaje (en km): "))
tiempo_minutos = float(input("Ingrese el tiempo estimado del viaje (en minutos): "))

# 2. PROCESO
# Definición de constantes del servicio (valores fijos)
TARIFA_BASE = 130
PRECIO_KM = 50
PRECIO_MIN = 75

# Cálculos basados en el diseño EPS
costo_distancia = distancia_km * PRECIO_KM
costo_tiempo = tiempo_minutos * PRECIO_MIN
costo_total = TARIFA_BASE + costo_distancia + costo_tiempo

# 3. SALIDA
print("\n--- RESUMEN DEL COBRO ESTIMADO ---")
print(f"Tarifa base: ₡{TARIFA_BASE}")
print(f"Costo por distancia ({distancia_km} km): ₡{costo_distancia:.2f}")
print(f"Costo por tiempo ({tiempo_minutos} min): ₡{costo_tiempo:.2f}")
print("----------------------------------")
print(f"VALOR TOTAL ESTIMADO: ₡{costo_total:.2f}")
print("----------------------------------")