import csv
import random
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("C:/Users/jaska/OneDrive/Desktop/data/python/class/projects/pro 110/medium_data.csv")
data = df["reading_time"].tolist()
population_mean = statistics.mean(data)
print("Population mean = ", population_mean)

def random_set_of_means(counter):
    dataset = []

    for i in range(0, counter):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    
    df=mean_list
    fig = ff.create_distplot([df], ["Reading time"], show_hist=False)
    fig.show()

def setup():
    mean_list = []

    for i in range(0, 100):
        set_of_means = random_set_of_means(30)
        mean_list.append(set_of_means)

    show_fig(mean_list)

    sample_mean=statistics.mean(mean_list)
    print("sample mean", sample_mean)

setup()