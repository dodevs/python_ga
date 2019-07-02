import matplotlib.pyplot as plt

def plotaResultados(numeroExecucoes, qtdGeracoes, qtdIndividuos):
    plot_y_media = []
    plot_y_melhor = []
    plot_x = [] # iteracao

    menor_execucoes = [0, float('inf')]

    for execucao in range(numeroExecucoes):
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
            
            file.close()

            if menor_geracao < menor_execucao:
                menor_execucao = menor_geracao

        plot_x.append(execucao)
        plot_y_melhor.append(menor_execucao)

        if menor_execucao < menor_execucoes[1]:
            menor_execucoes[1] = menor_execucao
            menor_execucoes[0] = execucao

    # PyPloat Config
    plt.title('Algoritmo Genético Binário')
    plt.xlabel('Execucão')
    plt.ylabel('Fitness')
    best_line, = plt.plot(plot_x, plot_y_melhor, color='g')
    plt.legend([best_line], ['Melhor de cada execução'])
    plt.annotate('Melhor das execucoes\n{0}'.format(menor_execucoes[1]), xy=menor_execucoes, xytext=(menor_execucoes[0], menor_execucoes[1] + (max(plot_y_melhor) - menor_execucoes[1]) / 2), arrowprops=dict(facecolor='black', shrink=0.05))
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