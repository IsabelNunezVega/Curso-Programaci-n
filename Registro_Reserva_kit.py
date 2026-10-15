#Solución: Misión kit seguro

nombre = input("Nombre: ").upper().strip
kit = input ('Tipo de kit: ').strip().lower()
autorización = input ("Tiene autorización (si/no)? ").strip().lower() == 'si'
try:
    cantidad = int(input("Cantidad de kits?: "))
except ValueError:
        print("Cantidad de kits invalida, digite del 1 al 100")
        cantidad = -1
try:
    días = int(input("Días de préstamo: "))
except ValueError:
    print ("Días de días invalida, digite del 1 al 100")
    días = -1
    
if not nombre or not kit or cantidad < 1:
    resultado = "Registro rechazado: revise los datos ingresados!"
    
elif autorización and cantidad <= 3 and not días > 7:
    resultado = f"Aprobado para {nombre}: {cantidad} kit(s) de kit"
else:
    resultado = "Solicitud enviada a revisión"
    
print ("-" * 50)
print(resultado)
    
