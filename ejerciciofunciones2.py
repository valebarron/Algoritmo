import os




def menu_general():
    os.system("cls")
    print("------ Menú -------")
    print("1.-Platos")
    print("2.-Bebidas")
    print("3.-Imprimir")
    print("4.-Salir")
    try:
        op_general = int(input("Ingrese una de las opciones:\n"))
        if op > 0 and op < 5:
            return op_general
        else:
            os.system("cls")
            input("Opcion no valida presiona enter para continuar ")
    except:
        os.system("cls")
        input("error en menú principal, presione enter para continuar")

def menu_p():
    os.system("cls")
    print("------ Menú platos -------")
    print("1.- Curanto: \t\t\t $20000")
    print("2.-Mariscal: \t\t\t $12000")
    print("3.-Chupe centolla: \t\t\t $19000")
    print("4.-Empanada: \t\t\t $3000")
    try:
        op_platos = int(input("Ingrese una de las opciones:\n"))
    except:
        os.system("cls")
        input("error en menú platos, presione enter para continuar")

menu= True
while menu:
    opc_general=menu_general()
    if opc_general == 1:
        opmenug = True
        while opmenug:
            opc_platos = menu_p()
            if opc_platos == 1:
                cant_cur = int(input("Cuantos desea comprar?\n"))
            if opc_platos == 2:
                cant_mar = int(input("Cuantos desea comprar?\n"))
            if opc_platos == 3:
                cant_chu = int(input("Cuantos desea comprar?\n"))
            if opc_platos == 4:
                cant_emp = int(input("Cuantos desea comprar?\n"))
            if opc_platos == 5:
                opmenug = False