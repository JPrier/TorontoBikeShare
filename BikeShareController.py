import Model as model
import DataFormatter as df

# From FrontEnd
def predictUserInputData(data):
	predictData(data)

def getModelResults():
	return [5, 4, 3, 2, 1]

### General Methods ###
def predictData(data):
	data = df.getFormattedData(data)
	return model.predict(data)

def trainData(data):
	model.train(data)
