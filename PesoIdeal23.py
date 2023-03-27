peso=float(input('Digite o seu peso: '))
altura=float(input('Digite a sua altura: '))
abaixo=('Abaixo do Peso')
ideal=('Peso Ideal')
acima=('Acima do Peso')
R=(peso/(altura**2))
imc=(peso/(altura**2))
if(R<20):R=abaixo
elif(20<=R<25):R=ideal
elif(R<=25):R=acima
print('A sua faixa de peso é: {} ,pois o seu IMC é de {}'.format(R,imc))