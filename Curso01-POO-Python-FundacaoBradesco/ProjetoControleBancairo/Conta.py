class Conta:
    def __init__(self, titular, numero, saldo):
        self._saldo = 0
        self._titular = titular
        self._numero = numero

    #Metodos GET
    @property
    def get_saldo(self):
        return float(self._saldo)

    def extrato(self):
        return print(f'Titular da conta: {self.get_titular()}, Numero: {self.get_numero()}, Saldo de R${self.get_saldo}')
    def get_titular(self):
        return self._titular

    def get_numero(self):
        return self._numero

    #Metodos SET
    def set_saldo(self, saldo):
        self._saldo = saldo if saldo > 0 else print(f'O valor R${float(saldo)} é negativo. Deposite um valor positivo!')


    # Funções
    def saque(self, valor):
        self._saldo -= valor if self._saldo >= valor else print('Saldo Insuficiente')

    def deposita(self, valor):
        self._saldo += valor if valor > 0 else print('Favor digitar um valor positivo')
