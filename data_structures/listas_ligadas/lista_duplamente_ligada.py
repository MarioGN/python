class No():
    def __init__(self, elemento, proximo=None, anterior=None):
        self.__elemento = elemento
        self.__proximo = proximo
        self.__anterior = anterior

    @property
    def elemento(self):
        return self.__elemento
    
    @elemento.setter
    def elemento(self, elemento):
        self.__elemento = elemento

    @property
    def proximo(self):
        return self.__proximo
    
    @proximo.setter
    def proximo(self, proximo):
        self.__proximo = proximo

    @property
    def anterior(self):
        return self.__anterior
    
    @anterior.setter
    def anterior(self, anterior):
        self.__anterior = anterior


class ListaDuplamenteLigada():
    def __init__(self):
        self.__inicio = None
        self.__fim = None
        self.__tamanho = 0

    def vazia(self):
        return self.__tamanho == 0

    def inserir(self, elemento):
        novo = No(elemento)

        if self.vazia():
            self.__inicio = novo
            self.__fim = novo
        else:
            self.__fim.proximo = novo
            novo.anterior = self.__fim
            self.__fim = novo
        self.__tamanho += 1

    def inserir_na_posicao(self, posicao, elemento):
        if posicao > -1 and posicao <= self.__tamanho:
            novo = No(elemento)
            if posicao == 0:
                novo.proximo = self.__inicio
                self.__inicio.anterior = novo
                self.__inicio = novo
            elif posicao == self.__tamanho:
                self.__fim.proximo = novo
                novo.anterior = self.__fim
                self.__fim = novo
            else:
                anterior = self.recuperar_no(posicao-1)
                atual = anterior.proximo

                anterior.proximo = novo
                novo.anterior = anterior
                atual.anterior = novo
                novo.proximo = atual
            self.__tamanho += 1

    def recuperar_no(self, posicao):
        resultado = None
        if posicao > -1 and posicao < self.__tamanho:
            for i in range(posicao + 1):
                if i == 0:
                    resultado = self.__inicio
                else:
                    resultado = resultado.proximo

        return resultado

    def recuperar_elemento(self, posicao):
        no = self.recuperar_no(posicao)
        if no:
            return no.elemento
        return no

    def contem(self, elemento):
        for i in range(self.__tamanho):
            no_atual = self.recuperar_no(i)
            if no_atual.elemento == elemento:
                return True
        return False

    def indice(self, elemento):
        for i in range(self.__tamanho):
            no_atual = self.recuperar_no(i)
            if no_atual.elemento == elemento:
                return i
        return -1

    def remover_posicao(self, posicao):
        if posicao > -1 and posicao < self.__tamanho:
            if posicao == 0:
                proximo = self.__inicio.proximo
                self.__inicio.proximo = None
                proximo.anterior = None
                self.__inicio = proximo
            elif posicao == self.__tamanho - 1:
                penultimo = self.__fim.anterior
                penultimo.proximo = None
                self.__fim.anterior = None
                self.__fim = penultimo
            else:
                removido = self.recuperar_no(posicao)
                anterior = removido.anterior
                proximo = removido.proximo
                anterior.proximo = proximo
                proximo.anterior = anterior
                removido.proximo = None
                removido.anterior = None
            self.__tamanho -= 1

    def remover_elemento(self, elemento):
        no_remover = self.indice(elemento)
        if no_remover == -1:
            print('elemento não existe.')
        else:
            self.remover_posicao(no_remover)

    def __str__(self):
        aux = self.__inicio
        elementos = ''
        while aux:
            elementos = f'{elementos} {aux.elemento}'
            aux = aux.proximo
        
        return elementos
