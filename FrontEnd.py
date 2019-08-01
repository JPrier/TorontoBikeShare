import BikeShareController
import io, matplotlib.pyplot as plt
from flask import Flask, Response, render_template, request, url_for, redirect
app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/plot.png')
def plot_png():
    data = BikeShareController.getModelResults()
    if data is None:
        data = [1, 2, 3, 4, 5]
    plt.figure()
    plt.plot(data)
    plt.title("Bike Share Data")
    output = io.BytesIO()
    plt.savefig(output, format='png')
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/bikeshare', methods=['GET', 'POST'])
def redirect_to_bikeshare():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('bikeshare.html')

@app.route('/resume', methods=['GET', 'POST'])
def redirect_to_resume():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('resume.html')
