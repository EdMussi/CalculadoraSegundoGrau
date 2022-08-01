import matplotlib.pyplot as plt
import numpy as np

print("="*30)
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))
print("="*30)
delta = ((b)**2)-(4*a*c)
if delta < 0:
    print('Essa função não apresenta uma raiz real')
elif delta == 0:
    print('Essa função apresenta uma raiz real! [x1 = x2]')
x1 = (-(b)+((delta)**(1/2)))/(2*a)
x2 = (-(b)-((delta)**(1/2)))/(2*a)
xv = -(b)/(2*a)
yv = -(delta)/(4*a)

print("O valor de delta(△) é: ", delta)
print("="*30)
print("O valor de x1 é: {:.2f}" .format(x1))
print("="*30)
print("O valor de x2 é: {:.2f}" .format(x2))
print("="*30)
print("O valor de  Xv é: {:.2f}" .format(xv))
print("="*30)
print("O valor de  Yv é: {:.2f}" .format(yv))
print("="*30)

eixo_x = []
eixo_y = []
zero = []

plt.ylabel('Valores de Y')
plt.xlabel('Valores de X')

variacao = abs(x1 - x2)
if variacao < 3:
    variacao = 3
print(variacao)

for x in np.arange(x1 - variacao, x2 + variacao, variacao / 100):
    y= a * (x ** 2 ) + b * (x) + c
    eixo_x.append(x)
    eixo_y.append(y)
    zero.append(0.0)
plt.plot(eixo_x,eixo_y,color="blue")
plt.plot(eixo_x,zero,color="black")
plt.show()
