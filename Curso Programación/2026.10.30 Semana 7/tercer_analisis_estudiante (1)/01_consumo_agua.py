"""Caso 1: cambio del consumo diario de agua. Complete el programa."""

consumos_litros = [120, 115, 108, 102, 96]

# TODO: Calcule el consumo total y el promedio diario.
consumo_total = sum(consumos_litros)
promedio_diario= consumo_total / len(consumos_litros)

# TODO: Compare el primer día con el último: litros ahorrados y porcentaje
#       de reducción respecto al primer día.
ahorro_litros = consumos_litros[0] - consumos_litros[-1]
reduccion_porcentaje = (ahorro_litros / consumos_litros[0]) * 100   

# TODO: Clasifique: >=15 % reducción alta; >0 % reducción moderada;
#       de lo contrario, sin reducción.
if reduccion_porcentaje >= 15:
    clasificacion = "reducción alta"
elif reduccion_porcentaje > 0:
    clasificacion = "reducción moderada"
else:   
    clasificacion = "sin reducción" 

# TODO: Muestre los cinco resultados.
# Control: total 541 L; promedio 108,2 L; ahorro 24 L; reducción 20 %;
#          reducción alta.
# Prueba: use temporalmente cinco consumos iguales. Debe indicar 0 % y
# "Sin reducción". Restaure la lista antes de entregar.
print(f"Consumo total: {consumo_total} Litros")
print(f"Promedio diario: {promedio_diario:.1f} Litros")
print(f"Ahorro en litros: {ahorro_litros} Litros")
print(f"Reducción porcentual: {reduccion_porcentaje:.0f} %")
print(f"Clasificación: {clasificacion}")    
