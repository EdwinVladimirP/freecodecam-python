'''
Funciones:
Bloque de código reutilizable que realiza una sola tarea espesífica. 
---> Sintaxis: def <función>():
                  #código


def mostrar_mensaje():
    print("hola, mundo!")


i = 0
while i <=5:
    mostrar_mensaje()
    i += 1
'''

'''def <función>(<parámetro>):
         #código '''

def mostrar_doble(num):
    print(num * 2)



def sumar(a, b):
    return(a + b)

resultado = sumar(int(input("dato 1: ")), int(input("dato 2: ")))
print("La suma resulta en:", resultado, " y el tipo de dato resultante es:", type(resultado))

#👉 Cuando se ejecuta 'return', la ejecución de la función se detiene inmediatamente. 
'''
Otra manera sería: 

def sumar(a, b):
    return a + b

dato1 = int(input("Ingrese el primer número: "))
dato2 = int(input("Ingrese el segundo número: "))
resultado = sumar(dato1, dato2)
print("La suma resulta en: " + str(resultado) + " y el tipo de dato resultante es: " + str(type(resultado)))

'''
#Alcance de una Variable (Scope)
"""Alcance que tendrá la variable en el programa. Dónde se podrá usar.
    Determina a qué variables se tiene acceso en cada parte del programa.  """







