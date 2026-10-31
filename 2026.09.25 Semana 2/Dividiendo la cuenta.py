# Pide el monto total de la factura (permite decimales/céntimos)
total_factura = float(input("Ingrese el monto total de la factura: "))

# Pide el número de personas (número entero)
personas = int(input("¿Entre cuántas personas se va a dividir la cuenta? "))

# Calcula cuánto le toca a cada uno
pago_individual = total_factura / personas

# Muestra el resultado final
print("Cada uno debe pagar:", pago_individual)