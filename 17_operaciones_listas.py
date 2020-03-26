#Operacions con listas
mi_lista = []
type(mi_lista)

mi_lista.append(1)

mi_lista2 = [2,3,4]
mi_lista3 = mi_lista + mi_lista2
mi_lista3 #nueva lista que contiene todos los valores de las otras dos listas

mi_lista4 = ['a']
mi_lista5 = mi_lista4 * 10
mi_lista5 # 10 veces letra a

mi_lista5 / 5   #error, operador de division no se peude usar con tipo lista y eneterop

#Probando slice
lista = [1,2,3,4,5,6]
lista[:1] #[2,3,4,5,6]
lista[1:3] #[2,3]
lista[1:6:2] #[2,4,6]
lista[:-1] #[6,5,4,3,2,1]

#modificacion , las listas si son mutables
# appende agrega elemento al final
# pop eliminar ultimo elemento de la lista
nombre = mi_lista.pop()
#sort ordenar lista
#extend 
mi_lista.extend(mi_lista2)
# eliminar 
utiles = ['lapiz','calculadora','cuaderno']
del utiles[0] #borra primer elemento

casa = 'casa'
type(casa) #str
lista_casa = list(casa) # ['c','a','s', 'a']

str_casa = ''.join(lista_casa)