#algoritmos de ordenamiento 
#-------------------------------------------------------------------------------
#1 - burbuja

def ord_burbuja(arreglo):
    n = len(arreglo)

    for i in range(n-1):       # <-- bucle padre
        for j in range(n-1-i): # <-- bucle hijo
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]

elementos = [8, 3, 1, 19, 14]
ord_burbuja(elementos)

print(elementos)
#-------------------------------------------------------------------------------
#2 - quicksort 

def swap(A, i, j):

	temp = A[i]
	A[i] = A[j]
	A[j] = temp

def partition(a, start, end):

	pivot = a[end]
	pIndex = start

	for i in range(start, end):
		if a[i] <= pivot:
			swap(a, i, pIndex)
			pIndex = pIndex + 1

	swap(a, end, pIndex)

	return pIndex

def quicksort(a, start, end):

	if start >= end:
		return

	pivot = partition(a, start, end)
	quicksort(a, start, pivot - 1)
	quicksort(a, pivot + 1, end)

if __name__ == '__main__':

	a = [9, -3, 5, 2, 6, 8, -6, 1, 3]
quicksort(a, 0, len(a) - 1)

print(a)
#-------------------------------------------------------------------------------
#3 - por seleccion 

def seleccion(arreglo):
    longitud = len(arreglo)
    for i in range(longitud-1):
        for j in range(i+1, longitud):
            if arreglo[i] > arreglo[j]:
                # Intercambiar
                arreglo[i], arreglo[j] = arreglo[j], arreglo[i]

def seleccion_descendente(arreglo):
    longitud = len(arreglo)
    for i in range(longitud-1):
        for j in range(i+1, longitud):
            if arreglo[i] < arreglo[j]:
                # Intercambiar
                arreglo[i], arreglo[j] = arreglo[j], arreglo[i]


numeros = [23, 25, 30, 1, 28, 11, 96, 2, 3, 1]
print("Arreglo de números original:")
print(numeros)
seleccion(numeros)
print("Arreglo de números ordenado: ")
print(numeros)
seleccion_descendente(numeros)
print("Arreglo de números ordenado descendente: ")
print(numeros)
#-------------------------------------------------------------------------------
#Algoritmos de busqueda
# 4- binaria 
def busqueda_binaria(lista,valor):
	steps = 0
	izq = 0
	der = len(lista) -1
	while izq <= der:
		steps +=1
		punto_medio =(izq + der) // 2
		if lista[punto_medio] == valor :
			return "valor econtrado en {} pasos, en la posicion {}.".format(steps,punto_medio)
		if lista[punto_medio] > valor:
			der = punto_medio -1
		if lista[punto_medio] < valor:
			izq = lista[punto_medio]  +1
	return "Elemento no econtrado."

lista = [1,2,3,4,5,6,7,8,9,10]
position = busqueda_binaria(lista,10)
print(position)

#-------------------------------------------------------------------------------
#5 - lineal 
valores=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
 
def busquedaLineal(buscar):
   
    for i in range(len(valores)):
        if valores[i]==buscar:
            return (True,i+1)
 
    return (False,i+1)
 
while True:
    buscar=input("indica un numero a buscar: ")
    if buscar=="":
        break
 
    try:
        buscar=int(buscar)
    except:
        print("El valor tienes que ser numero entre 0 y 9")
        continue
 
    conseguido,iteraciones=busquedaLineal(buscar)
    if conseguido:
        print("Encontrado en {} iteraciones".format(iteraciones))
    else:
        print("El valor introducido no se encuentra en la lista de valores. Se han necesitado {} iteraciones".format(iteraciones))
#-------------------------------------------------------------------------------

