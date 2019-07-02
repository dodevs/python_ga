from models import Populacao
from utils import salvaResultado, mediaIndividuos, plotaResultados

def fitness(x):
    return x ** 2 - 3 * x + 4

def main():
    numero_execucoes = 10
    numero_geracoes = 5

    for execucao in range(numero_execucoes):
        # Parametros: qtdIndividuos, dominio, funcao fitness, precisao, taxa crossover, taxa mutacao
        populacao = Populacao(
            qtdIndividuos=4,
            dominio=[-10,10],
            fitnessFunc=fitness,
            taxaCrossover=60,
            taxaMutacao=1,
            keep_blx_beta=True, # Se True, mantém o mesmo valor de Beta para todos filhos de um crossover
            blx_alpha=0.5 # Se keep_blx_beta == True, aumenta a região de possiveis filhos ao redor do pai
        )
        populacao.avaliacao()

        while populacao.geracaoAtual < numero_geracoes:
            salvaResultado(execucao, populacao.geracaoAtual, populacao.individuos)

            # Ciclo do algoritmo
            populacao.novaGeracao()
            populacao.avaliacao()

    plotaResultados(numero_execucoes, numero_geracoes, populacao.qtdIndividuos)

if __name__ == "__main__":
    main()
