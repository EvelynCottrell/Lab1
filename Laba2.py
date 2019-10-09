from control.matlab import *
from numpy import *
import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from fractions import Fraction

W1 = tf([0.6],[3., 1.])
W2 = tf([1.],[5., 1])
W3 = tf([2.],[4.,1.])
W4 = tf([24.],[8.,1.])
W5 = W4*W2*W3
W6 = W5/(1+W5*W1)
print(W6)

y, x = step(W6)
plt.plot(x, y, "r")
plt.title('Переходная Характеристика')
plt.ylabel('Амплитуда')
plt.xlabel('Время(с)')
plt.grid(True)
plt.show()

e = np.linspace(0, 100, num=1000)
real, imag, freq = nyquist(W6, omega= e)
plt.plot()
plt.title('Диаграмма найквиста')
plt.ylabel('+J')
plt.xlabel('+1')
plt.grid(True)
plt.show()

mag, phase, omega = bode(W6, dB=False)
plt.plot()
plt.show()

pzmap(W6)
plt.plot()
plt.grid(True)
plt.show()

D = W6.den
F = D[0]
S = F[0]
print("Коэффициенты: " + str(S))
n = len(S)
print("Количество элементов: " + str(n))
print("Полюса: " + str(pole(W6)))
w = symbols('w', real=True)
result = 0
for i in range(n):
    Z = S[i]*(I*w)**(n-1)
    result += Z
    n -= 1
print("Характеристический многочлен замкнутой системы" + str(result))
Real=re(result)
Im=im(result)
print("Действительная часть Re= " + str(Real))
print("Мнимая часть Im= " + str(Im))
x=[Real.subs({w:q}) for q in arange(0,50,0.01)]
y=[Im.subs({w:q}) for q in arange(0,50,0.01)]
plt.plot(x, y)
plt.grid(True)
plt.show()