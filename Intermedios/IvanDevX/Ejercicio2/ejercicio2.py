"""
2. **Uso de archivos** : Crea una lista de la compra que se guarde en un fichero txt y que 
el programa te diga si quieres cargarlo o crear uno nuevo ( si es que lo hay ) y te 
permita modificar la lista ya creada o eliminar un elemento en su interior..

"""

RUTA_ARCHIVOS = "./archivostxt/"


def comprobar_archivo():
    try:
        with open (RUTA_ARCHIVOS + "lastname.txt" , "r") as archivo:
            nombre_fichero = archivo.readlines()
        
        if nombre_fichero:
            file_name = nombre_fichero[0].strip()
            print(f"He encontrado el ultimo archivo guardado llamado {file_name}")
            return file_name

    except FileNotFoundError:
        print("Parece que no encuentro ningun archivo anterior.")
                      

def cargar_lista(file_name):
    try:
        with open (RUTA_ARCHIVOS + file_name , "r") as archivo:
            contenido = archivo.read()
            lista_compra = contenido.split("\n")
        
        return lista_compra
        
    except FileNotFoundError:
        print("Lista no encontrada")
    
    
def save_name_list_txt(nombre_archivo):
    with open (RUTA_ARCHIVOS + "lastname.txt" , "w") as archivo:
        archivo.write(nombre_archivo + ".txt")
    
    print("Nombre de la lista almacenada")
    
        
def save_lista_txt(lista_compra):
    print("Este archivo se va a guardar en un TXT")
    print("Que nombre le quieres dar?")
    nombre_archivo = input()

    with open (RUTA_ARCHIVOS + nombre_archivo + ".txt" , "w") as lista:
        lista.write(("\n".join(lista_compra)))
        
    print(f"Lista guardada como {nombre_archivo}")
   
    save_name_list_txt(nombre_archivo)


def ask_user():
    file_name = comprobar_archivo()
    lista_compra = None
    
    if file_name:
        lista_compra = cargar_lista(file_name)
        if lista_compra:
            input("Quieres que te enseñe la lista guardada? [Y/N]").lower() == "y"
            if True:
                print(f"Lista {lista_compra}")
    else:
        lista_compra = []

    while True:
        input_usuario = input(f"Para salir escribe [Q] y editar la [E] :\n" 
                                "Agrega un producto a continuacion : ").strip()
        
        if input_usuario.lower() == "q":
            break
        
        elif input_usuario == "" or len(input_usuario) == 0:
            print("No se permiten espacios en blanco o vacios")
            
        elif input_usuario.lower() == "e":
            if len(lista_compra) == 0:
                print("No se puede editar una lista vacia")
            else:
                print(f"Tu lista es : {lista_compra}")
                print("Escribe lo que quieras quitar de la lista.")
                edit_user = input()
                if edit_user in lista_compra:
                    lista_compra.remove(edit_user)
                    print(f"{edit_user} eliminado")
                else:
                    print("Producto no encontrado. Verifica mayusculas")
            
        elif input_usuario not in lista_compra:
            lista_compra.append(input_usuario)
            print(f"Añadido {input_usuario} y en la lista ahi : {lista_compra}")
        
        elif input_usuario in lista_compra:
            print(f"Añade otro producto, {input_usuario} ya esta en la lista.")
            
    
    save_lista_txt(lista_compra)
       

def main():
    print("Crearemos una lista y la guardaremos en txt")
    ask_user()


if __name__ == "__main__":
    main()
