
'''Estructura de datos utilizada para almacenar múltiples valores en secuecis'''

# sintaxis: [1, 2, 3, 4, 5]
#          👆 0-1-2-3-4-5



letras = ["E", "D", "W", "I", "N"] #metodo: .append() --->sirve para agregar un dato al final de la lista
letras.append("☕️")
print(letras)

letras2 = ["V", "L", "A", "D", "I"] # metodo .insert(<indice>, <elemento>)
letras2.insert(0, "☕️")
print(letras2)

letras3 = ["E", "J", "E", "M", "P", "L", "O"] # remove .remove()
letras3.remove("E")
print(letras3)

#---------<element>---in---<lista>-------- con el operador in, se indica el elemento que se quiere encontrar

numero = [1, 2, 3, 4, 5]
print(6 in numero) #false

granja = ["🐶", "🐺", "🐱", "🐧", "🐮"]
print("🐧" in granja) #true


#-----------.index(<element>)----------Retorna el índice de la primera ocurrencia del elemento
#                                       en la lista. Si no se encuentra el elemento, ocurre un error. 
vocales = ['a', 'e', 'i', 'o', 'u']
print(vocales.index('e')) #valor 1

cosas = ["bolso", "botas", "lentes", "llaves", "🐧"]
print(cosas.index("🐧")) #valor 4

# LAS LISTAS PUEDEN SE MUTABLES: 
#----------<lista>[<índice>] = <nuevo valor
nums = [1, 2, 3, 4, 5]
nums[0] = 10    #------->se actualizó el valor en el indice espesífico de una lista
print(nums)


''' METODOS DE LISTAS'''
#SINTAXIS ------------>     <LISTA>.<METODO>(<PARAMETROS>)
'''
.count(<elemet)--->permite contar cuantas veces se repite un elemento en una lista
.extend(<lista>)--->permite extender los elementos de una lista añadiendo elemetos de otra lista
.pop()--->elimina y retorna un elemento de una lista
.reverse()--->reversa los elementos de una lista
.sort()--->ordena una lista, acendente o decendente
'''
#EJEMPLO:
a = [3, 4, 5, 6]
a.pop()#----->se eliminó el número 6
print(a) 
a.reverse()#---->se invirtió el orden
print(a)
a.extend([8, 9, 0])#--->se le agregó nuevos elementos a la lista: 
print(a)


'''TUPLAS: es una estructura de datos inmutables que contiene una secuencia 
            ordenada de elementos. '''

ejemplo_acceder = ("hola", "hello", "hej")
print(ejemplo_acceder[0])
print(ejemplo_acceder[1])
print(ejemplo_acceder[2])

#encontrar un elemento: 
ejemplo_encontrar = (50, 51, 52, 53, 54, 55, "🐧", 56, 57, 58, 59, 60)
print("🐧" in ejemplo_encontrar, type("🐧"), ejemplo_encontrar.index("🐧"), ejemplo_encontrar.count("🐧"))
 #---> true, también solicité el tipo, la ubicación dentro de la tupla y cuantas veces se repite. 

'''LA DIFERENCIA ENTRE LAS LISTAS Y LAS TUPLAS EN PYTHON ES QUE LAS
LISTAS SON MUTABLES Y LAS TUPLAS SON INMUTABLES.  '''



