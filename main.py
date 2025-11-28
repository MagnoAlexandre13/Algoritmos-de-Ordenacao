# main.py
from algoritmos import *
from gerador_csv import gerar_planilha
from graficos import gerar_graficos

tamanhos = [10, 100, 1000]

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

# 1. Gera CSV
gerar_planilha("resultados_alg.csv", tamanhos, tipos, algoritmos)

# 2. Gera gráficos
gerar_graficos("resultados_alg.csv")
