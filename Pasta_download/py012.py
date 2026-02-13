#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p1 = float(input('Qual é o preço do produto? R$ '))
desconto = p1 / 1.05

novoPreco = desconto

print('O preço do produto com 5% de desconto é R$ {:.2f} ' .format(novoPreco))