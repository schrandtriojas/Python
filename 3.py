import numpy as np
import matplotlib.pyplot as plt

# Задаем функцию плотности распределения
def f(x):
    if x <= 0:
        return 0
    elif x <= 2:
        return (5/32)*x**4
    else:
        return 0

# Задаем интервал для построения графика
x = np.linspace(-1, 3, 1000)

# Вычисляем значения функции плотности распределения для каждого значения x
y = [f(i) for i in x]

# Строим график
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График плотности распределения')
plt.show()
