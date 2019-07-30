from BikeShareController import BikeShareController
import io
from flask import Flask, Response, render_template, request, url_for, redirect
from matplotlib import Figure, FigureCanvas
app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/plot.png')
def plotPng():
    bikeShareController = BikeShareController()
    if bikeShareController != None:
        data = bikeShareController.getModelResults()
    else:
        data = [1, 2, 3, 4]
    figure = createFigure(data)
    output = io.BytesIO()
    FigureCanvas(figure).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def createFigure(data):
    figure = Figure()
    axis = figure.add_subplot(1,1,1)
    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    return figure

@app.route('/bikeshare', methods=['GET', 'POST'])
def redirectToBikeShare():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('bikeshare.html')
