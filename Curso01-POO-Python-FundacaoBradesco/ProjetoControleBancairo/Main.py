class Main:
    pass


from Conta import Conta
from Cliente import Cliente

c1 = Cliente('Geruncio','(11) 2564-7898')
conta1 = Conta(c1.get_nome(), 6565, 122)


conta1.deposita(200)
conta1.saque(40)
conta1.extrato()
