class Gafanhoto:
    def __init__(self, nome = "vazio", idade = 0): # metodo Construtor

        #Atributos de instancia
        self.nome = nome
        self.idade = idade
    def aniversario(self):
        self.idade += 1

    def __str__(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos."
    
# Declaração de Objeto
g1 = Gafanhoto("Thiago", 21)
g1.aniversario()
print(g1)

