class Cliente:
    def __init__(self,n,fone):
        self.nome = n
        self.telefone = fone

    # Método GET
    def get_nome(self):
        return self.nome

    #Método SET
    def set_nome(self,nome):
        self.nome = nome




