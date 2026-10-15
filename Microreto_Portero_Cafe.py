"""Microreto: el portero del café."""

nombre = input("como te llamas?: ").upper().strip()
energia = int(input("Cuánta energía tienes de 0 a 100?:"))
trae_café = input("Trae café (si/no)?: ").lower().strip() == 'si'

mensaje = ''
# Si menos 50% y no tengo café: -> Descansar
if energia < 50 and not trae_café: #trae_cafe == False
    mensaje = "Descansar"
# Si 50% o mas o tenga café : -> Puede ingresar a la clase
elif energia >= 50 or trae_café:
    mensaje = "Puede ingresar a la clase"
# Cualquier otro escenario : Portero confundido : revisar respuestas
else:
    mensaje = "Portero confundido: revisar respuestas"

print(f"{nombre}: {mensaje}")
