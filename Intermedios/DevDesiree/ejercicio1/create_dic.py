import string
import random


# Creamos un diccionario vacio
dictio_words = {}


# Creamos una lista de todos los caracteres de ascii.letters
words = list(string.ascii_letters)


print(string.ascii_letters)

# A cada iteracion añadimos en orden la clave con su valor(que el valor es aleatorio)
# Una vez se añada el valor se borrara de la lista para que no se vuelva a repetir
for a in string.ascii_letters:
    random_value = random.choice(words)
    dictio_words[a] = random_value
    words.remove(random_value)
    
    
print(dictio_words)
            

"""
output del diccionario

Clave : Valor

   {
   "a":"d",
   "b":"R",
   "c":"u",
   "d":"E",
   "e":"J",
   "f":"N",
   "g":"T",
   "h":"w",
   "i":"M",
   "j":"k",
   "k":"P",
   "l":"z",
   "m":"e",
   "n":"D",
   "o":"p",
   "p":"Z",
   "q":"K",
   "r":"j",
   "s":"r",
   "t":"Y",
   "u":"i",
   "v":"t",
   "w":"g",
   "x":"v",
   "y":"H",
   "z":"l",
   "A":"m",
   "B":"O",
   "C":"Q",
   "D":"U",
   "E":"s",
   "F":"c",
   "G":"W",
   "H":"q",
   "I":"b",
   "J":"o",
   "K":"S",
   "L":"A",
   "M":"G",
   "N":"L",
   "O":"B",
   "P":"f",
   "Q":"n",
   "R":"V",
   "S":"X",
   "T":"a",
   "U":"y",
   "V":"h",
   "W":"x",
   "X":"I",
   "Y":"C",
   "Z":"F"
}

"""