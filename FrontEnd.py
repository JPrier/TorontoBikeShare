import BikeShareController, io
from flask import Flask, Response, render_template
app = Flask(__name__)

@app.route('/')
def index():
    if (bikeShareController is None):
        bikeShareController = BikeShareController()
    return render_template('index.html')

@app.route('/plot.png')
def plotPng():
    data = bikeShareController.getModelResults()
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
