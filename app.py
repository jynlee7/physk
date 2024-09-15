from flask import Flask, render_template, request, redirect, url_for
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from experiments.projectile_motion import projectile_motion
from experiments.pendulum_simulation import pendulum

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projectile', methods=['GET', 'POST'])
def projectile():
    if request.method == 'POST':
        try:
            # Retrieve user inputs from the form
            v0 = float(request.form['v0'])
            angle = float(request.form['angle'])
            t_end = float(request.form['t_end'])

            # Generate projectile motion plot
            fig = projectile_motion(v0, angle, t_end)

            # Convert plot to PNG image for display
            output = io.BytesIO()
            FigureCanvas(fig).print_png(output)
            img_data = base64.b64encode(output.getvalue()).decode('utf-8')

            return render_template('experiment.html', experiment_name="Projectile Motion", img_data=img_data)
        except ValueError:
            return render_template('experiment.html', experiment_name="Projectile Motion", error="Invalid input.")
    
    return render_template('experiment.html', experiment_name="Projectile Motion")

@app.route('/pendulum', methods=['GET', 'POST'])
def pendulum_sim():
    if request.method == 'POST':
        try:
            # Retrieve user inputs from the form
            theta0 = float(request.form['theta0'])
            L = float(request.form['L'])

            # Generate pendulum simulation plot
            fig = pendulum(theta0, L)

            # Convert plot to PNG image for display
            output = io.BytesIO()
            FigureCanvas(fig).print_png(output)
            img_data = base64.b64encode(output.getvalue()).decode('utf-8')

            return render_template('experiment.html', experiment_name="Pendulum Simulation", img_data=img_data)
        except ValueError:
            return render_template('experiment.html', experiment_name="Pendulum Simulation", error="Invalid input.")
    
    return render_template('experiment.html', experiment_name="Pendulum Simulation")

if __name__ == "__main__":
    app.run(debug=True)
