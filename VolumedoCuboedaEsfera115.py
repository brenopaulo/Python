r=int(input('Digite o raio da esfera: '))
a=int(input('Digite a aresta do cubo: '))
import math
x=math.pi
V1=(4/3*x*r**3)
V2=(a**3)
VT=(V1+V2)
print('O volume da esfera é {} e o do cubo é {}. Sendo assim,o volume total do recipiente é {}'.format(V1,V2,VT))
