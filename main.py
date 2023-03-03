import pprint

tareas = {}
id = 1
rta = True

print("===================================")
print("======== LISTA DE TAREAS ==========")
print("===================================")

while rta:
    print("1- Crear tarea")
    print("2- Eliminar tarea")
    print("3- Listar tareas")
    print("4- Terminar programa")
    print("")
    rta = int(input("Ingresa la operación que desea hacer: "))

    if(rta == 1):
        tarea = str(input("Ingresa la tarea: "))
        tareas[id] = tarea
        tarea = ""
        id = id + 1
    elif(rta == 2):
        eliminar = int(input("Ingresa el id de la tarea: "))
        tareas.pop(eliminar)
        print("")
        pprint.pprint(tareas)
        print("")
        eliminar = 0
    elif(rta == 3):
        print("")
        pprint.pprint(tareas)
        print("")
    elif(rta == 4):
        rta = False
    else:
        print("")
        print("¡Operación no encontrada!")
        print("")