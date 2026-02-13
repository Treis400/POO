print('---------------- Bem-vindo à Locadora de Carros! ----------------')

nomeCliente = input('Qual é o seu nome? ')
print(f'Ola, {nomeCliente}! Escolha o carro e a quantidade de dias em que você deseja alugar.')

# ----------------- LISTA DE CARROS -----------------
modelosCarros = {
    1: {"modelo": "Mobi 22/23", "cor": "Prata", "pacote": "Completo", "valor": 90},
    2: {"modelo": "Onix 24/25", "cor": "Branco", "pacote": "Completo", "valor": 110},
    3: {"modelo": "HB20 21/22", "cor": "Preto", "pacote": "Completo", "valor": 100}
}

print("\nModelos disponíveis:")
for codigo, dados in modelosCarros.items():
    print(f"{codigo}: {dados['modelo']} - {dados['cor']} - {dados['pacote']} - R$ {dados['valor']},00 por dia")

# Escolha do modelo
escolhaModelo = int(input('\nQual modelo você deseja alugar? (1, 2, 3): '))
if escolhaModelo not in modelosCarros:
    print('Opção inválida! Encerrando programa...')
    exit()

carroEscolhido = modelosCarros[escolhaModelo]
dias = int(input('Por quantos dias você irá alugar o carro? '))

print('\n----------- O seguro é obrigatório! -----------')
print('Você pode escolher entre:')
print('1 - Seguro Básico (R$ 12,00 por dia)')
print('2 - Seguro Completo (R$ 25,00 por dia)')

valorSeguro = int(input('Qual seguro você deseja contratar? (1 ou 2): '))
seguroBasico = 12
seguroCompleto = 25

if valorSeguro == 1:
    valor_seguro = seguroBasico
elif valorSeguro == 2:
    valor_seguro = seguroCompleto
else:
    print('Opção inválida! Fim do programa.')
    exit()


valor_total = (carroEscolhido["valor"] * dias) + (valor_seguro * dias)

print('\n------------------ RESUMO ------------------')
print(f'Cliente: {nomeCliente}')
print(f'Carro escolhido: {carroEscolhido["modelo"]}')
print(f'Dias alugados: {dias}')
print(f'Valor diário do carro: R$ {carroEscolhido["valor"]},00')
print(f'Tipo de seguro: {"Básico" if valorSeguro == 1 else "Completo"}')
print(f'Valor total do aluguel: R$ {valor_total:.2f}')

print('\nBoa viagem e conte conosco para o que precisar!')
print('---------------- FIM DO PROGRAMA ----------------')
