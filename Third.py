import sympy as sp
import matplotlib as plt
from matplotlib import pylab
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# rigidity of spring pendulum
k = 0.1
# deviation from equilibrium
A = 0.06
# Step of t
dt = 0.01
# max time
t_max = 10
# creating array of time
tt = [i * dt for i in range(int(t_max / dt))]

###########################################################################################
#                                       Part 1                                            #
###########################################################################################

# starting mass
m0 = 0.3
# zero omega
omega0 = np.sqrt(k/m0)
# coordinates in equation of motion 
x0 = [A * np.cos(i * omega0) for i in tt]
# drawing graph of coordinates and time
pylab.subplot(2, 3, 1)
pylab.grid()
pylab.plot(tt, x0, 'r')
pylab.xlabel('Время t, с')
pylab.ylabel('Координата x0, м')
pylab.title('Зависимость координаты x0 от времени t')
# finding and filling array of speed based on time 
v0 = [A*omega0*np.sin(i*omega0) for i in tt]
# drawing graph of speed and time
pylab.subplot(2, 3, 2)
pylab.grid()
pylab.plot(tt, v0, 'r')
pylab.xlabel('Время t, с')
pylab.ylabel('Скорсть v0, м/c')
pylab.title('Зависимость скорости v от времени t')
# filling array of acceleration bases on speed
a0 = [-A*(omega0**2)*np.cos(i*omega0) for i in tt]
# drawing graph of acceleration and time
pylab.subplot(2, 3, 3)
pylab.grid()
pylab.plot(tt, a0, 'r')
pylab.xlabel('Время t, с')
pylab.ylabel('Ускорение a0, м/c^2')
pylab.title('Зависимость ускорения a0 от времени t')

#########################################################################################
#                                         Part 2                                        # 
#########################################################################################

# number of different masses and filling array of masses with values
number_of_points = 3
mm = [m0 * (i + 1) for i in range(number_of_points)]
# finding 2d coordinates array for 3d graph
x = [[A * np.cos(p*np.sqrt(k/i)) for p in tt] for i in mm]
# drawing graph of speed and time according to changing mass
pylab.subplot(2, 3, 4)
pylab.grid()
pylab.plot(tt, x[0], 'k-', tt, x[1], 'k-.', tt, x[2], 'k--')
pylab.title(str(mm[0]) + ' кг - ' +  str(mm[1]) + ' кг -.-. ' +  str(round(mm[2] * 10) / 10) + ' кг ---')
pylab.xlabel('Время t, с')  
pylab.ylabel('Координата x, м')
# converting this coordinates to 2D arrays
x_for_graph = np.arange(0, t_max, dt)
y_for_graph = np.arange(m0, 4*m0, (3 * m0) / (t_max/dt))
xgrid, ygrid = np.meshgrid(x_for_graph, y_for_graph)
zgrid = A * np.cos(xgrid*np.sqrt(k/ygrid))

############################################################################################
#                                          part 3
############################################################################################

# constant of friction start
r0 = 0.05
# final constant of friction
r_max = 0.1
# array of constant of friction
r = [0.05, 0.075, 0.1]
# finding delta
delta = [i / (2*m0) for i in r]
# finding x to two-dimensional graph
x = [[A*np.cos(tt[j]*omega0)* np.exp(-tt[j]*delta[i]) for j in range(len(tt))] for i in range(len(r))]
# drawing graph of speed and time according to changing constant of friction
pylab.subplot(2, 3, 5)
pylab.grid()
pylab.plot(tt, x[0], 'k-', tt, x[1], 'k-.', tt, x[2], 'k--')
pylab.title(str(r[0]) + ' - ' +  str(r[1]) + ' -.-. ' +  str(r[2]) + ' ---')
pylab.xlabel('коэффициент вязкого трения r')  
pylab.ylabel('Координата точки x, м') 
# converting to two-dimensional arrays
y__for_graph = np.arange(r0, r_max, (dt * (r_max - r0) / t_max))
x_grid, y_grid = np.meshgrid(x_for_graph, y__for_graph)
mass = (2*m0)**(-1)
z_grid = (A * np.cos(x_grid * int(omega0))) / np.exp(x_grid * y_grid * mass)

##########################################################################################
#                             part 4
##########################################################################################

# first omega
delta0 = delta[0]
# main frequency
om = [1, 2, 3]
# first frequency
om0 = 1.04
# last frequency 
om_last = 3.04
# making array of coordinate
x3 = []
for i in range(len(om)):
    A = 1 / sp.sqrt(((omega0**2)-(om[i]**2)*((omega0**2)-(om[i]**2)+4*(delta0**2)*(om[i]**2))))
    fi = sp.atan2((2*delta0*om[i]),((omega0**2)-(om[i]**2)))
    current_x = []
    for j in range(len(tt)):
        current_x.append(A*sp.cos(tt[j]*om[i]+fi))
    x3.append(current_x)
# drawing graph of coordinate to time with changing frequency
pylab.subplot(2, 3, 6)
pylab.grid()
pylab.plot(tt, x3[0], 'k-', tt, x3[1], 'k-.', tt, x3[2], 'k--')
pylab.title(str(om[0]) + ' - ' +  str(om[1]) + ' -.-. ' +  str(om[2]) + ' ---')
pylab.xlabel('t, c')  
pylab.ylabel('x, m')
# finding two-dimmentional array to three-dimmntional graph
y3_for_graph = np.arange(om0, om_last, (dt * (om_last - om0) / t_max))
x__grid, y__grid = np.meshgrid(x_for_graph, y3_for_graph)
z__grid = np.cos(x__grid*y__grid + np.arctan2((2*delta0*y__grid),((int(omega0)**2) - (y__grid**2)))) / (np.sqrt(((int(omega0)**2) - (y__grid**2))*(int((omega0)**2) - (y__grid**2) + 4*(delta0**2)*(y__grid**2))))

# 3D DRAWINGS:
# FOR PART 2
# drawing 3d graph of speed and time according to changing mass
fig = pylab.figure()
axes = Axes3D(fig)
axes.plot_surface(xgrid, ygrid, zgrid, rstride=10, cstride=10, cmap = 'ocean')
axes.set_xlabel('Время t, c')
axes.set_ylabel('Масса точки m, кг')
axes.set_zlabel('Координата точки x, м')
# FOR PART 3
fig2 = pylab.figure()
axes = Axes3D(fig2)
axes.plot_surface(x_grid, y_grid, z_grid, rstride=10, cstride=10, cmap = 'terrain')
axes.set_xlabel('Время t, c')
axes.set_ylabel('коэффициент вязкого трения r')
axes.set_zlabel('Координата точки x, м')
# FOR PART 4
fig3 = pylab.figure()
axes = Axes3D(fig3)
axes.plot_surface(y__grid, x__grid, z__grid, rstride=10, cstride=10, cmap = 'inferno')
axes.set_xlabel('t, c')
axes.set_ylabel('x, м')
axes.set_zlabel('omega, c^-1')
# showing graphs
pylab.show()
