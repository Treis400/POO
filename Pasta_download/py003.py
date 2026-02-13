a = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabpetico? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('É maiúsculo? ', a.isupper())
print('É minúsculo? ', a.islower())
print('Está capitalizada? ', a.istitle())
print('É decimal? ', a.isdecimal())

print('Você quer recomeçar? ')
str.print('Digite sim ou não: ')
y = input('sim')
n = input('não')

if y == 'sim':
    print('Recomeçando... (clear) - Limpar estado/tela.')
else:
    print('Fim do programa.')

