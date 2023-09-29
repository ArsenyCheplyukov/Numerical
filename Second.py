import sympy as sp
from matplotlib import pylab

# create symbol to integrate acceleration in future
t_dif = sp.Symbol('t')
# time step
dt = 0.0001
# start time
start_t = 0
# final time
final_t = 2 
# start speed
start_v = 0
# create acceleration for integral
a_int = 2 * (sp.sin(t_dif)**3) * sp.cos(t_dif) 
# array of time
t = [i * dt + start_t for i in range(int(final_t / dt))]
# create array of values of acceleration
a = [(2 * (sp.sin(i)**3) * sp.cos(i)) for i in t]
# paint graph of acceleration to time
pylab.subplot(1, 3, 1)
pylab.grid()
pylab.plot(t, a, 'g')
pylab.xlabel('Время t, с')
pylab.ylabel('Ускорение a, м/c^2')
pylab.title('Зависимость ускорения a от времени t')
# integration acceleration to speed 
v = sp.integrate(a_int, t_dif)
# finding constatnt with start speed
v.subs(sp.oo, 0)
start_v_value = v.subs(t_dif, start_t)
c_to_v = start_v - start_v_value
# filling array of v with values
array_of_v = [v.subs(t_dif, i) + c_to_v for i in t]
# paint graph of speed to time
pylab.subplot(1, 3, 2)
pylab.grid()
pylab.plot(t, array_of_v, 'b')
pylab.xlabel('Время t, с')
pylab.ylabel('Скорость, м/c')
pylab.title('Зависимость скорости v от времени t')
# teoretical acceleration
v_t = [((sp.sin(i)**4) / 2) for i in t]
# paint graph of teoretical speed to time
pylab.subplot(1, 3, 3)
pylab.grid()
pylab.plot(t, v_t, 'r')
pylab.xlabel('Время t, с')
pylab.ylabel('Скорость, м/c')
pylab.title('Зависимость теоретической скорости v_t от времени t')
# Show window with all this icons
pylab.show()