# TorontoBikeShare
Project using machine learning to predict amount of bikes left over at a each bike share station in Toronto.

## Data
#### Target Data
Want to predict bikes_left at the end of each hour of the day. This variable is a vector of number of bikes currently at each station. It is an predictor and target variable.

#### Predictor Data
Model takes in a trip, current weather for the trip, and the bikes_left for each station

## Model
The model is an RNN with LTSM nodes, the model loops on itself and has an output prediction for each hour of the day.


