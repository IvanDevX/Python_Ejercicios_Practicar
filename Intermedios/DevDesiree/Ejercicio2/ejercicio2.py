"""
2. **Uso de archivos** : Crea una lista de la compra que se guarde en un fichero txt y que el programa te diga si quieres cargarlo o crear uno nuevo ( si es que lo hay ) 
                            y te permita modificar la lista ya creada o eliminar un elemento en su interior..
"""

def lastlist_name():
    """
    Leemos el nombre de archivo de la lista creada por el usuario, desde otro archivo.txt para poder leerse posteriormente en el caso de que haya un archivo ya creado
    """
    try:
        with open("namelist.txt" , "r") as namelist:
            name = namelist.readline()
            
        if name:
            print(f"He encontrado la lista con el nombre {name}")
            return name
            
    except FileNotFoundError:
        print("Archivo no encontrado")


def verify_list(namelist):
    """
    1.- Pasamos como parametro el archivo el nombre de la lista
    2.- Guardamos todo el contenido en la variable contenido en modo str y luego le hacemos un split por cada saltos de linea
    3.- Si todo es correcto retornamos la lista
    """
    try:
        with open(namelist, "r") as verifylist:
            contenido = verifylist.read()
            list_shop = contenido.split("\n")
        
        return list_shop
    
    except FileNotFoundError:
        print("Lista no encontrada")


def save_namelist_txt(text_user_txt):
    """
    Guardamos el nombre de la lista del usuario en el archivo namelist.txt
    """
    with open("namelist.txt", "w") as namelist:
        namelist.write(text_user_txt)
        
    print("Nombre de la lista guardada")


def save_txt(list_shop):
    """
    1.- Pasamos como parametro la lista de la compra
    2.- Preguntamos al usuario que nombre quiere darle al archivo.txt donde guarda la lista
    3.- Si todo va bien se guardara el archivo con el nombre establecido por el usuario
    """
    text_user = input("Que nombre quieres darle al archivo? \n")
    
    text_user_txt = text_user + ".txt"
    
    lista_compra_str = "\n".join(list_shop)
    
    with open(text_user_txt , "w") as mi_lista:
        mi_lista.write(lista_compra_str)
        
    print("Lista Guardada")
        
    save_namelist_txt(text_user_txt)
    

def ask_user():
    """
    1.- Comprobaremos si hay un archivo con la lista cargada creada anteriormente y si es asi, mostraremos el nombre de dicha lista
    2.- Si no existe, se creara una desde 0
    3.- Se crea un bucle WHILE que pregunte al usuario que producto desea guardar a la lista, 
            si escribe la q , saldra del bucle y continuara a la siguiente funcion de guardado de archivos
    4.- Si escribe la E se eliminara el producto que escriba el usuario , en caso de que exista en la lista
    5.- Se manejaran errores en el caso de que exista un articulo ya en la lista, o no se encuentre el producto para borrar de la lista
    6.- Si el usuario quiere salir, se llamara a la funcion de guardado de archivo pasandole como parametro la lista de la compra
    """
    namelist = lastlist_name()
    list_shop = None
    
    if namelist:
        list_shop = verify_list(namelist)
        if list_shop:
            print("He encontrado la lista guardada anteriormente")
            print(list_shop)
        else: 
            list_shop = []   
            
    else:
        print("No encuentro la lista.")
        list_shop = []

    while True:
        ask_user = input("Que producto quieres guardar en la lista?: \n"
                         "Si quieres salir escribe [Q] \n"
                         "Si quieres editar un producto [E] \n").lower()
        
        if ask_user == "q":
            print("Guardando lista... \n")
            break
        
        elif ask_user == "e":
            ask_user = input("Que producto deseas eliminar?: \n")
            if ask_user in list_shop:
                list_shop.remove(ask_user)
                print(f"Ok borro {ask_user} \n")
                print(f"Tu lista contiene: {list_shop} \n")
            else:
                print(f"No encuentro {ask_user} en la lista. Verifica las mayusculas \n")
                print(f"Tu lista contiene: {list_shop} \n")
                
        elif ask_user in list_shop:
            print("Ese producto ya esta en la lista! \n")
            
        elif ask_user not in list_shop:
            print(f"Vale! te agrego {ask_user} a la lista! \n")
            list_shop.append(ask_user)
            print(f"Tu lista contiene: {list_shop} \n")
            
            
    save_txt(list_shop)       

   
def main():
    print("----> Uso de Archivos, Crea una lista de la compra y te la guardo en txt <----")
    ask_user()


if __name__ == "__main__":
    main()