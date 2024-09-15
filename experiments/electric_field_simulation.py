import numpy as np
import matplotlib.pyplot as plt

def electric_field(charge, distance):
    k = 8.99e9  # Coulomb constant (N·m²/C²)
    r = np.linspace(0.01, distance, 500)
    E = k * charge / r**2

    fig, ax = plt.subplots()
    ax.plot(r, E)
    ax.set_title('Electric Field Simulation')
    ax.set_xlabel('Distance (m)')
    ax.set_ylabel('Electric Field (N/C)')
    ax.grid(True)

    return fig
