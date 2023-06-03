def menu_principal():
    print("---------Bienvenido----------")
    print("1.-Grabar")
    print("2.-Buscar")
    print("3.-Imprimir")
    print("4.-Salir")

    try:
        op = int(input("Seleccione una de las opciones:\n"))
        if op > 0 and op < 5:
            return op
    except:
        input("error en menu principal, presione enter para continuar")

grabar = [
    [" 867961-B21", "Servidor Huawei Next Generation 2", "30000"],
    ["840369-A21", "Servidor Huaweii Generation One", "70000"],
    ["777876-H55-H6", "Servidor HP Proliant Intel", "100000"]
]

def menu_grabar():
    numero_parte = input("Indique el numero de parte:\n")
    nombre_producto = input("Indique el nombre del producto:\n")
    precio_producto = input("Indique el precio del producto")

    grabar.append([numero_parte, nombre_producto, precio_producto])

def menu_buscar():