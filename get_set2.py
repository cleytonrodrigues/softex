from string import *

class Conta:


    def __init__(self, titular, saldo, limite):
        self.__titular = titular
        self.__saldo   = saldo
        self.__limite  = limite
        
        #if self.__saldo < 2000:
        #    print("Tá ficando liso...")


    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))


    def deposita(self, valor):
        self.__saldo += valor


    def saca(self, valor):
        self.__saldo -= valor


    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)


    # Getters e Setters
    def get_saldo(self):
        return self.__saldo


    def get_titular(self):
        return self.__titular


    def get_limite(self):
        return self.__limite


    def set_limite(self, limite):
        self.__limite = limite

if __name__ == '__main__':

    minha_conta = Conta("Vitor", 1000, 5000)


    minha_conta.deposita(1000)
    minha_conta.saca(500)
    minha_conta.extrato()


    outra_conta = Conta("Joao", 2500, 7000)
    outra_conta.transfere(500, minha_conta)
    minha_conta.extrato()

    # Acessando atributos 
    minha_conta.get_saldo()
    minha_conta.get_titular()
    minha_conta.get_limite()
    minha_conta.set_limite(10000)