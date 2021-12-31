import statistics
import pandas as pd
import plotly.figure_factory as ff
import random
import plotly.graph_objects as go

df = pd.read_csv('medium_data.csv')
data = df['reading_time'].tolist()

def randomSetOfMean(counter):
    dataset = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def showFigure(meanList):
    df = meanList
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],['reading_time'], show_hist=False)
    fig.add_trace(go.Scatter(x = [mean,mean], y = [0,1], mode = 'lines', name = 'Mean'))
    fig.show()

def setup():
    meanList = []
    for i in range(0,100):
        setOfMeans = randomSetOfMean(30)
        meanList.append(setOfMeans)
    showFigure(meanList)
setup()
