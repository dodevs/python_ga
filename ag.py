from models import Populacao
from utils import salvaResultado, mediaIndividuos, plotaResultados

def fitness(x):
    return x ** 2 - 3 * x + 4

def main():
    numero_execucoes = 1
    numero_geracoes = 50

    for execucao in range(numero_execucoes):
        # Parametros: qtdIndividuos, dominio, funcao fitness, precisao, taxa crossover, taxa mutacao
        populacao = Populacao(4, [-10,10], fitness, 100000, 60, 10)
        populacao.avaliacao()

        while populacao.geracaoAtual < numero_geracoes:
            #salvaResultado(execucao, populacao.geracaoAtual, populacao.individuos)

            # Ciclo do algoritmo
            populacao.novaGeracao()
            populacao.avaliacao()

    #plotaResultados(numero_execucoes, numero_geracoes, populacao.qtdIndividuos)

if __name__ == "__main__":
    main()
