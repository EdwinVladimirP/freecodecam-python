#Este juego es una practica de como puedes concatenar cadenas de caracteres

'''Mad Libs - Historias Locas 

Es un juego en el que tenemos un parrafo y en ese parrafo tenemos espacios en blanco que vamos a llenar con ciertas palabras. sustantivos, verbos, adjetivos.Esas palabras se las vamos a pedir al jugador y luego se le mostrará su historia loca. 
'''

#Supongamos que queremos crear una cadena que diga: 

#Aprende a programar con __________.

#organización = "freeCodeCamp"
#print("Aprende a programar con " + organización)         #--->codigo limpio.
#print("Aprende a programar con {}".format(organización)) #--->utilizando un método.
#print(f"Aprende a programar con {organización}")         #---> f-string --->la manera idónea. 


#Mad Libs (Historias Locas)

adj = input("Adjetivo: ")
verbo1 = input("Verbo 1: ")
verbo2 = input("Verbo 2: ")
sustantivo_plural = input("Sustantivo plural: ")

madlib = f"¡Programar es tan {adj}! Siempre me emociona porque me encanta {verbo1} problemas. ¡Aprende a {verbo2} con freeCodeCamp y alcanza tus {sustantivo_plural}! "
print(madlib)