"""Caso 2: asistencia por bloques. Complete el análisis con un ciclo for."""

asistencias = [120, 180, 210, 250, 230]
capacidad = 300

# TODO: Recorra asistencias con for para acumular el total y contar los bloques
#       que SUPERAN el 70 % de la capacidad (210 no cuenta).
total_asistencias = 0
bloques_superan_70 = 0
for asistencia in asistencias:
    total_asistencias += asistencia
    if asistencia > capacidad * 0.7:
        bloques_superan_70 += 1
        
# TODO: Calcule el promedio y su porcentaje de ocupación.
promedio = total_asistencias / len(asistencias)
porcentaje_ocupacion = (promedio / capacidad) * 100

# TODO: Clasifique el promedio: >=80 % alta; >=50 % media; si no, baja.
if porcentaje_ocupacion >= 80:
    estado = "alta"
elif porcentaje_ocupacion >= 50:
    estado = "media"
else:
    estado = "baja"

# TODO: Muestre total, promedio, porcentaje, cantidad de bloques y estado.
# Con los datos base: total 990, promedio 198, 66 %, 2 bloques, ocupación media.
# Prueba de código: use temporalmente cinco bloques con 240 asistentes cada uno
# para comprobar el límite del 80 %. Después restaure la lista.
print(f"Total de asistencias: {total_asistencias}")
print(f"Promedio de asistencias: {promedio:.0f}")
print(f"Porcentaje de ocupación: {porcentaje_ocupacion:.0f} %")
print(f"Cantidad de bloques que superan 70 %: {bloques_superan_70}")
print(f"Estado de ocupación: {estado}") 
