primeiro=int(input('Digite o primeiro valor: '))
segundo=int(input('Digite o segundo valor: '))
terceiro=int(input('Digite o terceiro valor: '))
maior=primeiro
if(segundo>maior):maior=segundo
if(terceiro>maior):maior=terceiro
print('O maior valor: {}'.format(maior))