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


class Fila():
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
            self.__fim = novo
        self.__tamanho += 1

    def remover(self):
        removido = None
        if not self.vazia():
            removido = self.__inicio.elemento
            if self.__inicio == self.__fim:
                self.__fim = None
            self.__inicio = self.__inicio.proximo
            self.__tamanho -= 1
        else:
            print('fila vazia!')
        return removido

    def __str__(self):
        aux = self.__inicio
        elementos = ''
        while aux:
            elementos = f'{elementos} {aux.elemento}'
            aux = aux.proximo
        
        return elementos