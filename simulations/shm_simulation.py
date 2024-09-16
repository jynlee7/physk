import numpy as np
import matplotlib.pyplot as plt
import io
import base64

def simulate_shm(k, m, x0):
    omega = np.sqrt(k / m)
    t = np.linspace(0, 10, num=500)
    x = x0 * np.cos(omega * t)

    fig, ax = plt.subplots()
    ax.plot(t, x)
    ax.set(xlabel='Time (s)', ylabel='Displacement (m)', title='Simple Harmonic Motion')
    ax.grid()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    img_data = base64.b64encode(img.getvalue()).decode()

    stats = {
        'Amplitude': np.max(np.abs(x))
    }

    return img_data, stats
