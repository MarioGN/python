from listas_ligadas import lista_ligada


class TabelaEspalhamento():
    def __init__(self, numero_categorias=10):
        self.__elementos = lista_ligada.ListaLigada()
        self.__numero_categorias = numero_categorias
        self.__tamanho = 0

        for i in range(self.__numero_categorias):
            self.__elementos.inserir(lista_ligada.ListaLigada())

    def __gerar_numero_espalhamento(self, elemento):
        return hash(elemento) % self.__numero_categorias

    def inserir(self, elemento):
        if self.contem(elemento):
            return False
        numero_espalhamento = self.__gerar_numero_espalhamento(elemento)
        categoria = self.__elementos.recuperar_no(numero_espalhamento).elemento
        categoria.inserir(elemento)
        self.__tamanho += 1
        return True

    def contem(self, elemento):
        numero_espalhamento = self.__gerar_numero_espalhamento(elemento)
        categoria = self.__elementos.recuperar_elemento(numero_espalhamento)
        return categoria.contem(elemento)

    def remover(self, elemento):
        numero_espalhamento = self.__gerar_numero_espalhamento(elemento)
        categoria = self.__elementos.recuperar_no(numero_espalhamento).elemento
        categoria.remover_elemento(elemento)
        self.__tamanho -= 1

    def __str__(self):
        return self.__elementos.__str__()
