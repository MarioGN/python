class No():
    def __init__(self, elemento, proximo=None):
        self.__elemento = elemento
        self.__proximo = proximo

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


class ListaLigada():
    def __init__(self):
        self.__inicio = None
        self.__fim = None
        self.__tamanho = 0

    @property
    def tamanho(self):
        return self.__tamanho

    def vazia(self):
        return self.__tamanho == 0

    def inserir(self, elemento):
        novo = No(elemento)

        if self.vazia():
            self.__inicio = novo
            self.__fim = novo
        else:
            self.__fim.proximo = novo
            self.__fim = novo
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

    def inserir_na_posicao(self, posicao, elemento):
        if posicao > -1 and posicao <= self.__tamanho:
            novo = No(elemento)
            if posicao == 0:
                novo.proximo = self.__inicio
                self.__inicio = novo
            elif posicao == self.__tamanho:
                self.__fim.proximo = novo
                self.__fim = novo
            else:
                no_anterior = self.recuperar_no(posicao-1)
                no_atual = self.recuperar_no(posicao)
                no_anterior.proximo = novo
                novo.proximo = no_atual
            self.__tamanho += 1

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
                proximo_no = self.__inicio.proximo
                self.__inicio = None
                self.__inicio = proximo_no
            elif posicao == self.__tamanho - 1:
                penultimo_no = self.recuperar_no(self.__tamanho - 2)
                penultimo_no.proximo = None
                self.__fim = penultimo_no
            else:
                no_remover = self.recuperar_no(posicao)
                no_anterior = self.recuperar_no(posicao - 1)
                no_anterior.proximo = no_remover.proximo
                no_remover.proximo = None
            self.__tamanho -= 1

    def remover_elemento(self, elemento):
        no_remover = self.indice(elemento)
        if no_remover == -1:
            print('elemento não existe.')
        else:
            self.remover_posicao(no_remover)

    def __str__(self):
        aux = self.__inicio
        elementos = '['
        while aux:
            elementos = f'{elementos} {aux.elemento}'
            aux = aux.proximo
        elementos =  f'{elementos} ]'
        return elementos
