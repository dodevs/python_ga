'''
    fazer mudanças nos modelos para que funcionem com numeros reais
'''


class Populacao:
    def __init__(self, qtdIndividuos, dominio, fitnessFunc, taxaCrossover, taxaMutacao, keep_blx_beta=True, blx_alpha=0.5):
        self.qtdIndividuos = qtdIndividuos
        self.dominio = dominio
        self.fitnessFunc = fitnessFunc
        self.taxaCrossover = taxaCrossover / 100
        self.taxaMutacao = taxaMutacao / 100
        self.individuos = self._gerarIndividuos()
        self.geracaoAtual = 0
        self.blx_alpha = blx_alpha
        self.keep_blx_beta = keep_blx_beta

    def _gerarIndividuos(self):
        from random import uniform
        return [Individuo(uniform(self.dominio[0], self.dominio[1])) for _ in range(self.qtdIndividuos)]

    # Blend Crossover (BLX-α)
    def _crossover(self, selecionados):
        from random import randint, uniform

        lenS = len(selecionados)
        filhos = []

        i = 0
        while i < lenS:
            pai1 = selecionados[i]
            if i+1 == lenS:
                pai2 = selecionados[lenS * -1]
            else:
                pai2 = selecionados[i+1]

            if uniform(0,1) <= self.taxaCrossover:
                blx_beta = uniform((-1 * self.blx_alpha), (1 + self.blx_alpha))
                novoCromossomo1 = pai1.cromossomo + blx_beta * (pai2.cromossomo - pai1.cromossomo)

                if(not self.keep_blx_beta):
                    blx_beta = uniform((-1 * self.blx_alpha), (1 + self.blx_alpha))

                novoCromossomo2 = pai2.cromossomo + blx_beta * (pai1.cromossomo - pai2.cromossomo)
                filho1 = Individuo(novoCromossomo1)
                filho2 = Individuo(novoCromossomo2)
                filhos.append(filho1)
                filhos.append(filho2)

            else:
                filhos.append(Individuo(pai1.cromossomo))
                filhos.append(Individuo(pai2.cromossomo))

            i+= 2

        #self._elitismo(selecionados, filhos)
        return filhos

    def _selecao(self):
        from random import choice

        selecionados = []

        while len(selecionados) < self.qtdIndividuos:
            desafiante1 = choice(self.individuos)
            desafiante2 = choice(self.individuos)
            selecionados.append(min(desafiante1, desafiante2))

        return selecionados

    # Mutação de Limite
    def _mutacao(self,selecionados):
        from random import uniform

        for individuo in selecionados:
            if(uniform(0,1) <= self.taxaMutacao):
                if (uniform(0,1) < 0.5):
                    individuo.cromossomo = self.dominio[0]
                else:
                    individuo.cromossomo = self.dominio[1]

    def avaliacao(self):
        for individuo in self.individuos:
            individuo.fitness = self.fitnessFunc(individuo.cromossomo)

    def novaGeracao(self):
        selecionados = self._selecao()
        novaGeracao = self._crossover(selecionados)
        self._mutacao(novaGeracao)
        self.individuos = novaGeracao
        self.geracaoAtual += 1
        return min(selecionados)


class Individuo:
    def __init__(self, cromossomo):
        self.cromossomo = cromossomo
        self.fitness = None

    def __eq__(self, value):
        return self.fitness == value.fitness

    def __le__(self, value):
        return self.fitness <= value.fitness

    def __lt__(self, value):
        return self.fitness < value.fitness
