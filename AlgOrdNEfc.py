import random
import time
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

def ordenado(n):
    return list(range(n))

def inverso(n):
    return list(range(n-1, -1, -1))

def quase_ordenado(n):
    v = list(range(n))
    # faz 2 trocas aleatórias só para bagunçar um pouco
    for _ in range(2):
        i = random.randint(0, n-1)
        j = random.randint(0, n-1)
        v[i], v[j] = v[j], v[i]
    return v

def aleatorio(n):
    v = list(range(n))
    random.shuffle(v)
    return v


# ---------------- TESTE SIMPLES ----------------

n = 5000  # escolhendo 10 para ficar fácil de ver

tipos = {
    "Ordenado": ordenado(n),
    "Inverso": inverso(n),
    "Quase ordenado": quase_ordenado(n),
    "Aleatório": aleatorio(n)
}

for nome, vetor in tipos.items():
    print("\n===============================")
    print("Tipo de sequência:", nome)
    print("Antes:", vetor)

    # Bubble
    '''inicio = time.perf_counter()
    out_bubble = bubble_sort_otimizado(vetor)
    fim = time.perf_counter()
    print("Bubble Sort:   ", out_bubble, f"(tempo: {fim - inicio:.6f}s)")'''

    '''# Selection
    inicio = time.perf_counter()
    out_sel = selection_sort(vetor)
    fim = time.perf_counter()
    print("Selection Sort:", out_sel, f"(tempo: {fim - inicio:.6f}s)")'''

    # Insertion
    inicio = time.perf_counter()
    out_ins = insertion_sort(vetor)
    fim = time.perf_counter()
    print("Insertion Sort:", out_ins, f"(tempo: {fim - inicio:.6f}s)")