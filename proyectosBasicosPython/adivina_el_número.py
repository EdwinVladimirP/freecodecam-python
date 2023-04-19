'''ADIVINA EL NÚMERO
El usuario va a adivinar el número en un rango específico y 
le vamos a decir si ese rango es mayor, menor, igual al número aletorio generado por la computadora. '''



import random  #---->vamos a importar el módulo random 


def adivina_el_número(x): #----->primero definimos una función.
      
      print("===========================")
      print("***¡Bienvenido(a) al juego!***")
      print("=============🎰=============")
      print("Tu meta es adivinar el número generado por la computadora.")
      
      número_aleatoreo = random.randint(1, x)     #---->función: randint = número aleatoreo(ran-random, int-integer = randint)
      predicción = 0

      while predicción != número_aleatoreo:
            predicción = int(input(f"Adivina un número entre 1 y {x}: "))

            if predicción < número_aleatoreo:
                  print("👉Intenta otra vez. Este número es muy pequeño.")
            elif predicción > número_aleatoreo: 
                  print("👉Intenta otra vez. Este número es muy grande.")

      print(f"🤓¡Felicitaciones! Adivinaste el número {número_aleatoreo} correctamente.")



adivina_el_número(10) #----> se definió un rango entre 1 y 10.




