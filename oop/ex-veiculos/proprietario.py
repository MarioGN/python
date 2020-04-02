from endereco import Endereco


class Proprietario():
    def __init__(self, nome, CPF, RG):
        self.__nome =  nome
        self.__CPF = CPF
        self.__RG = RG
        self.__data_nascimento = None
        self.__endereco = Endereco()

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome 

    @property
    def CPF(self):
        return self.__CPF

    @CPF.setter
    def CPF(self, CPF):
        self.__CPF = CPF

    @property
    def RG(self):
        return self.__RG

    @RG.setter
    def RG(self, RG):
        self.__RG = RG

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    @property
    def endereco(self):
        return self.__endereco

    def __str__(self):
        return f'{self.nome}, CPF: {self.CPF}, RG: {self.RG}'
