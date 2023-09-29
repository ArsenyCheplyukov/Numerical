import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

y1 = np.array([2.4, 3.65, 4.65, 5.41, 6.11, 6.68, 7.22])**2
y2 = np.array([1.78, 3.41, 4.47, 5.2, 5.94, 6.58, 7.16])**2
x1 = 3662-np.array([1, 2, 3, 4, 5, 6, 7])
x2 = 3459-np.array([1, 2, 3, 4, 5, 6, 7])
f1 = np.poly1d(np.polyfit(x1, y1, 1))
f2 = np.poly1d(np.polyfit(x2, y2, 1))

x_array1 = np.linspace(min(x2), max(x1), 10000)
x_array2 = np.linspace(min(x2), max(x2), 10000)
#($10^6$)
plt.grid(color='black', linestyle='--', linewidth=0.1, which='both')
plt.ylabel("Квадрат диаметра колец, $мм^2$")
plt.xlabel("Порядок колец")

plt.scatter(x1, y1, c="lightgreen", label='Измерянные величины для зелёного цвета')
plt.plot(x_array1, f1(x_array1), color="darkgreen", label='Сглаженные величины для зелёного цвета')

plt.scatter(x2, y2, c="peachpuff", label='Измерянные величины для оранжевого цвета')
plt.plot(x_array2, f2(x_array2), color="darkorange", label='Сглаженные величины для оранжевого цвета')

#plt.axhline(y=1.4445, color='black', linestyle='--')
#plt.axvline(x=79, color='black', linestyle='--')
#print((f(10)-f(0))/10, f(0))
plt.legend()
plt.title("Зависисмость диаметра колец от порядка расположения")
plt.show()