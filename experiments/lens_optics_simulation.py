import matplotlib.pyplot as plt

def lens_optics(focal_length, object_distance):
    # Lens equation: 1/f = 1/d_o + 1/d_i
    if object_distance != 0:
        image_distance = (focal_length * object_distance) / (object_distance - focal_length)
    else:
        image_distance = float('inf')

    fig, ax = plt.subplots()
    ax.plot([0, object_distance], [0, 1], 'bo-', label='Object')
    ax.plot([0, image_distance], [0, -1], 'ro-', label='Image')

    ax.axvline(x=0, color='k', linestyle='--', label='Lens')
    ax.set_title('Lens Optics Simulation')
    ax.set_xlabel('Distance (m)')
    ax.set_ylabel('Height')
    ax.legend()
    ax.grid(True)

    return fig
