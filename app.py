from flask import Flask, render_template, request
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from experiments.projectile_motion import projectile_motion
from experiments.pendulum_simulation import pendulum
from experiments.shm_simulation import shm
from experiments.electric_field_simulation import electric_field
from experiments.lens_optics_simulation import lens_optics

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Projectile Motion
@app.route('/projectile', methods=['GET', 'POST'])
def projectile():
    if request.method == 'POST':
        try:
            v0 = float(request.form['v0'])
            angle = float(request.form['angle'])
            t_end = float(request.form['t_end'])

            fig = projectile_motion(v0, angle, t_end)
            output = io.BytesIO()
            FigureCanvas(fig).print_png(output)
            img_data = base64.b64encode(output.getvalue()).decode('utf-8')
            return render_template('experiment.html', experiment_name="Projectile Motion", img_data=img_data)
        except ValueError:
            return render_template('experiment.html', experiment_name="Projectile Motion", error="Invalid input.")
    
    return render_template('experiment.html', experiment_name="Projectile Motion")

# Pendulum Simulation
@app.route('/pendulum', methods=['GET', 'POST'])
def pendulum_sim():
    if request.method == 'POST':
        try:
            theta0 = float(request.form['theta0'])
            L = float(request.form['L'])

            fig = pendulum(theta0, L)
            output = io.BytesIO()
            FigureCanvas(fig).print_png(output)
            img_data = base64.b64encode(output.getvalue()).decode('utf-8')
            return render_template('experiment.html', experiment_name="Pendulum Simulation", img_data=img_data)
        except ValueError:
            return render_template('experiment.html', experiment_name="Pendulum Simulation", error="Invalid input.")
    
    return render_template('experiment.html', experiment_name="Pendulum Simulation")

# Simple Harmonic Motion (SHM)
@app.route('/shm', methods=['GET', 'POST'])
def shm_sim():
    if request.method == 'POST':
        try:
            mass = float(request.form['mass'])
            k = float(request.form['k'])
            time = float(request.form['time'])

            fig = shm(mass, k, time)
            output = io.BytesIO()
            FigureCanvas(fig).print_png(output)
            img_data = base64.b64encode(output.getvalue()).decode('utf-8')
            return render_template('experiment.html', experiment_name="Simple Harmonic Motion", img_data=img_data)
        except ValueError:
            return render_template('experiment.html', experiment_name="Simple Harmonic Motion", error="Invalid input.")
    
    return render_template('experiment.html', experiment_name="Simple Harmonic Motion")

# Electric Field Simulation
@app.route('/electric_field', methods=['GET', 'POST'])
def electric_field_sim():
    if request.method == 'POST':
        try:
            charge = float(request.form['charge'])
            distance = float(request.form['distance'])

            fig = electric_field(charge, distance)
            output = io.BytesIO()
            FigureCanvas(fig).print_png(output)
            img_data = base64.b64encode(output.getvalue()).decode('utf-8')
            return render_template('experiment.html', experiment_name="Electric Field Simulation", img_data=img_data)
        except ValueError:
            return render_template('experiment.html', experiment_name="Electric Field Simulation", error="Invalid input.")
    
    return render_template('experiment.html', experiment_name="Electric Field Simulation")

# Lens Optics Simulation
@app.route('/lens_optics', methods=['GET', 'POST'])
def lens_optics_sim():
    if request.method == 'POST':
        try:
            focal_length = float(request.form['focal_length'])
            object_distance = float(request.form['object_distance'])

            fig = lens_optics(focal_length, object_distance)
            output = io.BytesIO()
            FigureCanvas(fig).print_png(output)
            img_data = base64.b64encode(output.getvalue()).decode('utf-8')
            return render_template('experiment.html', experiment_name="Lens Optics Simulation", img_data=img_data)
        except ValueError:
            return render_template('experiment.html', experiment_name="Lens Optics Simulation", error="Invalid input.")
    
    return render_template('experiment.html', experiment_name="Lens Optics Simulation")

if __name__ == "__main__":
    app.run(debug=True)
