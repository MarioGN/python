from .no import NoArvore


class NoArvoreInt(NoArvore):
    def __init__(self, valor):
        super().__init__(valor)

    def peso(self):
        return self.valor


class ArvoreInt():
    def __init__(self, raiz=None):
        self.__raiz = raiz

    @property
    def raiz(self):
        return self.__raiz

    def inserir_elemento(self, no):
        if self.__raiz == None:
            self.__raiz = no
        else:
            self.__inserir(self.__raiz, no)

    def __inserir(self, referencia, novo_no):
        if referencia.peso() >= novo_no.peso():
            if referencia.no_esquerdo == None:
                referencia.no_esquerdo = novo_no
            else:
                self.__inserir(referencia.no_esquerdo, novo_no)
        else:
            if referencia.no_direito == None:
                referencia.no_direito = novo_no
            else:
                self.__inserir(referencia.no_direito, novo_no)

    def buscar(self, no_busca):
        return self.__buscar(self.__raiz, no_busca)

    def __buscar(self, referencia, no_busca):
        if referencia.valor == no_busca.valor:
            return referencia
        else:
            if referencia.peso() >= no_busca.peso():
                if referencia.no_esquerdo == None:
                    raise ValueError('Elemento não encontrado')
                else:
                    print('Navegando pela esquerda do nó', referencia.valor.__str__())
                    return self.__buscar(referencia.no_esquerdo, no_busca)
            else:
                if referencia.no_direito == None:
                    raise ValueError('Elemento não encontrado')
                else:
                    print('Navegando pela direira do nó', referencia.valor.__str__())
                    return self.__buscar(referencia.no_direito, no_busca)

    def em_ordem(self):
        # Esq. -> Raiz -> Dir.
        self.__em_ordem(self.__raiz)

    def __em_ordem(self, referencia):
        if referencia.no_esquerdo != None:
            self.__em_ordem(referencia.no_esquerdo)
            print(referencia.valor.__str__())
            if referencia.no_direito != None:
                self.__em_ordem(referencia.no_direito)
        else:
            print(referencia.valor.__str__())
            if referencia.no_direito != None:
                self.__em_ordem(referencia.no_direito)

    def pre_ordem(self):
        # Raiz -> Esq. -> Dir.
        self.__pre_ordem(self.__raiz)

    def __pre_ordem(self, referencia):
        print(referencia.valor.__str__())
        if referencia.no_esquerdo != None:
            self.__pre_ordem(referencia.no_esquerdo)
            if referencia.no_direito != None:
                self.__pre_ordem(referencia.no_direito)
        else:
            if referencia.no_direito != None:
                self.__pre_ordem(referencia.no_direito)

    def pos_ordem(self):
        # Esq. -> Dir. -> Raiz
        self.__pos_ordem(self.__raiz)

    def __pos_ordem(self, referencia):
        if referencia.no_esquerdo != None:
            self.__pos_ordem(referencia.no_esquerdo)
            if referencia.no_direito != None:
                self.__pos_ordem(referencia.no_direito)
            print(referencia.valor.__str__())
        else:
            if referencia.no_direito != None:
                self.__pos_ordem(referencia.no_direito)
                print(referencia.valor.__str__())
            else:
                print(referencia.valor.__str__())

    def altura(self):
        return self.__altura(self.__raiz)

    def __altura(self, referencia):
        if referencia == None:
            return -1
        altura_esquerda = self.__altura(referencia.no_esquerdo)
        altura_direita = self.__altura(referencia.no_direito)
        
        altura = 0
        if altura_esquerda > altura_direita:
            altura = altura_esquerda + 1
        else:
            altura = altura_direita + 1
        return altura

    def __str__(self):
        return "[(X)]" if self.__raiz == None else self.__raiz.__str__()
