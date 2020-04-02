import proprietario


class Carro():
    def __init__(self, modelo, cor, ano, proprietario):
        self.__modelo = modelo
        self.__cor = cor
        self.__ano = ano
        self.__marca = None
        self.__chassi = None
        self.__proprietario = proprietario
        self.__velocidade_maxima = None
        self.__velocidade_atual = 0
        self.__numero_portas = None
        self.__tem_teto_solar = False
        self.__numero_marcha = 0
        self.__tem_cambio_automatico = False
        self.__volume_de_combustivel = None

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano
    
    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def chassi(self):
        return self.__chassi

    @chassi.setter
    def chassi(self, chassi):
        self.__chassi = chassi

    @property
    def proprietario(self):
        return self.__proprietario

    @property
    def velocidade_maxima(self):
        return self.__velocidade_maxima

    @velocidade_maxima.setter
    def velocidade_maxima(self, velocidade_maxima):
        self.__velocidade_maxima = velocidade_maxima

    @property
    def velocidade_atual(self):
        return self.__velocidade_atual

    @velocidade_atual.setter
    def velocidade_atual(self, velocidade_atual):
        self.__velocidade_atual = velocidade_atual

    @property
    def numero_portas(self):
        return self.__numero_portas

    @numero_portas.setter
    def numero_portas(self, numero_portas):
        self.__numero_portas = numero_portas

    @property
    def tem_teto_solar(self):
        return self.__tem_teto_solar

    @tem_teto_solar.setter
    def tem_teto_solar(self, tem_teto_solar):
        self.__tem_teto_solar = tem_teto_solar

    @property
    def numero_marcha(self):
        return self.__numero_marcha

    @numero_marcha.setter
    def numero_marcha(self, numero_marcha):
        self.__numero_marcha = numero_marcha

    @property
    def tem_cambio_automatico(self):
        return self.__tem_cambio_automatico

    @tem_cambio_automatico.setter
    def tem_cambio_automatico(self, tem_cambio_automatico):
        self.__tem_cambio_automatico = tem_cambio_automatico

    @property
    def volume_de_combustivel(self):
        return self.__volume_de_combustivel

    @volume_de_combustivel.setter
    def volume_de_combustivel(self, volume_de_combustivel):
        self.__volume_de_combustivel = volume_de_combustivel

    def acelera(self):
        self.velocidade_atual = self.velocidade_atual + 1

    def freia(self):
        self.velocidade_atual = 0

    def troca_marcha(self):
        self.numero_marcha = self.numero_marcha + 1

    def reduz_marcha(self):
        self.numero_marcha = self.numero_marcha - 1
