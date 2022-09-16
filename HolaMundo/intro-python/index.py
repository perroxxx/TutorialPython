#aca irá un comentario mish
from calendar import c
from subprocess import list2cmdline


#if 3 > 5:#comentario
    #print('Esto no se imprime we')
#if 5 > 3:#comentario
    #print('5 es mayor a 3')
x = 5
y = 'Palabra'

#print(x,y)#la coma concatena

email ="chanchitofeliz@gmail.com"
#print(email)

#print(x,y, ' ', email)

mi_Var='chanchito dijo el profe xd'
#if x+5 > 9:
    #print('Funciona?')
inicio, final = 'Hola', 'mundo'

#print(inicio + final)#concatena literalmente es decir HolaMundo
#print(inicio, final)#concatena? pero añadiendo un espacio es decir hola mundo
#String
palabra ='Hola mundo'
oracion = "Hola mundo comilla doble"
#Enteros
entero = 20 #integer
#double es decir decimales
conDecimales =20.2#float
#N°complejos
complejo = 1j #
#print(palabra, oracion, entero, conDecimales, complejo)

list= [1,2,3]#listas xD
print(list)
list.append(4)#agregar datos a nuestra lista
print(list)
lista2 = list.copy()#dependiendo de cuando se llame es diferente lo q puede mostrar
#list.clear()
print(lista2)
list.append(99)
print(list)
#print(list, 'El numero 3 se esta repitiendo:', lista2.count(3), 'vez o veces')
#print ('list posee',len(list), 'elementos')
larglist = len(list)
largLista2 = len(lista2)

#print(larglist + largLista2)#concatena y al ser del mismo tipo suma xD
#print(list(2))
#list.pop() #elimina el ultimo elemento de la lista
#list.pop()
#print(list)
list.remove(3)#elimina elemento por su valor
#print (list)
list.append(999)
#print(list)
#list.reverse()#invierte la lista
#print(list)
#list.append("Hola")
#print(list)
#list.remove("Hola")
#print(list)
#list.sort()#Ordenar lista (deben ser del mismo tipo de datos)
#print(list)
tupla=('hola', 'mundo', 'somos','tupla')#posee menos metodos que lista
print(tupla[0])#no se pueden modificar a no ser q se transformen en listas
listaDeTupla =list(tupla)
print (listaDeTupla)

rango = range(6)#6 es la longitud del rango
print(rango)

