import control.matlab as ctrl
import matplotlib.pylab as plt
import numpy

print('1 - безынерционное звено')
print('2 - апериодическое звено')
print('3 - интегрирующее звено')
print('4 - идеальное дифференцирующее звено')
print('5 - реально дифференцирующее звено')
print('Введите номер функции, которую необходимо отобразить:')
f = int(input())

def func_1(num11, den11, num21, den21):
    w11 = ctrl.tf(num11, den11)
    w21 = ctrl.tf(num21, den21)
    y11, x11 = ctrl.step(w11)
    y21, x21 = ctrl.step(w21)
    x11 = numpy.linspace(0, 18, num=100)
    x21 = numpy.linspace(0, 18, num=100)
    plt.axis([0, 18, 0, 8.5])
    plt.plot(x11, y11, "r", label='Исходная')
    plt.plot(x21, y21, "b", label='Уменьшенная k в два раза и увеличенная Т')
    plt.title('Переходная функция безынерционного звена')
    plt.ylabel('Амплитуда')
    plt.xlabel('Время, с')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()

    y11, x11 = ctrl.impulse(w11)
    y21, x21 = ctrl.impulse(w21)
    plt.plot(x11, y11, "r", label='Исходная')
    plt.plot(x21, y21, "b", label='Увеличенная k и уменшенная Т')
    plt.title('Импульсная функция безынерционное звена')
    plt.ylabel('Амплитуда')
    plt.xlabel('Время(с)')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()

    mag, phase, omega = ctrl.bode(w11, w21, dB=False)
    plt.plot()
    plt.show()
    print(w11, w21)




if f == 1:
    num11 = [4.]
    den11 = [0.1e-100,1.]
    num21 = [2.]
    den21 = [0.1e-100,1.]
    func_1(num11, den11, num21, den21)

elif f == 2:

    num11 = [3.]
    den11 = [2, 1.]
    num21 = [1.5, 0.1e-100]
    den21 = [4, 1.]
    w11 = ctrl.tf(num11, den11)
    w21 = ctrl.tf(num21, den21)
    y11, x11 = ctrl.step(w11)
    y21, x21 = ctrl.step(w21)
    x11 = numpy.linspace(0, 18, num=100)
    x21 = numpy.linspace(0, 18, num=100)
    plt.axis([0, 18, 0, 8.5])
    plt.plot(x11, y11, "r", label='Исходная')
    plt.plot(x21, y21, "b", label='Уменьшенная k в два раза и увеличенная Т')
    plt.title('Переходная функция безынерционное звена')
    plt.ylabel('Амплитуда')
    plt.xlabel('Время, с')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()

    y11, x11 = ctrl.impulse(w11)
    y21, x21 = ctrl.impulse(w21)
    plt.plot(x11, y11, "r", label='Исходная')
    plt.plot(x21, y21, "b", label='Увеличенная k и уменшенная Т')
    plt.title('Импульсная функция безынерционное звена')
    plt.ylabel('Амплитуда')
    plt.xlabel('Время(с)')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()

    mag, phase, omega = ctrl.bode(w11, w21, dB=False)
    plt.plot()
    plt.show()
    print(w11, w21)

elif f == 3:

    num11 = [1.]
    den11 = [1, 0.]
    num21 = [1.]
    den21 = [0.5, 0.]
    w11 = ctrl.tf(num11, den11)
    w21 = ctrl.tf(num21, den21)
    y11, x11 = ctrl.step(w11)
    y21, x21 = ctrl.step(w21)
    x11 = numpy.linspace(0, 18, num=100)
    x21 = numpy.linspace(0, 18, num=100)
    plt.axis([0, 18, 0, 8.5])
    plt.plot(x11, y11, "r", label='Исходная')
    plt.plot(x21, y21, "b", label='Уменьшенная k в два раза и увеличенная Т')
    plt.title('Переходная функция безынерционное звена')
    plt.ylabel('Амплитуда')
    plt.xlabel('Время, с')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()

    y11, x11 = ctrl.impulse(w11)
    y21, x21 = ctrl.impulse(w21)
    plt.plot(x11, y11, "r", label='Исходная')
    plt.plot(x21, y21, "b", label='Увеличенная k и уменшенная Т')
    plt.title('Импульсная функция безынерционное звена')
    plt.ylabel('Амплитуда')
    plt.xlabel('Время(с)')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()

    mag, phase, omega = ctrl.bode(w11, w21, dB=False)
    plt.plot()
    plt.show()
    print(w11, w21)

elif f == 4:
    num11 = [5, 0.]
    den11 = [0.1e-100,1.]
    num21 = [10,0.]
    den21 = [0.1e-100,1.]
    w11 = ctrl.tf(num11, den11)
    w21 = ctrl.tf(num21, den21)
    y11, x11 = ctrl.step(w11)
    y21, x21 = ctrl.step(w21)
    x11 = numpy.linspace(0, 18, num=100)
    x21 = numpy.linspace(0, 18, num=100)
    plt.axis([0, 18, 0, 8.5])
    plt.plot(x11, y11, "r", label='Исходная')
    plt.plot(x21, y21, "b", label='Уменьшенная k в два раза и увеличенная Т')
    plt.title('Переходная функция безынерционное звена')
    plt.ylabel('Амплитуда')
    plt.xlabel('Время, с')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()

    y11, x11 = ctrl.impulse(w11)
    y21, x21 = ctrl.impulse(w21)
    plt.plot(x11, y11, "r", label='Исходная')
    plt.plot(x21, y21, "b", label='Увеличенная k и уменшенная Т')
    plt.title('Импульсная функция безынерционное звена')
    plt.ylabel('Амплитуда')
    plt.xlabel('Время(с)')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()

    mag, phase, omega = ctrl.bode(w11, w21, dB=False)
    plt.plot()
    plt.show()
    print(w11, w21)

elif f == 5:
    num11 = [3.]
    den11 = [1, 1.]
    num21 = [1.5, 0.]
    den21 = [2, 1.]
    w11 = ctrl.tf(num11, den11)
    w21 = ctrl.tf(num21, den21)
    y11, x11 = ctrl.step(w11)
    y21, x21 = ctrl.step(w21)
    x11 = numpy.linspace(0, 18, num=100)
    x21 = numpy.linspace(0, 18, num=100)
    plt.axis([0, 18, 0, 8.5])
    plt.plot(x11, y11, "r", label='Исходная')
    plt.plot(x21, y21, "b", label='Уменьшенная k в два раза и увеличенная Т')
    plt.title('Переходная функция безынерционное звена')
    plt.ylabel('Амплитуда')
    plt.xlabel('Время, с')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()

    y11, x11 = ctrl.impulse(w11)
    y21, x21 = ctrl.impulse(w21)
    plt.plot(x11, y11, "r", label='Исходная')
    plt.plot(x21, y21, "b", label='Увеличенная k и уменшенная Т')
    plt.title('Импульсная функция безынерционное звена')
    plt.ylabel('Амплитуда')
    plt.xlabel('Время(с)')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()

    mag, phase, omega = ctrl.bode(w11, w21, dB=False)
    plt.plot()
    plt.show()
    print(w11, w21)
