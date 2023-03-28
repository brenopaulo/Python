p=float(input('Digite o primeiro valor positivo: '))
s=float(input('Digite o segundo valor positivo: '))
t=float(input('Digite o terceiro valor positivo: '))
q=float(input('Digite o quarto valor positivo: '))
qu=float(input('Digite o quinto valor positivo: '))
sex=float(input('Digite o sexto valor positivo: '))
set=float(input('Digite o sétimo valor positivo: '))
oit=float(input('Digite o oitavo valor positivo: '))
non=float(input('Digite o nono valor positivo: '))
dec=float(input('Digite o décimo valor positivo: '))

maior=p
if(s>maior):maior=s
if(t>maior):maior=t
if(q>maior):maior=q
if(qu>maior):maior=qu
if(sex>maior):maior=sex
if(set>maior):maior=set
if(oit>maior):maior=oit
if(non>maior):maior=non
if(dec>maior):maior=dec
print('O maior valor é o: {}'.format(maior))

soma=(t+p+s+q+qu+sex+set+oit+non+dec)
print('A soma desses 10 valores é igual a: {}'.format(soma))

media=((t+p+s+q+qu+sex+set+oit+non+dec)/10)
print('A média aritmética desses 10 valores é igual a: {}'.format(media))