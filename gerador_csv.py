# gerador_csv.py
import csv
from algoritmos import executar

def gerar_planilha(nome_arquivo, tamanhos, tipos, algoritmos):
    cabecalho = [
        "Algoritmo", "TipoEntrada", "TamanhoN",
        "Comparacoes", "Atribuicoes", "TempoSeg"
    ]

    with open(nome_arquivo, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(cabecalho)

        for n in tamanhos:
            for nome_tipo, gerador in tipos.items():
                lista = gerador(n)

                for nome_alg, func in algoritmos.items():
                    _, comp, atrib, tempo = executar(func, lista)

                    writer.writerow([
                        nome_alg,
                        nome_tipo,
                        n,
                        comp,
                        atrib,
                        f"{tempo:.8f}"
                    ])

    print(f"Planilha gerada: {nome_arquivo}")
