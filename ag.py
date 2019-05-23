'''
Objetivo: Minimizar f(x)=x²−3x+4
Critérios
    Dominio: x∈[−10,+10];
    Criar uma população inicial com 4 indivíduos;
    Usar seleção por torneio (n = 2);
    Aplicar Crossover com taxa de 60% (Crossover de 1 ponto uniforme);
    Aplicar Mutação com taxa de 1%;
    Usar 5 gerações e 10 gerações;
    Normalizacao:
        x = min + (max-min) * (b10/2l - 10), onde:
            b10 = binario(cromossomo) na base 10
            2l = 2 elevado ao numero de bits

1. Gerar a população inicial.
2. Avaliar cada indivíduo da população.
3. Enquanto critério de parada não for satisfeito faça
    3.1  Selecionar os indivíduos mais aptos.
    3.2  Criar novos indivíduos aplicando os operadores
        crossover e mutação.
    3.3  Armazenar os novos indivíduos em umanova população.
    3.4 Avaliar cada indivíduo da nova população.
'''

class Populacao:
    def __init__(self, qtdIndividuos, dominio, fitnessFunc, precisao):
        self.qtdIndividuos = qtdIndividuos
        self.dominio = dominio
        self.precisao = precisao
        self.fitnessFunc = fitnessFunc
        self.individuos = self._gerarIndividuos()
        self.geracaoAtual = 0

    def _gerarIndividuos(self):
        from random import randint
        return [
            Individuo(
                ''.join(map(str, [randint(0,1) for _ in range(self.precisao)])) #Binario
            ) for _ in range(self.qtdIndividuos)
        ]

    def _normalizacao(self, cromossomo):
        valor = int(cromossomo, 2)
        valorNormalizado = self.dominio[0] + (self.dominio[1] - self.dominio[0]) * (valor / (2 ** self.precisao - 1))
        return valorNormalizado

    def _crossover(self, selecionados):
        from random import randint, uniform

        lenS = len(selecionados)
        filhos = []

        for i in range(lenS):
            if uniform(0,1) <= 0.6:
                pai1 = selecionados[i].cromossomo
                if i == lenS - 1:
                    pai2 = selecionados[lenS * -1].cromossomo
                else:
                    pai2 = selecionados[i+1].cromossomo

                pontoDeCorte = randint(0, self.precisao)
                novoCromossomo = pai1[pontoDeCorte:] + pai2[:pontoDeCorte]
                novoFilho = Individuo(novoCromossomo)
                filhos.append(novoFilho)

        return filhos


    def _selecao(self):
        from random import choice

        selecionados = []

        while len(selecionados) <= 4:
            desafiante1 = choice(self.individuos)
            desafiante2 = choice(self.individuos)
            selecionados.append(min(desafiante1, desafiante2))

        return selecionados

    def avaliacao(self):
        for individuo in self.individuos:
            valorNormalizado = self._normalizacao(individuo.cromossomo)
            individuo.fitness = self.fitnessFunc(valorNormalizado)

    def novaGeracao(self):
        selecionados = self._selecao()
        novaGeracao = self._crossover(selecionados)
        self.individuos = novaGeracao
        self.geracaoAtual += 1


class Individuo:
    def __init__(self, cromossomo: str):
        self.cromossomo = cromossomo
        self.fitness = None

    def __eq__(self, value):
        return self.fitness == value.fitness

    def __le__(self, value):
        return self.fitness <= value.fitness

    def __lt__(self, value):
        return self.fitness < value.fitness


def fitness(x):
    return x ** 2 - 3 * x + 4

def main():
    populacao = Populacao(4, [-10,10], fitness, 10)
    populacao.avaliacao()

    while populacao.geracaoAtual <= 10:
        populacao.novaGeracao()
        populacao.avaliacao()

    print(min(populacao.individuos).fitness)

if __name__ == "__main__":
    main()
