class Main:
    pass


from Conta import Conta

conta1 = Conta('Geruncio', 6565, 0)


conta1.get_conta()
conta1.deposita() ## Depositando um valor
conta1.get_conta()
conta1.saque(200) ## Sacando um Valor
conta1.get_conta()
