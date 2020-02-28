import pandas
import matplotlib.pyplot as plt

date = pandas.read_csv('TimeSeries_DataPoints.csv', usecols=[1], engine='python', skipfooter=3)
date_set = date.values
date_set = date_set[-1000:-1] #01/18/2016 - 11/15/2019

dataframe = pandas.read_csv('TimeSeries_DataPoints.csv', usecols=[2], engine='python', skipfooter=3)
data_set = dataframe.values
data_set = data_set.astype('float32')
data_set = data_set[-999:]

plt.plot(data_set, color="g")
plt.plot(306, data_set[306], color="m", marker="d")
plt.plot(321, data_set[321], color="m", marker="d")
plt.plot(324, data_set[324], color="m", marker="d")
plt.show()
