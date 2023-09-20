"""
2. **Uso de archivos** : Crea una lista de la compra que se guarde en un fichero txt y que 
el programa te diga si quieres cargarlo o crear uno nuevo ( si es que lo hay ) y te 
permita modificar la lista ya creada o eliminar un elemento en su interior..

"""
# Constante con la ruta de los archivos.
RUTA_ARCHIVOS = "./archivostxt/"


def comprobar_archivo():
    
    """
    1. Verifico el nombre con el que el usuario guardo la lista
    Esto es un archivo con el nombre lastname que en su interior tiene el nombre de la lista que le dio el usuario ( Porque el usuario puede elegir con que nombre guardarla)
    """
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
    """
    1.Sabiendo el nombre de la lista se pasa como paremetro y se lee el contenido del txt
    2. Se guarda todo el contenido en str y luego se hace un split por saltos de linea
    3. Si todo esta bien retorna la lista
    """
    try:
        with open (RUTA_ARCHIVOS + file_name , "r") as archivo:
            contenido = archivo.read()
            lista_compra = contenido.split("\n")
        
        return lista_compra
        
    except FileNotFoundError:
        print("Lista no encontrada")
    
    
def save_name_list_txt(nombre_archivo):
    """
    Aqui se guarda el nombre de la lista en el archivo lastname.txt
    """
    with open (RUTA_ARCHIVOS + "lastname.txt" , "w") as archivo:
        archivo.write(nombre_archivo + ".txt")
    
    print("Nombre de la lista almacenada")
    
        
def save_lista_txt(lista_compra):
    """
    Se pasa como parametro la lista de compra
    Se le pregunta al usuario con que nombre quiere guardar la lista
    Al final se guarda en txt
    """
    print("Este archivo se va a guardar en un TXT")
    print("Que nombre le quieres dar?")
    nombre_archivo = input()

    with open (RUTA_ARCHIVOS + nombre_archivo + ".txt" , "w") as lista:
        lista.write(("\n".join(lista_compra)))
        
    print(f"Lista guardada como {nombre_archivo}")
   
    save_name_list_txt(nombre_archivo)


def ask_user():
    
    """
    1. Comprobamos si esta el nombre de la lista y si esta comprobamos la lista
    2. En caso de que la lista no este, se crea una.
    
    3. Con un bucle While se pregunta al usuario si quiere editar , añadir o salir de la lista
    3.1 Se manejan errores y posibles entradas invalidas,asi como si un producto ya esta en la lista, no se duplica.
    
    4. Al finalizar se manda como parametro la lista a la funcion save_lista_txt para que guarde la lista en un txt
    
    """
    
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
        
        elif len(input_usuario) == 0:
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
    # Funcion Principal
    print("Crearemos una lista y la guardaremos en txt")
    ask_user()


if __name__ == "__main__":
    main()
