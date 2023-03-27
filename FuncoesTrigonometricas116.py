a=int(input('Digite o valor de um ângulo em graus: '))
import math
b=math.radians(a)
x=math.sin(b)
y=math.cos(b)
z=math.tan(b)
p=(1/y)
print('0s valores de seno,cosseno,tangente e secante,respectivamente são {},{},{} e {}'.format(x,y,z,p))
