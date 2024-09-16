import numpy as np
import matplotlib.pyplot as plt
import io
import base64

def simulate_lens_optics(focal_length):
    x = np.linspace(-10, 10, 400)
    y = np.linspace(-10, 10, 400)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X / focal_length) * np.sin(Y / focal_length)

    fig, ax = plt.subplots()
    c = ax.contourf(X, Y, Z, cmap='viridis')
    fig.colorbar(c, ax=ax)
    ax.set(xlabel='X Position (m)', ylabel='Y Position (m)', title='Lens Optics Simulation')
    ax.grid()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    img_data = base64.b64encode(img.getvalue()).decode()

    stats = {
        'Lens Optics Intensity Range': np.min(Z),  # Example statistic
    }

    return img_data, stats
