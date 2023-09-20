class Main:
    pass


from Conta import Conta

conta1 = Conta('Geruncio', 6565, 0)


conta1.get_conta()
conta1.set_saldo(-2000)
conta1.set_saldo(2000)
conta1.get_conta()
