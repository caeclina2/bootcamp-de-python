from os import system
system("clear")
numeros = {1:"uno", 2:"dos", 3:"tres"}
print(numeros)
print(numeros[1])
print(numeros[2])
print(numeros[3])
informacion = {"nombre" : "Carlos",
               "apellido" : "Escobar",
               "estatura" : 1.65,
               "esta feliz" : True }
print(informacion)
claves = informacion.keys()
print(claves)
print(type(claves))
values = informacion.values()
print(values)
pairs = informacion.items()
print(pairs)
contacts = {"CAECLINA" : {"Apellido " : "Escobar",
                          "Altura " : 65,
                          "Edad" : 55,
                          "Teléfono": 3104230014,
                          "Signo Zodiacal": "Libra",
                          "Serie Favorita": "Un viaje al infinito",
                          "Canción favorita": "Para Elisa",
                          "Comida favorita": "Bandeja paisa",
                          "Lugar soñado vacaciones" : "Paris",
                          "Habilidad secreta" : "Dominar las matematicas",
                          "Heroe o persona que admiras": "mi madre",
                          "Libro que más me ha impactado": "El hombre que calculaba",
                          "Superpoder": "volar",
                          "Que logro personal te enorgullese": "Premio a la Excelencia Secretaria de educación del cauca"},
            "Emily" : ("Apellido" : "Ruiz",
                       "altura")
            }
print(contacts)