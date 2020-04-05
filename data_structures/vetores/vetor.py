class Vetor():
    def __init__(self, tamanho=0):
        self.__tamanho = tamanho
        self.__elementos = [None] * tamanho
        self.__posicao = 0

    def tamanho(self):
        return len(self.__elementos)

    def inserir_elemento_idx(self, elemento, idx):
        inicio = self.__elementos[:idx] + [None]
        fim = self.__elementos[idx:]

        inicio[len(inicio)-1] = elemento
        self.__elementos = inicio + fim
        self.__tamanho += 1
        self.__posicao = self.__tamanho

    def inserir_elemento_fim(self, elemento):
        if self.__posicao >= self.tamanho():
            self.__elementos += [None]

        self.__elementos[self.__posicao] = elemento
        self.__posicao += 1

    def listar_elemento(self, posicao):
        return self.__elementos[posicao]

    def contem(self, elemento):
        for i in range(self.tamanho()):
            e = self.listar_elemento(i)
            if elemento == e:
                return True
        return False

    def indice(self, elemento):
        for i in range(self.tamanho()):
            e = self.listar_elemento(i)
            if elemento == e:
                return i
        return -1

    def remover_elemento_idx(self, posicao):
        if posicao > -1 and posicao < self.tamanho():
            inicio = self.__elementos[:posicao]
            fim = self.__elementos[posicao+1:]
            self.__elementos = inicio + fim
            self.__posicao -= 1

    def remover_elemento(self, elemento):
        posicao = self.indice(elemento)
        if posicao > -1:
            self.remover_elemento_idx(posicao)

    def __str__(self):
        return ' '.join([str(i) for i in self.__elementos])
