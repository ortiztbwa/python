import os

def init():
    print("***ADMINISTRADOR DE CARPETAS Y ARCHIVOS***")
    opcion =    input("seleccione una opción c=crear e=eliminar")
    if(opcion == "c"):
        ruta = input("indique la ruta o deje en blanco para la actual")
        if(ruta==""): ruta = os.getcwd() + "\\"
        #comprobar si la ruta existe
        if(os.path.isdir(ruta)):
            tipo = input("indique el tipo a=archivo c=carpeta")
            if(tipo=="a"):
                archivo = input("indique el nombre del archivo")
                #crear el archivo
                manejador = open(ruta+archivo,"w")
                manejador.close()
                print("archivo", archivo,"creado con exito")
            elif(tipo=="c"):
                carpeta = input("indique el nombre de la carpeta")
                #crear la carpeta
                os.mkdir(ruta+carpeta)
                print("Carpeta",carpeta,"creada con exito")
            else: init() #reiniciamos el programa    
    elif(opcion == "e"):
        ruta = input("indique la ruta o deje en blanco para la actual")
        if(ruta==""): ruta = os.getcwd() + "\\"
        eliminar = input("indique el nombre de la carpeta o archivo a eliminar")
        #si es un archivo
        if(os.path.isfile(ruta+eliminar)):
            os.remove(ruta+eliminar)
            print("archivo",eliminar,"eliminado con exito")
        #si es una carpeta
        if(os.path.isdir(ruta+eliminar)):
            os.rmdir(ruta+eliminar)
            print("carpeta", carpeta, "eliminada con exito")
        else: init() #reiniciar el programa
    else: init() #reiniciar el programa
    
init()    