import PredictionModel

# From FrontEnd
def predictUserInputData(data):
	predictData(data)

# From Prediction
def getTrainingParameters():
	# return TrainingModel.getParameters()
	pass

### General Methods ###
def predictData(data):
	return PredictionModel.predict(data)

def trainData(data):
	# TrainingModel.train(data)
	PredictionModel.setParameters(getTrainingParameters())