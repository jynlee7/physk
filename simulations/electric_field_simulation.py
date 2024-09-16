import numpy as np
import matplotlib.pyplot as plt
import io
import base64

def simulate_electric_field(q1, q2):
    k = 8.99e9
    x = np.linspace(-1, 1, 100)
    y = np.linspace(-1, 1, 100)
    X, Y = np.meshgrid(x, y)
    r1 = np.sqrt(X**2 + Y**2)
    r2 = np.sqrt((X-0.5)**2 + Y**2)
    E1 = k * q1 / r1**2
    E2 = k * q2 / r2**2
    E = E1 - E2

    fig, ax = plt.subplots()
    c = ax.contourf(X, Y, E, cmap='RdYlBu')
    fig.colorbar(c, ax=ax)
    ax.set(xlabel='X Position (m)', ylabel='Y Position (m)', title='Electric Field')
    ax.grid()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    img_data = base64.b64encode(img.getvalue()).decode()

    stats = {
        'Electric Field Range': np.min(E),  # Example statistic
    }

    return img_data, stats
