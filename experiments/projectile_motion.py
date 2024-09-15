import numpy as np
import matplotlib.pyplot as plt

def projectile_motion(v0, angle, t_end, g=9.81):
    angle_rad = np.deg2rad(angle)
    t = np.linspace(0, t_end, num=500)
    x = v0 * np.cos(angle_rad) * t
    y = v0 * np.sin(angle_rad) * t - 0.5 * g * t**2
    
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title('Projectile Motion')
    ax.set_xlabel('Distance (m)')
    ax.set_ylabel('Height (m)')
    ax.grid(True)
    
    return fig
