import os

def menu_principal():
    os.system("cls")
    print("----- BIENVENIDO A AUTO SEGURO -----")
    print("1.- Grabar")
    print("2.- Buscar")
    print("3.- Imprimir certificado")
    print("4.- Salir")
    opc = opcion(5)
    return opc

def opcion(f):
    try:
        op= int(input("Ingrese una de las opciones"))
        if op > 0 and op < f:
            return op
        else:
            input("Opcion invalida, presione enter para continuar\n")
    except:
        input("Error en la opcion escogida, presione enter para continuar\n")

def op_guardar():
    os.system("cls")
    print("Ingrese los siguientes datos")
    tipo = input("Tipo del vehiculo: ")
    patente = val_patente()
    marca = val_marca()
    precio = val_precio()
    multas = val_multa()
    fecha_registro = input("Fecha de registro: ")
    nombre_dueno = input("Nombre del dueño: ")

    vehiculos_registrados.append([tipo,patente,marca,precio,multas,fecha_registro,nombre_dueno])

    print(f"Vehiculos registrados: {vehiculos_registrados}")

def val_patente():
    val = True
    while val:
        patente = input("Patente del vehiculo: ")
        if len(patente) == 6:
            val = False
        else:
            input("patente invalida, presione enter para continuar\n")
    return patente

def val_marca():
    val = True
    while val:
        marca = input("Marca del vehiculo: ")
        if len(marca) > 1 and len(marca) < 16:
            val = False
        else: 
            input("Marca ingresada invalida, presione enter para continuar\n")
    return marca

def val_precio():
    val = True
    while val:
        precio = input("Precio del vehiculo: ")
        if precio > 5000000:
            val = False
        else:
            input("Precio menor a 5 millones, presione enter para continuar\n")
    return precio

def val_multa():
    multa = []
    val = True
    while val:
        try:
            opc = int(input("Tiene multas?\n1.-Si 2.-No"))
            if opc == 1:
                cant = int(input("Cuantas multas tiene?\n"))
                for i in range(cant):
                    monto_multa = int(input(f"Monto multa {i+1} > "))
                    fecha_multa = input(f"Fecha multa {i+1} > ")
                    multa.append([monto_multa, fecha_multa]) 

                    val = False
            elif opc == 2:
                val = False
        except:
            input("Valor ingresado erroneo, presione enter para continuar\n")
    return multa

def op_buscar():
    print("----Patentes registradas----")
    print(listado_patente)
    patente = ""
    val = True
    while val:
        patente = input("Ingrese la patente que desea consultar: ")
        if patente in listado_patente:
            val = False
        else:
            input("La patente ingresada no se encuentra registrada, presione enter para continuar\n")
    return patente

    

def salir():
    os.system("cls")
    print("")
    print("--- SALIO DEL SISTEMA  ---")
    print("")

vehiculos_registrados=[]
listado_patente = []

menu = True
while menu:
    op_mp = menu_principal()
    if op_mp == 1:
        op_guardar()
    elif op_mp == 2:
        op_buscar()
    elif op_mp == 3:
        print("op 3")
    elif op_mp == 4:
        salir()
        menu = False