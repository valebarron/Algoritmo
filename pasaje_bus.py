import os

bus = [
    ["A0","A1","A2"],
    ["B0","B1","B2"],
    ["C0","C1","C2"],
    ["D0","D1","D2"],
    ["E0","E1","E2"],
    ["F0","F1","F2"],
    ["G0","G1","G2"],
    ["H0","H1","H2"]
]

def imprimir_asientos():
    i_asientos = "------BUS-------\n"
    for fila in bus:
        for asiento in fila:

            asiento_del_bus.append(asiento)

            if asiento in asientos_comprados:
                i_asientos += "[--]"
            else:
                i_asientos += f"[ {asiento} ]"
        i_asientos+="\n"

    print(i_asientos)


def menu_general():
    print("----BUSES SPEDDY GONZALES----")
    print("1.-Mostrar asientos")
    print("2.-Comprar pasaje")
    print("3.-cancelar pasaje")
    print("4.-Pagar pasaje")
    print("5.-Cancelar compra")
    print("6.-Salir")

    try:
        opcion = int(input("Seleccione una de las opciones disponibles\n"))
        if opcion >0 and opcion < 7:
            return opcion
        else:
            input("No disponible")
    except:
        input("No disponible, presione enter para continuar")

def comprar_asiento():
    opcion= input("Ingrese el asiento que desa utilizar\n")

    if opcion in asiento_del_bus:
        if opcion in asientos_comprados:
            asientos_comprados.append(opcion)
            os.system("cls")
            input(f"El asiento {opcion} fue registrado")
        else:
            input("El asiento indicado se encuentra ocupado, presione enter para continuar")
    else:
        input("El asiento indicado no existe, presione enter para continuar")


def persona_pasaje():
    print("Favor indique sus datos")
    rut = input("Rut: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")

    pasajero_bus.append([asiento, rut, nombre, apellido])

def imprimir_pasajero():
    os.system("cls")
    print("-----PASAJERO-----")
    asiento = input("Seleccione uno de los asientos")
    for pasajero in pasajero_bus:
        if asiento in pasajero:
            print(f"Asiento: {asiento[0]}")
            print(f"Rut: {asiento[1]}")
            print(f"Nombre: {asiento[2]}")
            print(f"Apellido: {asiento[3]}")


asientos_comprados = []
asiento_del_bus = []
pasajero_bus = []

menu = True
while menu:
    op_menu= menu_general()
    if op_menu == 1:
        imprimir_asientos()
        input("")
    if op_menu == 2:
        imprimir_asientos()
        comprar_asiento()
    if op_menu == 3:
        imprimir_asientos()