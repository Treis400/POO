class ContaBancaria:
    def __init__(self, id_conta, nome, saldo=0.0):
        self.id = id_conta
        self.nome = nome
        self.saldo = saldo

        print(f"\nConta {self.id} criada com sucesso!")
        print(f"Saldo atual da conta é de: R$ {self.saldo:.2f}")

    # Método apenas para exibir os dados
    def __str__(self):
        return f"A conta {self.id} de {self.nome} possui saldo de R$ {self.saldo:.2f} disponível."

    def depositar(self, valor):
        if valor <= 0:
            print("Valor de depósito inválido.")
            return

        self.saldo += valor
        print(f"Depósito de R$ {valor:2f} realizado com sucesso.")
        print(f"Novo saldo: R$ {self.saldo:,.2f}")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido.")
        elif valor > self.saldo:
            print(f"Saque de R$ {valor:,.2f} negado: saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque de R$ {valor:,.2f} realizado com sucesso.")
            print(f"Novo saldo: R$ {self.saldo:,.2f}")

# ================= PROGRAMA PRINCIPAL =================

print("--------------- Bem-vindo ao Nosso Banco ---------------")

num = input("Digite o número da conta: ")
nome = input("Digite o nome do titular: ")

c1 = ContaBancaria(num, nome)

while True:
    print("\nEscolha uma opção:")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Exibir dados da conta")
    print("0 - Sair")

    opcao = input("Opção: ")

    if opcao == "0":
        print("Obrigado por usar NOSSO BANCO. Até logo!")
        break

    if opcao == "1":
        valor = float(input("Digite o valor para depósito: R$ "))
        c1.depositar(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor para saque: R$ "))
        c1.sacar(valor)
    elif opcao == "3":
        print(c1)
    else:
        print("Opção inválida.")