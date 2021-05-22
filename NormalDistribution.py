import random
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import csv
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")
mathList = df["reading score"].to_list()

mean = sum(mathList)/len(mathList)
median = statistics.median(mathList)
mode = statistics.mode(mathList)
standardDV = statistics.stdev(mathList)
print("Mean: ", mean)
print("Median: ", median)
print("Mode: ", mode)
print("Standard Deviation: ", standardDV)

#print(x)
fig = ff.create_distplot([mathList], ["Result"])

first_stdev_start, first_stdev_end = mean - standardDV, mean + standardDV
second_stdev_start, second_stdev_end = mean - (2*standardDV), mean + (2*standardDV)
third_stdev_start, third_stdev_end = mean - (3*standardDV), mean + (3*standardDV)

fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_stdev_start, first_stdev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_stdev_end, first_stdev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_stdev_start, second_stdev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_stdev_end, second_stdev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[third_stdev_start, third_stdev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))
fig.add_trace(go.Scatter(x=[third_stdev_end, third_stdev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))
fig.show()