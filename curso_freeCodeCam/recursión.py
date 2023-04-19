'''RECURSIÓN
Definir algo en términos de sí mismo. 
'''
# la secuencia de fibonacci es un ejemplo: fib(n) = fib(n-1) + fib(n-2)
'''Función Recursiva: Función que se llama a sí misma'''

0, 1, 1, 2, 3, 5, 8, 13, 21

def fibonacci(n):
    if n == 0 or n == 1: 
        return n
    else: 
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(2))

#una función recursiva debe tener un caso base y un caso recursivo para llegar al caso base. 
def factorial(n):
    if n == 0 or n == 1: 
        return 1
    else: 
        return n * factorial(n-1)
    
print(factorial(5))

with open("frases_famosas.txt", "r") as archivo:
    for linea in archivo: 
        print("☕️=== Frase ===☕️")
        print(linea)

with open("frases_pruebas.txt", "r") as file:
    for linea in file: 
        print("🔎...")
        print(linea)











