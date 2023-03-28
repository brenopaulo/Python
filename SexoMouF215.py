sexo=str(input('Digite o seu sexo: ')).upper()
while sexo not in 'MF':
    sexo=str(input('ERROR,Digite o seu sexo novamente: ')).upper()
if sexo in 'F':
    print('O Sexo informado foi o Feminino')
if sexo in 'M':
    print('O Sexo informado foi o Masculino')
