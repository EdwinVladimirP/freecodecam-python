'''El Ahorcado
Se presenta una palabra de una serie de palabras disponible y el 
usuario debe intentar adivinar esa palabla, tiene un numero espesífico de vidas pero tiene que ir adivinando letra por letra'''

import random
import string

from palabras import palabras
from ahorcadoDiagrama import vidas_diccionario_visual

def obtener_palabra_valida(palabras):
    #seleccionar una palabra al azar de la lista de palabras validas
    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
    return palabra.upper()


def ahorcado():
    print("=====***======***=======")
    print("======¡Bienvenido=======")
    print("===========al===========")
    print("===>_-_-AHORCADO-_-_<===")

    palabra = obtener_palabra_valida(palabras)

    letras_por_adivinar = set(palabra)
    abecedario = set(string.ascii_uppercase) #no contine letra ñ
    letras_adivinadas = set()
    
    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")
        #mostrar el estado actual de la palabra
        palabra_lista = [letra if letra in letras_adivinadas
        else '-' for letra in palabra]
        #mostrar estado del ahorcado
        print(vidas_diccionario_visual[vidas])
        #mostrar las letras separadas por un espacio 
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input("Escoge una letra: ").upper()
        #si la letra escogida por el usuario está en el abecedario y no está en el conjunto de letras que ya se han ingresado, se añade la letra al conjunto de letras ingresadas
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            #Si la letra está en la palabra
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else: 
                vidas = vidas -1
                print(f"\nTu letra, {letra_usuario} no está en la palabra.")
        #si la letra escogida por el usuario ya fué ingresada. 
        elif letra_usuario in letras_adivinadas: 
            print("\nYa escogiste esa letra. Por favor escoge una letra nueva. ")
        else:
            print("\nEsta letra no es válida. ")

    #El juego llega a esta línea cuando se adivinan todas las letras 
    #de la palabra o cuando se agotan las vidas del jugador. 
    if vidas == 0: 
        print(f"¡Ahorcado! Perdiste. Lo lamento mucho. La palabra era {palabra}")
    else: 
        print(f"¡Excelente! ¡Adivinaste la palabra: {palabra}!")

ahorcado()
