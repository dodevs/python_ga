class Populacao:
    def __init__(self, qtdIndividuos, dominio, fitnessFunc, precisao, taxaCrossover, taxaMutacao):
        self.qtdIndividuos = qtdIndividuos
        self.dominio = dominio
        self.precisao = precisao
        self.fitnessFunc = fitnessFunc
        self.taxaCrossover = taxaCrossover / 100
        self.taxaMutacao = taxaMutacao / 100
        self.individuos = self._gerarIndividuos()
        self.geracaoAtual = 0

    def _gerarIndividuos(self):
        from random import randint
        return [
            Individuo(
                [randint(0,1) for _ in range(self.precisao)]
            ) for _ in range(self.qtdIndividuos)
        ]

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

                pontoDeCorte = randint(0, self.precisao)
                novoCromossomo1 = pai1.cromossomo[:pontoDeCorte] + pai2.cromossomo[pontoDeCorte:]
                novoCromossomo2 = pai2.cromossomo[:pontoDeCorte] + pai1.cromossomo[pontoDeCorte:]
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

    def _mutacao(self,selecionados):
        from random import uniform

        for individuo in selecionados:
            for i in range(self.precisao):
                if(uniform(0,1) <= self.taxaMutacao):
                    individuo.cromossomo[i] = int(not individuo.cromossomo[i])

    def _normalizacao(self, cromossomo):
        valorNormalizado = (self.dominio[0] + (self.dominio[1] - self.dominio[0])) * cromossomo / (2 ** self.precisao - 1)
        return valorNormalizado

    def avaliacao(self):
        for individuo in self.individuos:
            valorNormalizado = self._normalizacao(individuo.cromossomo_int())
            individuo.fitness = self.fitnessFunc(valorNormalizado)

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

    def cromossomo_str(self):
        return ''.join(map(str, self.cromossomo))

    def cromossomo_int(self):
        return int(self.cromossomo_str(), 2)
