import numpy as np
import matplotlib.pyplot as plt
import io
import base64

def simulate_pendulum(length, theta0):
    g = 9.8
    t = np.linspace(0, 10, num=500)
    theta = theta0 * np.cos(np.sqrt(g / length) * t)
    x = length * np.sin(theta)
    y = -length * np.cos(theta)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set(xlabel='X Position (m)', ylabel='Y Position (m)', title='Pendulum Motion')
    ax.grid()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    img_data = base64.b64encode(img.getvalue()).decode()

    stats = {
        'Max Displacement': np.max(np.abs(x))
    }

    return img_data, stats
