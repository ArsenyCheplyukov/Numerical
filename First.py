import sympy as sp
from matplotlib import pylab

t_dif = sp.Symbol('t')
# time step
dt = 0.01
max_time = 1 
# create x for differential
x_d = 1 / (2*t_dif**2 + 1)
# array of time
t = [i * dt for i in range(int(max_time / dt))]
# array of coordinates
x = [(1 / (2*(i**2) + 1)) for i in t]
# teoretical speed
vt = [(-4*i / (2*(i**2) + 1)**2) for i in t]
# teoretical acceleration
at = [(4 * (8 * (i**2) / (2*(i**2) + 1) - 1) / ((2 * (i**2) + 1)**2)) for i in t]
# speed of differential
v = x_d.diff(t_dif)
# replacing 't' with values in array of speed
array_of_v = [v.subs(t_dif, i) for i in t ]
# acceleration of differential
a = v.diff(t_dif)
# replacing 't' with values in array of acceleration
array_of_a = [a.subs(t_dif, i) for i in t]
# drawing graph of time to teoretical coorditate
pylab.subplot(1, 3, 1)
pylab.grid() 
pylab.plot(t, x, 'r')
pylab.xlabel('Время t, с')
pylab.ylabel('Координата x, м/c')
pylab.title('Зависимость координаты x от времени t')
# drawing graph of time to teoretical speed
pylab.subplot(1, 3, 2)
pylab.grid()
pylab.plot(t, vt, 'r')
pylab.plot(t, array_of_v, 'b')
pylab.xlabel('Время t, с')
pylab.ylabel('Скорость v, м/c^2')
pylab.title('Зависимость скорости v от времени t')
# drawing graph of time to teoretical and practical acceleretion
pylab.subplot(1, 3, 3)
pylab.grid()
pylab.plot(t, at, 'r')
pylab.plot(t, array_of_a, 'b')
pylab.xlabel('Время t, с')
pylab.ylabel('Ускорение a, м/c^2')
pylab.title('Зависимость ускорения a от времени t')
# Show window with all this icons
pylab.show()
