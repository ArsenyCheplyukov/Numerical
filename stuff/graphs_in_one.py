import numpy as np
import matplotlib.pyplot as plt
import numpy as np

plt.grid(color='black', linestyle='-', linewidth=0.25, which='both')

x = np.array([[1, 3, 3, 3, 1, 2, 2, 2],
                [10, 10, 10, 10, 10, 10, 10, 10, 9, 8],
                [20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
                [30, 30, 30, 30, 30, 30, 30, 30, 30, 30],
                [40, 39, 39, 39, 39, 39, 39, 39, 39, 40]]) * 2
y = np.array([[1, 5, 4, 10, 25, 21, 18, 13],
                [1, 3, 5, 7, 9, 13, 15, 20, 24, 25],
                [1, 2, 5, 7, 10, 11, 14, 16, 19, 20],
                [1, 2, 5, 7, 10, 11, 14, 16, 19, 20],
                [0, 1, 4, 7, 9, 14, 16, 20, 23, 25]]) * 2
for x, y in zip(x, y):
    fit = np.polyfit(x, y, x.size)
    print(fit)
    f = np.poly1d(fit)
    x_array = np.linspace(min(x), max(x), 1000)
    plt.scatter(x,y, c="blue", label='Измерянные величины')
    plt.plot(x_array,f(x_array), color="red", label='Сглаженные величины')
plt.xlabel("Н, напряжённость поля насыщения, A/м $10^{2}$")
plt.ylabel("μ, магнтная проницаемость, $10^{3}$")
plt.show()