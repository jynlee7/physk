from flask import Flask, render_template, request
from simulations.electric_field_simulation import simulate_electric_field
from simulations.lens_optics_simulation import simulate_lens_optics
from simulations.pendulum_simulation import simulate_pendulum
from simulations.projectile_motion import simulate_projectile_motion
from simulations.shm_simulation import simulate_shm


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/experiment/<string:experiment_name>', methods=['GET', 'POST'])
def experiment(experiment_name):
    if request.method == 'POST':
        dimension = request.form.get('dimension')

        # Handle 3D Simulation
        if dimension == '3D':
            return render_template('experiment.html', exp_name=experiment_name, dimension="3D")

        # Handle 2D Simulations (existing logic for 2D)
        # Add the corresponding 2D simulation code
        if experiment_name == 'Projectile Motion':
            v0 = float(request.form['v0'])
            angle = float(request.form['angle'])
            t_end = float(request.form['t_end'])
            img_data, stats = simulate_projectile_motion(v0, angle, t_end)
        elif experiment_name == 'Pendulum':
            length = float(request.form['length'])
            theta0 = float(request.form['theta0'])
            img_data, stats = simulate_pendulum(length, theta0)
        elif experiment_name == 'Simple Harmonic Motion':
            k = float(request.form['k'])
            m = float(request.form['m'])
            x0 = float(request.form['x0'])
            img_data, stats = simulate_shm(k, m, x0)
        elif experiment_name == 'Electric Field':
            q1 = float(request.form['q1'])
            q2 = float(request.form['q2'])
            img_data, stats = simulate_electric_field(q1, q2)
        elif experiment_name == 'Lens Optics':
            focal_length = float(request.form['focal_length'])
            img_data, stats = simulate_lens_optics(focal_length)

    return render_template('experiment.html', exp_name=experiment_name)

if __name__ == '__main__':
    app.run(debug=True)
