from listas_ligadas import lista_ligada


class Conjunto():
    def __init__(self):
        self.__elementos = lista_ligada.ListaLigada()

    def inserir(self, elemento):
        if not self.contem(elemento):
            self.__elementos.inserir(elemento)
            return True
        return False

    def inserir_posicao(self, posicao, elemento):
        if not self.contem(elemento):
            self.__elementos.inserir_na_posicao(posicao, elemento)
            return True
        return False

    def contem(self, elemento):
        return self.__elementos.contem(elemento)

    def indice(self, elemento):
        return self.__elementos.indice(elemento)

    def vazia(self):
        return self.__elementos.vazia()

    def recuperar_elemento(self, posicao):
        return self.__elementos.recuperar_elemento(posicao)

    def recuperar_no(self, posicao):
        return self.__elementos.recuperar_no(posicao)

    def tamanho(self):
        return self.__elementos.tamanho

    def remover_posicao(self, posicao):
        self.__elementos.remover_posicao(posicao)
    
    def remover_elemento(self, elemento):
        self.__elementos.remover_elemento(elemento)

    def __str__(self):
        return self.__elementos.__str__()
