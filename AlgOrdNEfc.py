import random
import numpy as np

def bubble_sort_otimizado(lista):
    n = len(lista)
    
    for i in range(n-1):
        trocou = False
        
        for j in range (n - 1 - i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                trocou = True
                
        if not trocou:
            break
    
    return lista
    
def insertion_sort(lista):
    n = len(lista)
    
    for i in range(1,n):
        chave = lista[i]
        j = i - 1 
        
        while j >= 0 and lista[j] > chave:
            lista[j+1] = lista[j]
            j = j - 1
        lista[j+1] = chave
            
    return lista


def selection_sort(lista):
    n = len(lista)

    for j in range(n-1):
        min_index = j
        for i in range(j,n):
            if lista[i] < lista[min_index]:
                min_index = i 
        if lista[j] > lista[min_index]:
            aux = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = aux

    return lista



n = 10000
valores = np.random.randint(1, 10000, size=n)
print("Lista original:", valores)
print("Lista ordenada:", bubble_sort_otimizado(valores))
print("Lista ordenada com insertion sort:", insertion_sort(valores))
print("Lista ordenada com selection sort:", selection_sort(valores))