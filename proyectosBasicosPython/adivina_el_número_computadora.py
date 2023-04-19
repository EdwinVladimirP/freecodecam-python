'''ADIVINA EL NÚMERO (computadora)

La computadora deberá adivinar el número'''

import random

def adivina_el_número_computadora(x):

    print("===============***=================")
    print("===--->¡Bienvenid@ al Juego!<---===")
    print("===============***=================")
    print(f"Selecciona un número entre 1 y {x} para que la computadora intente adivinarlo") #--->f-string

    limite_inferior = 1 #--->es lo mismo [1, x]
    limite_superior = x #--->es lo mismo [1, x]

    respuesta = ""

    while respuesta != "c":
        #Generar predicción
        if limite_inferior != limite_superior: # [1, 10]
            predicción = random.randint(limite_inferior, limite_superior)
        else:
            predicción = limite_inferior #también podría ser el límite superior. 

            #Obtener respuesta del usuario
        respuesta = input(f"Mi predicción es: {predicción}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcta, ingresa (C): ").lower() #-------------->lower brindará letra minúscula para evitar conflicto entre ingreso de mayusculas ó minúsculas. 

        if respuesta == "a":
                limite_superior = predicción - 1
        elif respuesta == "b":
                limite_inferior = predicción + 1
    print(f"¡Siiii! La computadora adivinó tu número correctamente: {predicción}")

adivina_el_número_computadora(10)





