import os

persona = ["1-7", "Alan", "Patricio", "Brito", "Delgado"]

grupo = [
    ["1-7", "Alan", "Patricio", "Brito", "Delgado"],
    ["1-8", "Maria", "Patricia", "Brito", "Delgado"],
    ["3-9", "Jose", "Francisco", "Brito", "Martinez"]
]

#for i in range(len(persona)):
#    print(persona(i))

def buscar_por_rut(rut_persona):
    for i in range(len(grupo)):
        for i in range(len(grupo(1))):
            if grupo[i] == rut_persona:
               return grupo[i]

def imprimir_persona(array_persona):
        print(f"Rut: \t {array_persona[0]}") 
        print(f"Nombre: \t {array_persona}") 
        print(f"Segundo nombre: \t {array_persona[1]}") 
        print(f"Apellido paterno: \t {array_persona[2]}") 
        print(f"Apellido materno: \t {array_persona[3]}") 
        input("")

def agregar_persona():
    os.system("cls")
    print("------ AGREGAR PERSONA ------")
    rut = input("Indique su rut:\n")
    nombre = input("Indique su nombre:\n")
    segundo_nombre = input("Indique su segundo nombre:\n")
    ap_paterno = input("Indique su apellido paterno:\n")
    ap_materno = input("Indique su apellido materno:\n")

    grupo.append([rut, nombre, segundo_nombre, ap_paterno, ap_materno])

agregar_persona()
print(grupo)