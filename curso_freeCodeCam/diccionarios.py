'''DICCIONARIOS = COLECCIÓN DE CLAVE VALOR
    Sintaxis: {"A": 45, "B": 30} --->cada uno se denomina Par Clave-Valor
            clav👆val👆          '''
'''Características: 
✅ Colección de Pares Clave-Valor. 
✅ Las claves deben ser 👉únicas e inmutables👈.
✅ Los valores asosciados pueden ser de cualquier tipo. 
✅ La clave se usa para acceder a su valor asociado. 
✅ Los pares Clave-Valor pueden ser modificados, añadidos y eliminados.
'''

#Acceder a un valor en un diccionario: 
#<diccionario>[<clave>]--->resultado que conlleva al valor de la clave. 
edades = {"Carl": 15, "Nora":45}
print(edades["Carl"]) #---> 15
print(edades["Nora"], type(edades)) #---> 45 y el tipo 'dict'

#Otro metodo para obtener el valor: 
gatos = {"tom": 5, "felix": 10, "rifraf": 9}
print("el valor es :", gatos.get("felix", type(gatos))) #--->se obtiene el valor que tiene asignado "felix"(10) y el tipo de dato de "gatos" dict. 

#Modificar el valor: 
#<diccionario>[clave] = <nuevo_valor>
gatos["rifraf"] = 11 #------------->SE AGREGÓ UN NUEVO VALOR!
print(gatos["rifraf"]) #--->11

#Añadir un nuevo Clase-Valor: 
gatos["fiera"] = 15
print("El nuevo Clave-Valor es: ", gatos.get("fiera"), type(gatos["rifraf"])) #--->15
print(gatos)

#OTRO EJEMPLO: 
buses = {"a":5, "b":10, "c":"carl", "d":"zimmerman"}
print(buses.get("c"), type(buses["c"]))

#----->REMOVER------>Sintaxis: del <dicc>[<clave>]------(del significa delete)
resident_evil = {"Leon":34, "Christ":39, "Ada":35, "Jill":33}
print(resident_evil)
del resident_evil["Jill"] #--->Se mandó a eliminar
print(resident_evil)

#------>Revisar Existencia de un elemnto -----Sintaxis: <element> in <dicc>
print("Jill" in resident_evil) #--->false (se comprobó que se eliminó)
print("Leon" in resident_evil) #---->true






