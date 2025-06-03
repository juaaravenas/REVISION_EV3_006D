opcion = 0
cantidad_entradas = 0
while  opcion != 4:
    print("***** Cine Estrella *****")
    print("Bienvenido al sistema de venta de entradas del Cine Estrella")
    print("1.	Ver cuántas entradas quedan.")
    print("2.	Comprar una cantidad de entradas.")
    print("3.	Cargar entradas.")
    print("4.	Salir del sistema.")
    ingreso_ok = True
    while ingreso_ok:
        try:
            opcion = int(input("Opcion a  ejecutar "))
            if opcion > 0 and opcion <= 4:
                ingreso_ok = False
            else:
                print("Debe ingresar un valor mayor que cero y menor o igual a 4 ")
        except:
            print("ERROR: Ingrese un valor valido") 
    match opcion:
        case 1:
            print(f"En este momento queda {cantidad_entradas} entradas para su venta ")

        case 2:
            ingreso_ok = True
            while ingreso_ok:
                try:
                    cantidad_comprar = int(input("Ingrese la cantidad de entradas a comprar "))
                    if cantidad_comprar <= 0:
                        print(f"Cantidad a comprar debe ser mayor que cero ")          
                    elif cantidad_comprar <= cantidad_entradas:
                        cantidad_entradas = cantidad_entradas - cantidad_comprar
                        ingreso_ok = False
                    else:
                        print(f"Cantidad insuficiente de entradas disponibles ")
                except:
                    print("ERROR: Ingrese un valor valido") 
        case 3:
            ingreso_ok = True
            while ingreso_ok:
                try:
                    cantidad_cargar = int(input("Ingrese la cantidad de entradas a cargar "))
                    if cantidad_cargar <= 0:
                        print(f"Cantidad a cargar debe ser mayor que cero ")  
                    else:
                        cantidad_entradas = cantidad_entradas + cantidad_cargar
                        ingreso_ok = False
                except:
                    print("ERROR: Ingrese un valor valido") 
        case 4:
            print("Gracias por preferirnos ")