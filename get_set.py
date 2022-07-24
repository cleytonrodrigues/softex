class Conta:

    def __init__(self, titular, saldo, limite):
        self.__titular = titular
        self.__saldo   = saldo
        self.__limite  = limite
        
    def get_saldo(self):
        return self.__saldo
        
if __name__ == '__main__':
    newobject = Conta('cleyton',1000,2000)
    #print(newobject.__saldo)
    print(newobject.get_saldo())