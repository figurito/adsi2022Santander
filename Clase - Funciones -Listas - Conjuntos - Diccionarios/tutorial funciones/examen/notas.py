'''Objetivos

Crear un cuaderno Google Colaboratory 
Nombrar el cuaderno con tu nombre+apellido+adsinumeroficha 
Experimentar el siguiente código en Python en el cuaderno.

Escenario

Escribir un programa que pida a un aprendiz las 5 notas de la clase de programación en python, los almacene en una lista, los muestre por pantalla ordenadas de mayor a menor.

Tu tarea es:

Ingresar por teclado las notas

Agregar las notas a una lista

Imprimir de Mayor a menor las 5 notas

notas=[]
for x in range(5):
    n=float(input('Ingresar Nota : '))
    notas.append(n)
notas.sort() 
notas.reverse() 
print(notas)
'''
miLista=[]
for x in range(5):
    n=float(input('Ingresar Nota : '))
    miLista.append(n)

swapped = True # lo necesitamos verdadero (True) para ingresar al bucle while

while swapped:
    swapped = False # no hay swaps hasta ahora
    for i in range(len(miLista) - 1):
        if miLista[i] < miLista[i + 1]:
            swapped= True # ocurrió el intercambio!
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

print(miLista)