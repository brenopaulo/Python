primeiro=int(input('Digite o primeiro valor: '))
segundo=int(input('Digite o segundo valor: '))
igual=('Os dois valores são iguais')
maior=primeiro
if(segundo>maior):maior=segundo
if(primeiro==segundo):maior=igual
print('O maior valor: {}'.format(maior))