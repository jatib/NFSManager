import os
import shutil

data = trunk(file)
structured = structureData(data[0])
iPs = ipData(structured)

def mainHook(fin=False):
    if fin == False:
        print("Selecciona una de las siguientes opciones:\n1) Reemplazar ip\n2)Eliminar ip\n3)Añadir ip\n4)Visualizar dependencias según ip\n5)Visualizar dependencias según carpetas\n\n")

        option = int(input("Introduzca número de opción:\n"))
        if option == 4:
            print("Selecciona una de las siguientes opciones:\n1)Filtrar\n2)Mostrar todo\n\n")
            option = int(input("Introduzca número de opción:\n"))
            print("\n\n")
            if option == 1:
                query = input("Introduzca una nueva ip:\n")
                if query in iPs:
                    print(iPs.index(query))
                else:
                    print("La ip señalada no existe")
        mainHook()

mainHook()
