from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @abstractmethod
    def acelerar(self, velocidade=10):
        pass

    @abstractmethod
    def freiar(self):
        pass


class Carro(Veiculo):
    def __init__(self, cor, marca, ano):
        self.__cor = cor
        self.__marca = marca
        self.__ano = ano
        self.__ligado = False
        self.__velocidade = 0

    @property
    def cor(self):
        return self.__cor
    
    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    def ligar(self):
        if self.__ligado:
            print('O veículo já está ligado.')
        else:
            self.__ligado = True
            print('O veículo foi ligado.')

    def desligar(self):
        if !self.__ligado:
            print('O veículo já esta desligado.')
        else:
            self.__ligado = False
            print('O veículo foi desligado.')

    def acelerar(self, velocidade=10):
        if velocidade > 0:
            self.__velocidade += velocidade
            print(f'O veículo foi acelerado para {self.__velocidade} KMs.')

    def freiar(self):
        self.__velocidade = 0
        print('Veículo freiado.')

    def __str__(self):
        return f'Carro: {self.__marca}, Cor: {self.__cor}, Ano: {self.__ano}'
