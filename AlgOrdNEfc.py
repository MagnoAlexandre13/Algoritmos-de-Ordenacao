import random
import time
import csv
#import numpy as np


# ================================================================
#  FUNÇÕES DE GERAÇÃO DE DADOS
# ================================================================

def gerar_ordenado(n):
    return list(range(n))

def gerar_invertido(n):
    return list(range(n, 0, -1))

def gerar_aleatorio(n):
    # garante sem repetição
    return random.sample(range(n * 10), n)

def gerar_quase_ordenado(n):
    lista = list(range(n))
    # bagunça cerca de 1% dos elementos
    trocas = max(1, n // 100)
    for _ in range(trocas):
        i = random.randrange(n)
        j = random.randrange(n)
        lista[i], lista[j] = lista[j], lista[i]
    return lista


# ================================================================
#  BUBBLE SORT OTIMIZADO
# ================================================================

def bubble_sort_otimizado(lista):
    lista = lista.copy()

    comparacoes = 0
    atribuicoes = 0

    n = len(lista)
    for i in range(n - 1):
        trocou = False

        for j in range(n - 1 - i):
            comparacoes += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                atribuicoes += 3
                trocou = True

        if not trocou:
            break

    return lista, comparacoes, atribuicoes


# ================================================================
#  INSERTION SORT
# ================================================================

def insertion_sort(lista):
    lista = lista.copy()

    comparacoes = 0
    atribuicoes = 0

    n = len(lista)

    for i in range(1, n):
        chave = lista[i]
        atribuicoes += 1

        j = i - 1
        while j >= 0:
            comparacoes += 1
            if lista[j] > chave:
                lista[j + 1] = lista[j]
                atribuicoes += 1
                j -= 1
            else:
                break
        lista[j + 1] = chave
        atribuicoes += 1

    return lista, comparacoes, atribuicoes


# ================================================================
#  SELECTION SORT
# ================================================================

def selection_sort(lista):
    lista = lista.copy()

    comparacoes = 0
    atribuicoes = 0

    n = len(lista)

    for j in range(n - 1):
        min_index = j

        for i in range(j + 1, n):
            comparacoes += 1
            if lista[i] < lista[min_index]:
                min_index = i

        if min_index != j:
            lista[j], lista[min_index] = lista[min_index], lista[j]
            atribuicoes += 3

    return lista, comparacoes, atribuicoes

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

# ================================================================
#  MERGE SORT
# ================================================================
def merge_sort(lista):
    lista = lista.copy()
    comparacoes = 0
    atribuicoes = 0

    def merge(esq, dir):
        nonlocal comparacoes, atribuicoes
        i = j = 0
        resultado = []

        while i < len(esq) and j < len(dir):
            comparacoes += 1
            if esq[i] <= dir[j]:
                resultado.append(esq[i])
                atribuicoes += 1
                i += 1
            else:
                resultado.append(dir[j])
                atribuicoes += 1
                j += 1

        while i < len(esq):
            resultado.append(esq[i])
            atribuicoes += 1
            i += 1

        while j < len(dir):
            resultado.append(dir[j])
            atribuicoes += 1
            j += 1

        return resultado

    def merge_sort_rec(v):
        if len(v) <= 1:
            return v

        meio = len(v) // 2
        esq = merge_sort_rec(v[:meio])
        dir = merge_sort_rec(v[meio:])
        return merge(esq, dir)

    ordem = merge_sort_rec(lista)
    return ordem, comparacoes, atribuicoes

# ================================================================
#  QUICK SORT
# ================================================================
def quick_sort(lista):
    lista = lista.copy()
    comparacoes = 0
    atribuicoes = 0

    def partition(v, baixo, alto):
        nonlocal comparacoes, atribuicoes
        pivo = v[alto]
        i = baixo - 1

        for j in range(baixo, alto):
            comparacoes += 1
            if v[j] <= pivo:
                i += 1
                v[i], v[j] = v[j], v[i]
                atribuicoes += 3

        v[i+1], v[alto] = v[alto], v[i+1]
        atribuicoes += 3
        return i + 1

    def quick_rec(v, baixo, alto):
        if baixo < alto:
            pi = partition(v, baixo, alto)
            quick_rec(v, baixo, pi - 1)
            quick_rec(v, pi + 1, alto)

    quick_rec(lista, 0, len(lista) - 1)
    return lista, comparacoes, atribuicoes

# ================================================================
#  HEAP SORT
# ================================================================
def heap_sort(lista):
    lista = lista.copy()
    comparacoes = 0
    atribuicoes = 0

    def heapify(v, n, i):
        nonlocal comparacoes, atribuicoes
        maior = i
        esq = 2 * i + 1
        dir = 2 * i + 2

        if esq < n:
            comparacoes += 1
            if v[esq] > v[maior]:
                maior = esq

        if dir < n:
            comparacoes += 1
            if v[dir] > v[maior]:
                maior = dir

        if maior != i:
            v[i], v[maior] = v[maior], v[i]
            atribuicoes += 3
            heapify(v, n, maior)

    n = len(lista)

    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)

    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        atribuicoes += 3
        heapify(lista, i, 0)

    return lista, comparacoes, atribuicoes


# ================================================================
#  FUNÇÃO AUXILIAR PARA MEDIR TEMPO
# ================================================================

def executar(algoritmo, lista):
    ini = time.perf_counter()
    ordenada, comp, atrib = algoritmo(lista)
    fim = time.perf_counter()
    tempo = fim - ini
    return ordenada, comp, atrib, tempo


# ================================================================
#  FUNÇÃO PARA GERAR PLANILHA
# ================================================================

def gerar_planilha(nome_arquivo, tamanhos, tipos, algoritmos):
    cabecalho = [
        "Algoritmo",
        "TipoEntrada",
        "TamanhoN",
        "Comparacoes",
        "Atribuicoes",
        "TempoSeg"
    ]

    with open(nome_arquivo, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(cabecalho)

        for n in tamanhos:
            for nome_tipo, gerador in tipos.items():
                lista_base = gerador(n)

                for nome_alg, func in algoritmos.items():
                    _, comp, atrib, tempo = executar(func, lista_base)

                    writer.writerow([
                        nome_alg,
                        nome_tipo,
                        n,
                        comp,
                        atrib,
                        f"{tempo:.8f}"
                    ])

    print(f"Planilha gerada: {nome_arquivo}")


# ================================================================
#  EXEMPLOS DE TESTE
# ================================================================

if __name__ == "__main__":
    
    tamanhos = [10, 100, 1000]  # ajuste como quiser
    
    tipos = {
        "ordenado": gerar_ordenado,
        "invertido": gerar_invertido,
        "aleatorio": gerar_aleatorio,
        "quase_ordenado": gerar_quase_ordenado
    }
    
    algoritmos = {
        "BubbleSort": bubble_sort_otimizado,
        "InsertionSort": insertion_sort,
        "SelectionSort": selection_sort,
        "QuickSort": quick_sort,
        "MergeSort": merge_sort,
        "HeapSort": heap_sort
    }


    for n in tamanhos:
        print(f"\n==============================")
        print(f" Testando n = {n}")
        print(f"==============================")

        for nome_tipo, gerador in tipos.items():
            lista = gerador(n)
            print(f"\n>> Tipo de entrada: {nome_tipo}")

            for nome_alg, func in algoritmos.items():
                _, comp, atrib, tempo = executar(func, lista)
                print(f"{nome_alg}: Comp={comp} | Atrib={atrib} | Tempo={tempo:.6f}s")

gerar_planilha("resultados_algoritmos.csv", tamanhos, tipos, algoritmos)
