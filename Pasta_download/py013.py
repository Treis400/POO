#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

nomeFuncionario = str(input('Qual é o nome do funcionário? '))
cargoFuncionario = str(input('Qual é o cargo do funcionário? '))
matriculaFuncionario = str(input('Qual é a matrícula do funcionário? '))
salarioAtual = float(input('Qual é o salário atual do funcionário? R$ '))
pontuacaoFuncionario = int(input('De 0 a 100, quantos pontos o funcionário recebeu na avaliação de desempenho? '))
metaAumento = salarioAtual * 1.15
print('-------------------------------------------------------------------------------------------------------')
if pontuacaoFuncionario < 75:
    novoSalario = salarioAtual
    print('Infelizmente, {} não atingiu a pontuação mínima para receber o aumento salarial. ' .format(nomeFuncionario))
else:
    novoSalario = metaAumento
    print('Parabéns, {}!!, ficamos felizes em informar que você atingiu a pontuação necessária para receber um aumento salarial! '.format(nomeFuncionario))

print('Agora {}, cuja matricula é {}, e que ocupa o cargo de {} é de R$ {:.2f} ' .format(nomeFuncionario, matriculaFuncionario, cargoFuncionario, novoSalario))
print('------------------------------------FIM-----------------------------------------')