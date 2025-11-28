# main.py
from algoritmos import *
from gerador_csv import gerar_planilha
from graficos import gerar_graficos

# ============================================================
# TAMANHOS USADOS NO TRABALHO
# ============================================================
tamanhos = [10, 1000, 10000]

# ============================================================
# TIPOS DE ENTRADA
# ============================================================
tipos = {
    "ordenado": gerar_ordenado,
    "invertido": gerar_invertido,
    "aleatorio": gerar_aleatorio,
    "quase_ordenado": gerar_quase_ordenado
}

# ============================================================
# ALGORITMOS NÃO EFICIENTES (O(n²))
# ============================================================
algoritmos_lentos = {
    "BubbleSort": bubble_sort_otimizado,
    "InsertionSort": insertion_sort,
    "SelectionSort": selection_sort
}

# Máximo seguro para evitar travamento
LIMITE_LENTOS = 1000  # NÃO EXECUTE bubble/insertion/selection acima disso

# ============================================================
# ALGORITMOS EFICIENTES
# ============================================================
algoritmos_rapidos = {
    "QuickSort": quick_sort,
    "MergeSort": merge_sort,
    "HeapSort": heap_sort
}

# ============================================================
# Função auxiliar para determinar limite de elementos exibidos
# ============================================================
def limite_para(n):
    if n == 10:
        return 10
    elif n == 1000:
        return 200
    else:
        return 200

# ============================================================
# Gera arquivo TXT com antes/depois
# ============================================================
def gerar_relatorio_txt(nome_arquivo, tamanhos, tipos, algoritmos_lentos, algoritmos_rapidos):
    with open(nome_arquivo, "w") as f:
        f.write("RELATÓRIO DE LISTAS ANTES E DEPOIS DA ORDENAÇÃO\n")
        f.write("============================================================\n\n")

        for n in tamanhos:
            for nome_tipo, gerador in tipos.items():

                lista_original = gerador(n)
                limite = limite_para(n)

                # ------------------------------------------------------------
                # ALGORITMOS NÃO EFICIENTES — rodar somente até LIMITE_LENTOS
                # ------------------------------------------------------------
                if n <= LIMITE_LENTOS:
                    for nome_alg, func in algoritmos_lentos.items():
                        ordenada, _, _, _ = executar(func, lista_original)

                        f.write("============================================================\n")
                        f.write(f"Algoritmo: {nome_alg}\n")
                        f.write(f"Tipo de entrada: {nome_tipo}\n")
                        f.write(f"Tamanho: {n}\n")
                        f.write("------------------------------------------------------------\n")

                        # ANTES
                        antes = lista_original[:limite]
                        f.write(f"ANTES ({len(antes)} primeiros elementos): {antes}")
                        if len(lista_original) > limite:
                            f.write(" ...")
                        f.write("\n\n")

                        # DEPOIS
                        depois = ordenada[:limite]
                        f.write(f"DEPOIS ({len(depois)} primeiros elementos): {depois}")
                        if len(ordenada) > limite:
                            f.write(" ...")
                        f.write("\n\n")

                # ------------------------------------------------------------
                # ALGORITMOS EFICIENTES — sempre executam todos os tamanhos
                # ------------------------------------------------------------
                for nome_alg, func in algoritmos_rapidos.items():
                    ordenada, _, _, _ = executar(func, lista_original)

                    f.write("============================================================\n")
                    f.write(f"Algoritmo: {nome_alg}\n")
                    f.write(f"Tipo de entrada: {nome_tipo}\n")
                    f.write(f"Tamanho: {n}\n")
                    f.write("------------------------------------------------------------\n")

                    # ANTES
                    antes = lista_original[:limite]
                    f.write(f"ANTES ({len(antes)} primeiros elementos): {antes}")
                    if len(lista_original) > limite:
                        f.write(" ...")
                    f.write("\n\n")

                    # DEPOIS
                    depois = ordenada[:limite]
                    f.write(f"DEPOIS ({len(depois)} primeiros elementos): {depois}")
                    if len(ordenada) > limite:
                        f.write(" ...")
                    f.write("\n\n")

        print(f"Arquivo TXT gerado: {nome_arquivo}")

# ============================================================
# FUNÇÃO PARA CRIAR MAPA COMPLETO DE ALGORITMOS → CSV
# ============================================================
def algoritmos_para_csv():
    algs = {}

    # Os lentos só entram se tiver N pequeno
    for nome, func in algoritmos_lentos.items():
        algs[nome] = func

    # Os rápidos sempre entram
    for nome, func in algoritmos_rapidos.items():
        algs[nome] = func

    return algs

# ============================================================
# 1. GERAR RELATÓRIO TXT
# ============================================================
gerar_relatorio_txt("relatorio_listas.txt", tamanhos, tipos, algoritmos_lentos, algoritmos_rapidos)

# ============================================================
# 2. GERAR CSV
# ============================================================
gerar_planilha(
    "resultados_alg.csv",
    tamanhos,
    tipos,
    algoritmos_para_csv()
)

# ============================================================
# 3. GERAR GRÁFICOS
# ============================================================
gerar_graficos("resultados_alg.csv")
