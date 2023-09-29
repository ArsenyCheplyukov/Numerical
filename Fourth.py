import sympy as sp
import pylab

# maximum time
max_time = 15
# time step
dt = 0.05
# filling array of time
t = [i * dt for i in range(int(max_time / dt))]

############################################################################################################
#                                          part 1
############################################################################################################

# start omega
omega = 3
# amplitude of hesitation
a1 = 0.2
a2 = 0.1
# phases of hesitations
fi1 = 0
fi2 = 0
# equations of motion of this pendulums
x1 = [a1 * sp.sin(omega * i + fi1) for i in t]
x2 = [a2 * sp.sin(omega * i + fi2) for i in t]
# sum of two equations of motion
xr = [x1[i] + x2[i] for i in range(len(t))] 
# drawing graph of equation of summarized motion
pylab.subplot(1, 3, 1)
pylab.grid()
pylab.plot(t,x1, '--', label = 'x1')
pylab.plot(t,x2,'-.', label = 'x2')
pylab.plot(t,xr,'-', label = 'x1 + x2')
pylab.xlabel('время t, с');
pylab.ylabel('смещение x, м');
pylab.title('Зависимость смещения маятника от времени')
pylab.legend()

########################################################################################################
#                                      part 2
########################################################################################################

# first amplitude
a1 = 1 
# first omega
omega1 = 50
# second omega
omega2 = 56
# filling array of first coordinate
x1 = [a1 * sp.sin(omega1 * i) for i in t]
x2 = [a1 * sp.sin(omega2 * i) for i in t]
# sum of two equations of motion
xr = [x1[i] + x2[i] for i in range(len(t))] 
# envelope equation
xo = [2 * a1 * sp.cos((omega2-omega1) * i/2) for i in t]
# drawing graph of summarized equations
pylab.subplot(1, 3, 2)
pylab.grid()
pylab.plot(t,xr,'-', label = 'x1+x2')
pylab.plot(t,xo,'--', label = 'огибающая')
pylab.xlabel('время t, с')
pylab.ylabel('смещение x, м')
pylab.title('Зависимость смещения маятника от времени')
pylab.legend()

###########################################################################################################
#                                                  part 3
###########################################################################################################

# first and second amplitude
a1 = 0.2
a2 = 0.3 
# first and second omega
omega1 = 2
omega2 = 3
# phases of hesitations
fi1 = sp.pi / 4
fi2 = 0
# filling array of first coordinate
x1 = [a1 * sp.sin(omega1 * i + fi1) for i in t]
x2 = [a2 * sp.sin(omega2 * i + fi2) for i in t]
# draw Lisajue's figure
pylab.subplot(1, 3, 3)
pylab.grid()
pylab.plot(x1,x2)
pylab.title('Фигура Лиссажу')
# Show window with all this icons
pylab.show()