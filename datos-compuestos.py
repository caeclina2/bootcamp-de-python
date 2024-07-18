from os import system
system("clear")
#El primer tipo de datos: Listas

lista = ["Carlos","Magister en matematicas",True,1.68]
print(lista) 
lista[3]="CAECLINA"
print(lista[3])

#El primer tipo de datos: tupla

tupla = ("Carlos","Magister en matematicas",True,1.68)
print(tupla[1]) 
#tupla[1]="Robotica"
#print(tupla[1]) 

#Creando un conjunto o Set
#No admite duplicados

conjunto={"Carlos","Magister en matematicas",True,1.68,1.68,"Carlos"}
print(conjunto)

#Creando un diccionario

diccionario = {
    "nombre", "Magister en matematicas",
    "apellido", "Escobar",
    "estatura", 1.68,
}

print(diccionario["nombre"])