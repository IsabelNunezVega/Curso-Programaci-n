"""Plantilla guiada: análisis de ventas de dos tiendas, sin ciclos."""

ventas_centro = [125000, 98000, 147000, 132000, 110000]
ventas_norte = [140000, 135000, 150000, 145000, 155000]

# TODO: calcula total, cantidad, mayor y menor para Centro.

total_centro = sum(ventas_centro)
cantidad_centro = len(ventas_centro)
mayor_centro = max(ventas_centro)
menor_centro = min(ventas_centro)
# TODO: calcula promedio, rango, diferencia y porcentaje para Centro.

promedio_centro = sum(ventas_centro)/len(ventas_centro)
rango_centro = max(ventas_centro)-min(ventas_centro)
diferencia_centro = max(ventas_centro)-min(ventas_centro)
porcentaje_centro = (rango_centro/sum(ventas_centro))*100

# TODO: repite los indicadores para Norte.
total_norte = sum(ventas_norte)
cantidad_norte = len(ventas_norte)
mayor_norte = max(ventas_norte)
menor_norte = min(ventas_norte)
promedio_norte = sum(ventas_norte)/len(ventas_norte)
diferencia_norte = max(ventas_norte)-min(ventas_norte)
rango_norte = max(ventas_norte)-min(ventas_norte)
porcentaje_norte = (rango_norte/sum(ventas_norte))*100
diferencia_regiones = sum(ventas_norte)-sum(ventas_centro)

# TODO: decide si cada tienda superó, igualó o no alcanzó su meta.

meta_centro = 640000
meta_norte = 700000
dif_meta_centro = sum(ventas_centro)-meta_centro
dif_meta_norte = sum(ventas_norte)-meta_norte

if total_centro>meta_centro:
    estado_centro ="superó la meta"
elif total_centro==meta_centro:
    estado_centro ="igualó la meta"
else:
    estado_centro ="no alcanzó la meta"
    
if total_norte>meta_norte:
    estado_norte ="superó la meta"
elif total_norte==meta_norte:
    estado_norte ="igualó la meta"
else:
    estado_norte ="no alcanzó la meta"    

# TODO: compara los totales y los rangos.

if total_norte>total_centro:
    mayor_total ="norte"
elif total_centro>total_norte:
    mayor_total ="centro"
else:
    mayor_total ="empate"
    
if rango_norte<rango_centro:
    mas_estable ="norte"
elif rango_centro<rango_norte:
    mas_estable ="centro"
else:
    mas_estable ="empate"    

# TODO: presenta un reporte con etiquetas claras y f-strings.

print("===REPORTE DE VENTAS===")
print(f"Total Centro: {total_centro:,} colones")
print(f"Meta Centro: {meta_centro:,} colones -> {estado_centro}")
print(f"Promedio Centro: {promedio_centro:,.2f} colones") 
print(f"Rango Centro: {rango_centro:,} colones")
print(f"Total Norte: {total_norte:,} colones")
print(f"Meta Norte: {meta_norte:,} colones -> {estado_norte}")
print(f"Promedio Norte: {promedio_norte:,.2f} colones")
print(f"Rango Norte: {rango_norte:,} colones")
print(f"Mayor Total: {mayor_total}")
print(f"Tienda Estable: {mas_estable}")

# TODO: escribe las tres conclusiones solicitadas en la guía.

print("===CONCLUSIONES===")
print(f"1. La tienda {mayor_total} vendió más, con una diferencia de {diferencia_regiones:,} colones.")
print(f"2. La tienda {mas_estable} fue más estable, con un rango de {rango_norte:,} colones frente a {rango_centro:,} colones.")
print(f"3. Centro {estado_centro} y Norte {estado_norte}.")
