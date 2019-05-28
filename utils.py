import matplotlib.pyplot as plt

def plotaResultados(numeroExecucoes, qtdGeracoes, qtdIndividuos):
    plot_y_media = []
    plot_y_melhor = []
    plot_x = [] # iteracao

    for execucao in range(numeroExecucoes):
        media_execucao = 0
        menor_execucao = float('inf') #Valor infinito

        for geracao in range(qtdGeracoes):
            soma_geracao = 0
            menor_geracao = float('inf')
            
            file = open("resultados/{0}_{1}_{2}.txt".format(execucao, geracao, qtdIndividuos), 'r')
            fitness = file.readline()
            while fitness != "":
                fitness_float = float(fitness)

                soma_geracao += fitness_float
                if fitness_float < menor_geracao:
                    menor_geracao = fitness_float

                fitness = file.readline()
            
            media_execucao += soma_geracao/qtdGeracoes
            if menor_geracao < menor_execucao:
                menor_execucao = menor_geracao

        plot_x.append(execucao)
        plot_y_media.append(media_execucao)
        plot_y_melhor.append(menor_execucao)

    # PyPloat Config
    plt.title('Algoritmo Genético')
    plt.xlabel('Execucão')
    plt.ylabel('Fitness')
    media_line, = plt.plot(plot_x, plot_y_media, color='y')
    best_line, = plt.plot(plot_x, plot_y_melhor, color='g')
    plt.legend([media_line, best_line], ['Média; Ultima execução: {0}'.format(plot_y_media[-1]), 'Melhor; Ultima execução: {0}'.format(plot_y_melhor[-1])])

    #plt.ylim(-10, 10)
    plt.xticks(plot_x)
    plt.show()

def mediaIndividuos(individuos, qtdIndividuos):
    soma_fitness = 0
    for individuo in individuos:
        soma_fitness += individuo.fitness

    return soma_fitness/qtdIndividuos

def salvaResultado(execucao, geracao, individuos):
    file = open("resultados/{0}_{1}_{2}.txt".format(execucao, geracao, len(individuos)), "w")
    for individuo in individuos:
        file.write("{0}\n".format(individuo.fitness))

    file.close()