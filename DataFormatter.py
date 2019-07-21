import pandas as pd


class DataFormatter():
	def __init__():
		pass

	def getFormattedData(data):
		pass

	def getTrainTargetTest(data):
		pass

	def get2017BikeData():
		# TODO: read in bike data
		data = format2017BikeData(data)
		# TODO: insert station ids
		# TODO: get target variables
		# TODO: read in weather data
		# TODO: concat weather data
		return data

	def format2017BikeData(data):
		data = format_time(data)
		pass

	def format2017Time(quarter, data):
		if quarter == 0 or quarter == 1:
			data['trip_start_time'] = pd.to_datetime(data['trip_start_time'],
		                                                format='%d/%m/%Y %H:%M')
			data['trip_stop_time'] = pd.to_datetime(data['trip_stop_time'],
		                                               format='%d/%m/%Y %H:%M')
		elif quarter == 3:
			data['trip_start_time'] = pd.to_datetime(data['trip_start_time'],
		                                                format='%m/%d/%y %H:%M:%S')
			data['trip_stop_time'] = pd.to_datetime(data['trip_stop_time'],
		                                               format='%m/%d/%y %H:%M:%S')
		else:
			data['trip_start_time'] = pd.to_datetime(data['trip_start_time'],
		                                                format='%m/%d/%Y %H:%M')
			data['trip_stop_time'] = pd.to_datetime(data['trip_stop_time'],
		                                                format='%m/%d/%Y %H:%M')
		return data
