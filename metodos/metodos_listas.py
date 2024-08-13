from os import system
system("clear")
lista = list (["Hola", " Caeclina", 1969])
#Nos devuelve la longitud de la lista
cadena = "hola"
resultado = len(lista)
print(resultado)
#Agrega un elemmento a la lista
lista.append("ALberto")
lista.insert(2,"Escobar")
print(lista)
#Agrega varios elemmentos a la lista
lista.extend(["Vereda Rionegro","Corinto","Cauca"])
print(lista)
print(len(lista))
lista.pop(0)
print(len(lista))
lista.pop(-1)
print(len(lista))
print(lista)
#Eliminando por su valor
lista.remove("Escobar")
print(lista)
lista2 = list ([1969, 10, 14, 2023, 2017, 1974])
print(lista2)
#Ordenando
lista2.sort()
print(lista2)
lista2.sort(reverse=True)
print(lista2)
#Verificar un elemento existente
elemento_encontrado=lista2.index(10)
print(elemento_encontrado)