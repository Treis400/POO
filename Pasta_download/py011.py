#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
paredeLargura = float(input('Escreva a largura da parede em metros: '))
paredeAltura = float(input('Escreva a altura da parede em metros: '))
areaParede = paredeLargura * paredeAltura

lataTinta = areaParede / 2

print('A área da parede é de {:.2f} m2. ' .format(areaParede))
print('-----------------------------------------------------')
print('e você vai precisar de {:.2f} litros de tinta para pintar '.format(lataTinta))
print('          ')
print('---------------Então, mão na massa !!-------------------')
print('-----------------------FIM------------------------------')
