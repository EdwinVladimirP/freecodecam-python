import math
print(math.pow(9, 2))
print(math.pi)

import math as matematica #se importó math y se le dió un nombre alternativo
matematica.pi

# from <módulo> import <elemento> -------->se usa para importar un solo elemento. 
print(pow(6, 2))


'''TEMA APARTE:

ERRORES Y EXCEPCIONES

SintaxError:

 Error en la sintaxis del programa. Ocurre cuando no se siguien las reglas formales para escribir el código 
 
 IndexError: 
 Error detectado durante la ejecución de un programa. 
 
 KeyError(Error de clave): 
 Se da cuando se intenta acceder a una clave que no está en un diccionario.
 
 NameError: 
  Se genera cuando el nombre de una variable no se reconose, o no esta definida la variable.
   
 RecursionError: 
   '''

#       try: 
#       except: 

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
try: 
    resultado = num1 / num2
    print(f"{num1} / {num2} = ", resultado)
except: 
    ZeroDivisionError 
    print("Alerta, Excepción. ") # ---->salta hasta esta parte al detectar una excepción ej: 0 
else: 
    print("Else")

    '''Sintaxis: 
try: 
    Intenta ejecutar este código
except <tipo_de_excepción> as <var>: 
    si ocurre una excepción de este tipo, 
    detente inmediateamente y ejecuta
    este código
else: 
    si no ocurrió una excepción en 'try'
    ejecuta este código
finally: 
    luego ejecuta este código. '''