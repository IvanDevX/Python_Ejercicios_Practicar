import string
import random

# Funcion para generar aleatoriamente un diccionario con los caracteres cambiados (No tengo ganas de crearlo a mano xD) y asi practicar.

# Crear una lista de caracteres disponibles
caracteres_disponibles = list(string.ascii_letters)

# Crear un diccionario vacio
diccionario_caracteres = {}

# Por cada iteracion del for añadimos en orden el caracter con su valor ( que es aleatorio) y una vez añadido se borra de la lista para no repetir
for caracter in string.ascii_letters:
    valor_aleatorio = random.choice(caracteres_disponibles)
    diccionario_caracteres[caracter] = valor_aleatorio
    caracteres_disponibles.remove(valor_aleatorio)

print(diccionario_caracteres)

"""
output pasado por JSON formatter

   {
   "a":"q",
   "b":"a",
   "c":"T",
   "d":"j",
   "e":"t",
   "f":"h",
   "g":"x",
   "h":"F",
   "i":"i",
   "j":"G",
   "k":"b",
   "l":"J",
   "m":"N",
   "n":"p",
   "o":"K",
   "p":"d",
   "q":"E",
   "r":"w",
   "s":"o",
   "t":"k",
   "u":"v",
   "v":"m",
   "w":"H",
   "x":"f",
   "y":"O",
   "z":"Z",
   "A":"Y",
   "B":"c",
   "C":"y",
   "D":"s",
   "E":"A",
   "F":"U",
   "G":"I",
   "H":"z",
   "I":"P",
   "J":"r",
   "K":"W",
   "L":"C",
   "M":"Q",
   "N":"B",
   "O":"D",
   "P":"l",
   "Q":"n",
   "R":"g",
   "S":"M",
   "T":"L",
   "U":"S",
   "V":"u",
   "W":"X",
   "X":"R",
   "Y":"V",
   "Z":"e"
}

"""
        