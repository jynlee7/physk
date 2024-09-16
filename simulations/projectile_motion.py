import numpy as np
import matplotlib.pyplot as plt
import io
import base64

def simulate_projectile_motion(v0, angle, t_end):
    t = np.linspace(0, t_end, num=500)
    g = 9.8
    theta = np.radians(angle)
    x = v0 * np.cos(theta) * t
    y = v0 * np.sin(theta) * t - 0.5 * g * t**2

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set(xlabel='Distance (m)', ylabel='Height (m)', title='Projectile Motion')
    ax.grid()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    img_data = base64.b64encode(img.getvalue()).decode()

    stats = {
        'Max Height': np.max(y),
        'Max Distance': np.max(x)
    }

    return img_data, stats
