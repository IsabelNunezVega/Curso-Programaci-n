#Misión Final: "Embajada Python"
monto = int(input("Monto en cuenta bancaria"))
antecedentes = (input("Tiene antecedentes penales? (si/no): "))
profesion = input("profesion?")
if (monto>=50000 and antecedentes =="no") or (profesion== "diplomatico"):
    print("Aprobado: Visa Dorada")
elif (monto>=20000 and antecedentes =="no"):
    print("Aprobado: Visa Estandar")
elif (monto < 20000 and (profesion == "estudiante") or (profesion == "jubilado")):
    print("Pendiente: Requiere entrevista")
else:
    print("Denegado")