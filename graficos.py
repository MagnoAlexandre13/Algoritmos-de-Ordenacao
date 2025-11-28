# graficos.py
import pandas as pd
import matplotlib.pyplot as plt

def gerar_graficos(nome_csv):
    df = pd.read_csv(nome_csv)

    # ---------------------------
    # Tempo por tamanho (por algoritmo)
    # ---------------------------
    for alg in df["Algoritmo"].unique():
        subset = df[df["Algoritmo"] == alg]

        plt.figure(figsize=(8,5))
        for tipo in subset["TipoEntrada"].unique():
            dados = subset[subset["TipoEntrada"] == tipo]
            plt.plot(dados["TamanhoN"], dados["TempoSeg"], marker="o", label=tipo)

        plt.title(f"Tempo de Execução - {alg}")
        plt.xlabel("Tamanho N")
        plt.ylabel("Tempo (s)")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.savefig(f"grafico_tempo_{alg}.png")
        plt.close()

    # ---------------------------
    # Comparações por tamanho
    # ---------------------------
    for alg in df["Algoritmo"].unique():
        subset = df[df["Algoritmo"] == alg]

        plt.figure(figsize=(8,5))
        for tipo in subset["TipoEntrada"].unique():
            dados = subset[subset["TipoEntrada"] == tipo]
            plt.plot(dados["TamanhoN"], dados["Comparacoes"], marker="o", label=tipo)

        plt.title(f"Comparações - {alg}")
        plt.xlabel("Tamanho N")
        plt.ylabel("Número de comparações")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.savefig(f"grafico_comparacoes_{alg}.png")
        plt.close()

    # ---------------------------
    # Atribuições por tamanho
    # ---------------------------
    for alg in df["Algoritmo"].unique():
        subset = df[df["Algoritmo"] == alg]

        plt.figure(figsize=(8,5))
        for tipo in subset["TipoEntrada"].unique():
            dados = subset[subset["TipoEntrada"] == tipo]
            plt.plot(dados["TamanhoN"], dados["Atribuicoes"], marker="o", label=tipo)

        plt.title(f"Atribuições - {alg}")
        plt.xlabel("Tamanho N")
        plt.ylabel("Número de atribuições")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.savefig(f"grafico_atribuicoes_{alg}.png")
        plt.close()

    # ============================================================
    # Comparação entre algoritmos NÃO EFICIENTES
    # ============================================================

    nao_eficientes = ["BubbleSort", "InsertionSort", "SelectionSort"]
    df_nao = df[df["Algoritmo"].isin(nao_eficientes)]

    for tipo in df["TipoEntrada"].unique():
        plt.figure(figsize=(8,5))
        for alg in nao_eficientes:
            subset = df_nao[(df_nao["Algoritmo"] == alg) &
                            (df_nao["TipoEntrada"] == tipo)]
            plt.plot(subset["TamanhoN"], subset["TempoSeg"], marker="o", label=alg)

        plt.title(f"Comparação de Tempo (Não Eficientes) - Entrada: {tipo}")
        plt.xlabel("Tamanho N")
        plt.ylabel("Tempo (s)")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.savefig(f"comparacao_nao_eficientes_{tipo}.png")
        plt.close()

    # ============================================================
    # Comparação entre algoritmos EFICIENTES
    # ============================================================

    eficientes = ["QuickSort", "MergeSort", "HeapSort"]
    df_eff = df[df["Algoritmo"].isin(eficientes)]

    for tipo in df["TipoEntrada"].unique():
        plt.figure(figsize=(8,5))
        for alg in eficientes:
            subset = df_eff[(df_eff["Algoritmo"] == alg) &
                            (df_eff["TipoEntrada"] == tipo)]
            plt.plot(subset["TamanhoN"], subset["TempoSeg"], marker="o", label=alg)

        plt.title(f"Comparação de Tempo (Eficientes) - Entrada: {tipo}")
        plt.xlabel("Tamanho N")
        plt.ylabel("Tempo (s)")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.savefig(f"comparacao_eficientes_{tipo}.png")
        plt.close()

    # ============================================================
    # Gráfico grande: TODOS os algoritmos juntos
    # ============================================================

    for tipo in df["TipoEntrada"].unique():
        plt.figure(figsize=(10,6))
        for alg in df["Algoritmo"].unique():
            subset = df[(df["Algoritmo"] == alg) &
                        (df["TipoEntrada"] == tipo)]
            plt.plot(subset["TamanhoN"], subset["TempoSeg"], marker="o", label=alg)

        plt.title(f"Comparação Geral - Tipo de Entrada: {tipo}")
        plt.xlabel("Tamanho N")
        plt.ylabel("Tempo (s)")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.savefig(f"comparacao_geral_{tipo}.png")
        plt.close()

    print("Todos os gráficos foram gerados com sucesso.")