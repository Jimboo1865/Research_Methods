from matplotlib.pylab import *

g = 9.81 #Acceleration due to gravity in m/s^2

def velocity(t):
    v = -g *t
    return v

def position(t,height):
    y = height - 0.5 * g * t**2
    return y

def main():
    height = float(input("Enter the hieght in meters from which the obect is dropped: "))
    t = linspace(0, sqrt(2 * height /g), 100)
    y = position(t,height)
    v = velocity(t)
    plot(t, y, label = 'Position (m)', color = 'blue')
    plot(t, v, label = 'Velocity (m/s)', color = 'red')
    title('Free Fall from Height of {} meters'.format(height))
    xlabel('Time (s)')
    ylabel('Position (m) and Velocity (m/s)')
    grid(True)
    legend()
    show()
main()