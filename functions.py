#!/usr/bin/python 

import numpy as np
import pandas as pd

import plotly.graph_objs as go
import matplotlib.pyplot as plt

def make_piechart(df,column,title,mid_text):
    #'''
    #creates a pie chart from the dataframe.
    #'''
    labels = list(df[column].unique())
    values = df[column].value_counts()

    # Use `hole` to create a donut-like pie chart
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.6)])
    fig.update_layout( title_text=title,
    
    # Add annotations in the center of the donut pies.
    annotations=[dict(text=mid_text, x=0.5, y=0.5, font_size=20, showarrow=False)])
    fig.update_layout(autosize=False)
    fig.show()