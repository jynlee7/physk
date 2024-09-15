import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def pendulum(theta0, L, g=9.81):
    def equation(theta, t):
        theta1 = theta[0]
        omega1 = theta[1]
        dtheta1dt = omega1
        domega1dt = -(g / L) * np.sin(theta1)
        return [dtheta1dt, domega1dt]
    
    t = np.linspace(0, 10, 500)
    theta_initial = [np.deg2rad(theta0), 0]
    
    sol = odeint(equation, theta_initial, t)
    
    fig, ax = plt.subplots()
    ax.plot(t, np.rad2deg(sol[:, 0]))
    ax.set_title('Pendulum Simulation')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Angle (degrees)')
    ax.grid(True)
    
    return fig
