def menu1():
    print("Bienvenido al restaurante")
    print("1.-Platos")
    print("2.-Bebidas")
    print("3.-Imprimir boleta")
    print("4.-Salir")
    op = int(input("Ingrese una opción"))
    return op

def menu_platos():
    print("--Menú platos--")
    print("1.-Curanto:      $20000")
    print("2.-Mariscal:     $12000")
    print("Chupe centolla:  $19000")
    print("4.-Empanada:     $3000")

def menu_bebidas():
    print("--Menú de bebidas--")
    print("1.-Pisco sour:   $5000")
    print("2.-Bebida lata:  $3000")
    print("3.-Jugo:         $2000")

def imp_boleta():
    print("-----Boleta-----")

print(menu1)

menu = True
while menu:
    op = menu1
    if op == 1:
        menu_platos
    if op == 2:
        menu_bebidas
    if op == 4:
        imp_boleta
    if op == 4:
        menu = False
        print("Hasta luego")