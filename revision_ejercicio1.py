cantidad_paciente = 0
contar_60 = 0
contar_mas_60 = 0

ingreso_ok = True
while ingreso_ok:
    try:
        cantidad_paciente= int(input("Ingrese la cantidad de pacientes "))
        if cantidad_paciente > 0:
            ingreso_ok = False
        else:
            print("Debe ingresar un valor mayor que cero")
    except:
        print("ERROR: Ingrese un valor valido")    
for i in range(cantidad_paciente):
    nombre_paciente = input("Ingrese el nombre del paciente ") 
    ingreso_ok = True
    while ingreso_ok:
        try:
            edad_paciente= int(input(f"Ingrese la edad de paciente {nombre_paciente} "))
            if edad_paciente > 0:
                ingreso_ok = False
            else:
                print("Debe ingresar un valor mayor que cero")
        except:
            print("ERROR: Ingrese un valor valido") 
    if edad_paciente <= 60:
        print(f"El pacient {nombre_paciente} tiene 60 o menos años ")
        contar_60 += 1
    else:
        print(f"El pacient {nombre_paciente} es mayor de 60 años ")
        contar_mas_60 += 1      
     
print(f"Se registraron {contar_mas_60} pacientes mayores de 60 años.")
print(f"Se registraron {contar_60}  pacientes de 60 años o menos.")

