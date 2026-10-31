#Leer una nota, Si la nota es mayor o igual a 90
# es un Excelente, si la nota es mayor a 80 = Muy bueno
# Nota mayor o igual a 70 = Aprobado.
# Y cualquier nota  inferior a 70 es Reprobado

nota  = float(input('Obtener una nota (0-100):'))

if(nota >= 100) or (nota < 0):
    print('Error: nota no válida, debe estar ente 0-100!!')
else:
    if nota >= 90:
        print('Excelente, Vas bien!!')
    elif nota > 80:
        print("Muy bueno!")
    elif nota >= 70:
        print("Aprobado")
    else:
        print("Reprobado")
        