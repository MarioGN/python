class Endereco():
    def __init__(self):
        self.__rua = None
        self.__bairro = None
        self.__cidade = None
        self.__CEP = None
        self.__complemento = None

    @property
    def rua(self):
        return self.__rua

    @rua.setter
    def rua(self, rua):
        self.__rua = rua

    @property
    def bairro(self):
        return self.__bairro

    @bairro.setter
    def bairro(self, bairro):
        self.__bairro = bairro

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @property
    def CEP(self):
        return self.__CEP

    @CEP.setter
    def CEP(self, CEP):
        self.__CEP = CEP
    
    @property
    def complemento(self):
        return self.__complemento

    @complemento.setter
    def complemento(self, complemento):
        self.__complemento = complemento

    def __str__(self):
        return f'rua: {self.rua}, bairro: {self.bairro}, cidade: {self.cidade}' \
               f', cep: {self.CEP}, complemento: {self.complemento}'