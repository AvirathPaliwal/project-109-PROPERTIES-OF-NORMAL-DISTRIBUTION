import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import csv
import random

df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()

mean = sum(data) / len(data)
std = statistics.stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)

first_std_deviation_start , first_std_deviation_end = mean - std , mean+std
second_std_deviation_start , second_std_deviation_end = mean-(2*std) , mean+(2*std)
third_std_deviation_start , third_std_deviation_end = mean-(3*std) , mean+(3*std)

fig = ff.create_distplot([data], ["reading scores"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean] , y=[0,0.17] , mode ='lines' , name ="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0,0.17] ,mode="lines" , name="SD 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0,0.17] ,mode="lines" , name="SD 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0,0.17] ,mode="lines" , name="SD 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0,0.17] ,mode="lines" , name="SD 2"))

list_of_data_within_1_std = [result for result in data if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std = [result for result in data if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std = [result for result in data if result > third_std_deviation_start and result < third_std_deviation_end]

print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))
print("SD of this data is {}".format(std))
print("\n")
print("{}% of data lies within 1 Std".format(len(list_of_data_within_1_std)*100.0/len(data)))
print("{}% of data lies within 2 Std".format(len(list_of_data_within_2_std)*100.0/len(data)))
print("{}% of data lies within 3 Std".format(len(list_of_data_within_3_std)*100.0/len(data)))