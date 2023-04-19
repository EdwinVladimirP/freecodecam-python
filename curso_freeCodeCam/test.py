

#✅comentarios: # codigo
#✅comentarios: ''' codigo '''

name = "vladimir"
print(type(name),len(name),name[0:8])

print(name.capitalize()) 


#METODOS IMPORTANTES: 

#FIND ---------- ISDIGIT
#INDEX --------- ISLOWER ----------> GENERALMENTE LOS METODOS
#ISALNUM ------- ISUPPER             RETORNAN VALORES FALSO O VERDADERO
#ISALPHA ------- LOWER
#ISDECIMAL ----- UPPER

#datoUsuario = input('Ingresa el dato: ')👉-------> importante:input siempre retorna
#print('ingresaste: ', datoUsuario, type(datoUsuario))                 una cadena de caracteres. 

#datoUsuario = int(input('Ingresa el dato: '))👉------->se colocó int para que debuelva tipo número. 
#print("El dato fué: ", datoUsuario, type(datoUsuario))

#datoTest = bool(input("Ingresa Falso ó Verdadero: "))👉------>se colocó bool para que devuelva tipo booleano
#print("Se ingresó: ", datoTest, type(datoTest))

#🌟una expresión Conbinación de valores, variables, y operadores que al ser 
#evaluados resultan en un valor. 

#🌟Operadores Lógicos:      and or not
#Prioridad:     not ---> and --->or

#🌟Operadores de Asignación: 
"""
edad = 56
edad += 3
print(edad)
edad -=2
print(edad)
edad *= 3
print(edad)
edad /= 2
print(edad)
"""
#🌟Sentencias Condicionales: 
"""Instrucción o un grupo de instrucciones cuya ejecución depende
del valor de una condición---> BOOLEANA<---. """

#if <condición>:
#    Código-------->ojo con la indentación!


"""
temperatura = int(input("Cuantos grados registra el termómetro?: "))
if temperatura < 15:
    print("Está debajo de", temperatura, "Grados", type(temperatura))
else:
    print(temperatura, "Temperatura aceptable", type(temperatura))
#ejemplo:
notas = int(input("Ingresa la Nota:"))
if notas < 6:
    print(notas,"Está por debajo del promedio", type(notas))
else:
    print(notas,"Está bien!", type(notas))
#ejemplo:
hora = int(input("Ingresa la hora: "))
if hora > 8 and hora < 11:
    print("aún en hora!")
else:
    print("No se puede")
#ejemplo:
test = int(input("ingresa el numero secreto:"))
if test == 50:
    print("exito")

tiempo = int(input("ingresa el número: "))
if tiempo <= 5:
    print("menos de cinco", type(tiempo))
elif tiempo >=6:
    print("mayor de cinco", type(tiempo))
"""
#SINTAXIS DE LA CONDICIÓN ELIF:
'''
if <condición>:
    #codigo
elif <condición>:
    #codigo
elif <condición>:
    #codigo
else:
    #codigo
'''







#https://www.youtube.com/watch?v=DLikpfc64cA
#1:44:29