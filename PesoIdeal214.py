peso=float(input('Digite o seu peso em Kg: '))
altura=float(input('Digite a sua altura em Metros: '))
sexo=input('Digite o seu sexo usando F para feminino e M para masculino: ')
imc=(peso/(altura**2))
if(sexo=='F'):
    if(imc<19):
        print('Abaixo do Peso')
    elif(19<=imc<24):
        print('Peso Ideal')
    elif(imc>=24):
        print('Acima do Peso')
if(sexo=='M'):
    if(imc<20):
        print('Abaixo do Peso')
    elif(20<=imc<25):
        print('Peso Ideal')
    elif(imc>=25):
        print('Acima do Peso')
