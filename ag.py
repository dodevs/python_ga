from models import Populacao
from utils import salvaResultado, mediaIndividuos, plotaResultados

def fitness(x):
    return x ** 2 - 3 * x + 4

def main():
    import matplotlib.pyplot as plt
    from time import sleep
    from functools import reduce

    numero_execucoes = 10
    numero_geracoes = 10

    for execucao in range(numero_execucoes):
        # Parametros: qtdIndividuos, dominio, funcao fitness, precisao, taxa crossover, taxa mutacao
        populacao = Populacao(4, [-10,10], fitness, 10, 60, 1)
        populacao.avaliacao()

        while populacao.geracaoAtual < numero_geracoes:
            salvaResultado(execucao, populacao.geracaoAtual, populacao.individuos)

            # Ciclo do algoritmo
            #menorDaSelecao = populacao.novaGeracao() #elitismo?
            populacao.novaGeracao()
            populacao.avaliacao()

            #piorDaNovaGeracao = max(populacao.individuos)
            #if piorDaNovaGeracao > menorDaSelecao:
            #    populacao.individuos[populacao.individuos.index(piorDaNovaGeracao)] = menorDaSelecao

    plotaResultados(numero_execucoes, numero_geracoes, populacao.qtdIndividuos)

if __name__ == "__main__":
    main()
