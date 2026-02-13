class Gafanhoto:
    def __init__(self): # metodo Construtor

        #Atributos de instancia
        self.nome = ""
        self.idade = 0

    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos."
    
# Declaração de Objeto
g1 = Gafanhoto()
g1.nome = input("Digite o nome do Gafanhoto: ")
g1.idade = int(input(" Digite a idade:"))
g1.aniversario()
print('           ')
print(g1.mensagem())
print('           ')

