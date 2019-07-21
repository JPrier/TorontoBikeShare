import Model
import DataFormatter

def BikeShareController():
	def __init__():
		self.model = Model()
		self.dataFormatter = DataFormatter()

	# From FrontEnd
	def predictUserInputData(data):
		predictData(data)

	def getModelResults():
		return None

	### General Methods ###
	def predictData(data):
		data = self.dataFormatter.getFormattedData(data)
		return self.model.predict(data)

	def trainData(data):
		self.model.train(data)
