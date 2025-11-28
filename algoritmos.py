# algoritmos.py
import random
import time

# -----------------------------
# Geradores de entrada
# -----------------------------
def gerar_ordenado(n):
    return list(range(n))

def gerar_invertido(n):
    return list(range(n, 0, -1))

def gerar_aleatorio(n):
    return random.sample(range(n * 10), n)

def gerar_quase_ordenado(n):
    lista = list(range(n))
    trocas = max(1, n // 100)
    for _ in range(trocas):
        i = random.randrange(n)
        j = random.randrange(n)
        lista[i], lista[j] = lista[j], lista[i]
    return lista

# -----------------------------
# Algoritmos não eficientes
# -----------------------------
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

# -----------------------------
# Algoritmos eficientes
# -----------------------------
def merge_sort(lista):
    lista = lista.copy()

    def rec(v):
        # se tiver só 1 elemento, não há operação
        if len(v) <= 1:
            return v, 0, 0

        meio = len(v) // 2

        # ordenar metade esquerda
        esq, comp_esq, atrib_esq = rec(v[:meio])
        # ordenar metade direita
        dir, comp_dir, atrib_dir = rec(v[meio:])

        # mesclar
        i = j = 0
        resultado = []
        comp_merge = 0
        atrib_merge = 0

        while i < len(esq) and j < len(dir):
            comp_merge += 1
            if esq[i] <= dir[j]:
                resultado.append(esq[i])
                atrib_merge += 1
                i += 1
            else:
                resultado.append(dir[j])
                atrib_merge += 1
                j += 1

        while i < len(esq):
            resultado.append(esq[i])
            atrib_merge += 1
            i += 1

        while j < len(dir):
            resultado.append(dir[j])
            atrib_merge += 1
            j += 1

        return (
            resultado,
            comp_esq + comp_dir + comp_merge,
            atrib_esq + atrib_dir + atrib_merge
        )

    ordenada, comp_total, atrib_total = rec(lista)
    return ordenada, comp_total, atrib_total



def quick_sort(lista):
    lista = lista.copy()
    comparacoes = 0
    atribuicoes = 0

    import random

    def partition(v, baixo, alto):
        nonlocal comparacoes, atribuicoes

        # escolher pivô aleatório
        pivo_index = random.randint(baixo, alto)
        v[pivo_index], v[alto] = v[alto], v[pivo_index]
        atribuicoes += 3

        pivo = v[alto]
        i = baixo - 1

        for j in range(baixo, alto):
            comparacoes += 1
            if v[j] <= pivo:
                i += 1
                v[i], v[j] = v[j], v[i]
                atribuicoes += 3

        v[i + 1], v[alto] = v[alto], v[i + 1]
        atribuicoes += 3

        return i + 1

    def rec(v, baixo, alto):
        if baixo < alto:
            p = partition(v, baixo, alto)
            rec(v, baixo, p - 1)
            rec(v, p + 1, alto)

    rec(lista, 0, len(lista) - 1)
    return lista, comparacoes, atribuicoes


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
                atribuicoes += 1
        
        if dir < n:
            comparacoes += 1
            if v[dir] > v[maior]:
                maior = dir
                atribuicoes += 1

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

# -----------------------------
# Função executar
# -----------------------------
def executar(algoritmo, lista):
    ini = time.perf_counter()
    ordenada, comp, atrib = algoritmo(lista)
    fim = time.perf_counter()
    return ordenada, comp, atrib, fim - ini
