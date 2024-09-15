import numpy as np
import matplotlib.pyplot as plt

def shm(mass, k, time):
    omega = np.sqrt(k / mass)
    t = np.linspace(0, time, num=500)
    x = np.cos(omega * t)

    fig, ax = plt.subplots()
    ax.plot(t, x)
    ax.set_title('Simple Harmonic Motion')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Displacement (m)')
    ax.grid(True)

    return fig
