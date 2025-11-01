from matplotlib.pylab import *
t = linspace(0, 10*pi, 5000)
z = cos(t)*exp(t/10)
plot(t,z,'b-')
title("James' Exponential Cosine Wave")
xlabel("Time")
ylabel("Displacement")
show()