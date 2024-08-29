from os import system
system("clear")
#Iterador que genere impares
#range(1, limit+1, 2)
odd_iter = iter(range(1,10,2))
for num in odd_iter:
    print(num)
#Definir funcion generadora
def my_generator():
    yield 1
    yield 2
    yield 3
#usar un bl
print("Generador")
for value in my_generator():
    print(value)
print("Serie Fibonacci")
def fibonacci(limit):
    #inicializar los dos primero números de la secuencia de Fibonacci
    a, b = 0, 1
    #Continuar generando números mientras 'a' sea menor que el límte
    while a < limit:
        yield a #Devolver el valor actual de 'a' y pausar la ejecución de la función
        a, b = b, a + b 
for num in fibonacci(10):
    print(num)

    
    

