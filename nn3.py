from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
import numpy as np
import csv, math
import pandas as pd

np.random.seed(10)

def split_data(data, period=1):
	X, Y = [], []
	for i in range(len(data)-period-1):
		tmp = data[i:(i+period), 0]
		X.append(tmp)
		Y.append(data[i + period, 0])
	return np.array(X), np.array(Y)

#city = input("enter the city name (for ex: nyc or chicago) : ")
citty = ['atlanta','chicago','nyc','portland']
for city in citty:
	filename = "./temperatures/"+city+".csv"

	dataframe = pd.read_csv(filename,usecols=[3])
	data = dataframe.values

	for i in range(data.shape[0]):
		if pd.isna(data[i][0]):
			data[i][0]=data[i-1][0]

	data = data.astype('float32')

	train_size = int(len(data)*0.995)
	test_size = len(data)-train_size

	train = data[0:train_size,:]
	test = data[train_size:len(data),:]

	period = 1
	X_train, Y_train = split_data(train, period)
	X_test, Y_test = split_data(test, period)

	model = Sequential()
	#hidden layer
	model.add(Dense(8, input_dim=period, activation='relu'))
	#output layer
	model.add(Dense(1))
	#create the architecture
	model.compile(loss='mean_squared_error', optimizer='adam')

	#train the network
	model.fit(X_train, Y_train, epochs=2, batch_size=2, verbose=2)

	Predict = model.predict(X_test)
	ans = Predict[:30]
	print(ans)
	plt.plot(Y_test, color='orange')
	plt.plot(Predict)
	plt.title(city.capitalize())
	plt.xlabel('No. of Days')
	plt.ylabel('Temperature in degree Celsius')
	plt.legend(["Actual Test Data", "Predicted Temperature"])
	plt.show()
