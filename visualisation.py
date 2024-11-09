import matplotlib.pyplot as plt
import numpy as np
from planets import planets

def generate_trajectory(a,e):
    theta = np.linspace(0,2*np.pi,100)
    r = a*(1-e**2)/(1+e*np.cos(theta))
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    return x,y



def plot_trajectory(a,e):
    x,y = generate_trajectory(a,e)

    plt.figure()
    plt.plot(x,y)
    plt.title("Spacecraft Trajectory")
    plt.xlabel("X (AU)")
    plt.ylabel("Y (AU)")
    plt.grid(True)
    plt.show()

plot_trajectory(planets[2].semi_major_axis+planets[3].semi_major_axis/2,0.207)