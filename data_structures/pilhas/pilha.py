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


class Pilha():
    def __init__(self):
        self.__inicio = None
        self.__tamanho = 0

    def vazia(self):
        return self.__tamanho == 0

    def empilhar(self, elemento):
        novo = No(elemento)
        novo.proximo = self.__inicio
        self.__inicio = novo
        self.__tamanho += 1

    def desempilhar(self):
        removido = None
        if not self.vazia():
            removido = self.__inicio.elemento
            self.__inicio = self.__inicio.proximo
            self.__tamanho -= 1
        else:
            print('pilha vazia!')
        return removido
        

    def __str__(self):
        aux = self.__inicio
        elementos = ''
        while aux:
            elementos = f'{elementos} {aux.elemento}'
            aux = aux.proximo
        
        return elementos
