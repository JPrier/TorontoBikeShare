# TorontoBikeShare
Project using machine learning to predict amount of bikes left over at a each bike share station in Toronto.

## Data
#### Target Data
Want to predict bikes_left at the end of each hour of the day. This variable is a vector of number of bikes currently at each station. It is an predictor and target variable.

#### Predictor Data
Model takes in a trip, current weather for the trip, and the bikes_left for each station

## Model
The model is an RNN with LTSM nodes, teacher forcing and the model loops on itself (the last node in the RNN outputs to the first node).
The RNN's timestep outputs represent an hour of time throughout a day

## Production Architecture
#### FrontEnd
Holds all code running front end realtime visualization and user inputs

#### RealTimeDataReceiver
Calls Toronto's API to get realtime data, then formats and sends the data to the training model through the controller

#### PredictionModel
Holds a copy of the training models parameters to allow for experimentation and testing on a model without possibly ruining the trained model. Also allows for user input of data without side effects

#### TrainingModel
The meat and potatoes of the project. Holds the model that is being trained off of realtime data and was already trained off of the 2017 dataset.

#### BikeShareController
Central controller for all of the project. Holds API methods for all of the other services.
##### API Calls:
  * FrontEnd
    * addNewDataToFront
    * setUserInputData
    * getPredictionData
  * RealTimeDataReceiver
    * addNewTrip
  * Prediction Model
    * getPrediction
    * getTrainingParameters
  * Training Model
    * getModelParameters
    * trainNewTrip
  



