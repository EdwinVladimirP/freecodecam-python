'''
Ciclo While
✅ Ciclo que continúa 👉!MIENTRAS¡👈 una condición es verdadera y se detiene cuando es falsa. 
----> Sintaxis: while <condición>:
                    #código
'''
'''--------> EJEMPLOS <-----------
⚜️
X = 20
while X <= 35:
    print(X)
    X += 3  #35

⚜️
i = 0
while i <= 10:
    print(i)
    i += 1

⚜️
 
a = 0
while a < 10:
    a += 1
    if a == 7:
        print(a)
# --->En el ejemplo anterior vemos dos ciclos, parecidos al anterior ya explicado. Hay un momento en el que se compara si i==7, y luego ocurre un continue. Es decir, cuando el valor sea 7, termina la iteración actual (ya no ejecuta print(i)) y pasa a la siguiente iteración (i+=1).

⚜️

b = 0
while True: #--->Ciclo infinito. 
    b += 1
    print(b)
    if b == 13: 
        break
En el ejemplo anterior se crea un ciclo infinito (while True). Con esto indicamos que el ciclo siempre se ejecuta pues while nunca obtiene un Falso. (Tudor, 2019) ¿Cómo se sale del ciclo? Cuando i==13 se ejecuta la instrucción break. Eso termina la ejecución de todo el ciclo.

'''


