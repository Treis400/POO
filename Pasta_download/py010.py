#Crie um programa que leia quanto dinhero um pessoa tem na carteira e mostre quantos dolares ela pode gastar.
print('---------------------Bem Vindo ao seu Conversor monetário-------------------------')
nome = str(input('Qual é o seu nome? '))
pais = str(input('Para qual pais você irá viajar? '))
print('//////////////////////////////////////////////////')
print('Olá, {}!'.format(nome), 'Será um prazer em te ajudar a ver o quanto você pode gastar no(a,os,as) {}.'.format(pais))
print('                                            ')
real = float(input('Quanto reais você tem na Conta neste momento? R$ '))
dolar = 5.20
conversao = real / dolar
print('                                                              ')

print('Com R$ ', real, 'você tem disponível em dolares: U$ {:.2f}' .format(conversao))
print('                                ')
print('Boa viagem e aproveite bastante!')
print('//////////////////////////////////////////////////')
