import pandas as pd
import plotly.express as px 

df = pd.read_csv("St.csv")
fig = px.scatter(df, x = "Date", y = "Cases", size="Percentage", size_max=3170, title="CovidCases")
fig.show()