import pandas as pd
import numpy as py
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

df = pd.read_csv('vgsales.csv').dropna()
#Clean

# #Years
Years = df.groupby("Year")["Global_Sales"].sum()
fig1 = px.line(x = Years.index, y = Years.values, title = "Total Video Game Sales By Year")


# Platforms
plat = df.groupby("Platform")["Global_Sales"].sum()
fig2 = px.bar(x = plat.index, y = plat.values, title = "By Platform")


# Genres
gen = df.groupby("Genre")["Global_Sales"].sum()
fig3 = px.bar(x = gen.index, y = gen.values, title = "By Genre")


#Box Genre
df1 = df[df["Global_Sales"] < 60]
box1 = px.scatter(df1, x = "Year", y = "Global_Sales", color = "Genre", title = "Plot")

colormap = {"Racing":"red", "Platform" : "blue", "Sports" : "green", "Role-Playing" : "yellow", "Puzzle" : "purple", "Shooter" : "pink", "Simulation" : "magenta"} 
marker_col = df1["Genre"].map(colormap)

fig = make_subplots(rows = 2, cols = 2, subplot_titles=("Global Sales by Year", "Total Sales per Platform", "Total Sales per Genre", "Global Sales per Game coloured by Genre"))
fig.add_trace(go.Scatter(x = Years.index, y = Years.values),row = 1, col = 1)
fig.add_trace(go.Bar(x = plat.index, y = plat.values), row = 1, col = 2)
fig.add_trace(go.Bar(x = gen.index, y = gen.values), row = 2, col = 1)
fig.add_trace(go.Scatter(x = df1["Year"], y = df1["Global_Sales"], mode = "markers", marker = dict(color = marker_col)), row = 2, col = 2)
fig.update_layout(title = dict(text = "Video Game Sales", x = 0.49, y = 0.95, xanchor = "center"))
fig.show()

# fig.write_html("Video Game Interactive Graph", include_plotlyjs = 'cdn')