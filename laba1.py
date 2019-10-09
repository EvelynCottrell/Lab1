import control.matlab as ctrl
import matplotlib.pylab as plt


def process_data(num11, den11, num21, den21):
    w11 = ctrl.tf(num11, den11)
    w21 = ctrl.tf(num21, den21)
    print('результат w11={} w21={}'.format(w11, w21))
    TimeLine = []
    for i in range (1, 3000):
        TimeLine.append(i/1000)
    plt.figure(0, figsize = [7, 6])

    [y11, x11] = ctrl.step(w11, TimeLine)
    [y21, x21] = ctrl.step(w21, TimeLine)
    plt.plot(x11, y11, "r", label='Исходная')
    plt.plot(x21, y21, "b", label='Увеличенная k и уменшенная Т')
    plt.title('Переходная функция звена')
    plt.ylabel('Амплитуда')
    plt.xlabel('Время(с)')
    plt.grid(True)
    plt.show()

    [y11, x11] = ctrl.impulse(w11, TimeLine)
    [y21, x21] = ctrl.impulse(w21, TimeLine)
    plt.plot(x11, y11, "r", label='Исходная')
    plt.plot(x21, y21, "b", label='Увеличенная k и уменшенная Т')
    plt.title('Импульсная функция  звена')
    plt.ylabel('Амплитуда')
    plt.xlabel('Время(с)')
    plt.grid(True)
    plt.show()

    ctrl.mag, ctrl.phase, ctrl.omega = ctrl.bode(w11, w21, dB=False)
    plt.plot()
    plt.show()
    return w11, w21


print('1 - безынерционное звено')
print('2 - апериодическое звено')
print('3 - интегрирующее звено')
print('4 - идеальное дифференцирующее звено')
print('5 - реально дифференцирующее звено')
print('Введите номер функции, которую необходимо отобразить:')
func_number = int(input())

if func_number == 1:
    process_data([4.], [ 1.], [2.], [ 1.])

elif func_number == 2:
    process_data([3.], [2, 1.], [1.5, 0.], [4, 1.])

elif func_number == 3:
    process_data([1.], [1, 0.], [1.], [0.5, 0.])

elif func_number == 4:
    process_data([5, 0.], [1e-12, 1.], [10, 0.], [1e-12, 1.])

elif func_number == 5:
    process_data([3.], [1, 1.], [1.5, 0.], [2, 1.])
