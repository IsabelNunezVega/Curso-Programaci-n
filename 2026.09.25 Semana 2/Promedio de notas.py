# 1, 2 y 3. Leer las tres notas
nota1 = float(input("Ingrese la Nota 1: "))
nota2 = float(input("Ingrese la Nota 2: "))
nota3 = float(input("Ingrese la Nota 3: "))

# 4. CALCULAR promedio (los paréntesis aseguran que primero se sume y luego se divida)
promedio = (nota1 + nota2 + nota3) / 3

# 5. MOSTRAR el resultado
print("Tu promedio final es: " + str(promedio))