producto = ["Cafe", 5000, 20]

print(producto[0])
print(producto[1])
print(producto[2])

porcentaje_aumento = 20

descuento = (producto[1])*15/100
precio_promocional = (producto[1])-descuento

ingreso_actual = (producto[1])*(producto[2])

aumento_unidades = (producto[2])*porcentaje_aumento/100
unidades_proyectadas = (producto[2])+aumento_unidades

ingreso_proyectado = precio_promocional*unidades_proyectadas
diferencia = ingreso_proyectado-ingreso_actual

if diferencia>0:
    estado ="lanzar"
else: 
    estado ="no lanzar"

print("===ANALISIS DE PROMOCION===")
print(f"Producto: {producto[0]}")
print(f"Precio actual: {producto[1]:,} colones")
print(f"Unidades Actuales: {producto[2]}")
print(f"Ingreso actual: {ingreso_actual:,} colones")
print(f"Descuento: {descuento:,.2f} colones")
print(f"Precio promocional: {precio_promocional:,.2f} colones")
print(f"Aumento unidades: {aumento_unidades:.0f}")
print(f"Aumento esperado en ventas: {porcentaje_aumento}%")
print(f"Unidades proyectadas: {unidades_proyectadas:.0f}")
print(f"Ingreso con promoción: {ingreso_proyectado:,.2f} colones")
print(f"Diferencia: {diferencia:,.2f} colones")

print("===CONCLUSION===")
print(f"1. Recomendacion: {estado}.")


