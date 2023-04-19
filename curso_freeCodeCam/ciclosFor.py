'''CICLOS FOR 
✅Se utiliza cuando SABEMOS CUANTAS VECES REPETIR EL CICLO; Cuando no, utilizamos ciclo while. 

✅ ITERACIÓN: Es una repetición de ciertos grupos de instrucciones o ciclos.

Estructura de control en programación que permite ejecutar una o varias lineas de código múltiples veces.  
✅ Los usamos cuando sabemos con antelación CUÁNTAS VECES debemos repetir ciertas instrucciones . 
  
Sintaxis:
 for <var> in range(<inicio>, <fin>):
    #codigo
'''
'''
for i in range(4): #---------->La función range(4) sirve para devolver una secuencia de números enteros. 
    print(i) #----->0 1 2 3 
# Se pueden personalizar al usar: range(start, stop, [step])


i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for j in range(0, 9, 2):
    print(i[j])

for char in "Loops":
    print(char)

for killer_instinct in "Glacius": 
    print(killer_instinct,)
'''

letras = {"A":1, "B":2}
for clave in letras:
    print(clave)

for valor in letras.values():
    print(valor)

for clave, valor in letras.items():
    print(clave, valor)






'''https://www.youtube.com/watch?v=DLikpfc64cA
02:48:47'''