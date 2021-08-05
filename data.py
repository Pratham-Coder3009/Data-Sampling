import pandas as pd
import plotly_express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as st
import random

df = pd.read_csv(r'F:\Python Projects\Data Sampling\medium_data.csv')
data = df["reading_time"].to_list()
fig = ff.create_distplot([data], ["reading_time"], show_hist=False)
fig.show()

population_mean = st.mean(data)
print("Population Mean = ", population_mean)
population_st_dev = st.stdev(data)
print("Standard Deviation = ", population_st_dev)

dataset = []
for i in range(0,1000):
    random_index = random.randint(0, len(data))
    value = data[random_index]
    dataset.append(value)
mean = st.mean(dataset)
st_dev = st.stdev(dataset)
print("Mean of 1000 values=", mean)
print("Standard deviation of 1000 values = ",st_dev)
