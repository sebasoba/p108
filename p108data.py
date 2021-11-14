import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("studentdata.csv")

fig = ff.create_distplot(df["level"].tolist(),["attempt"])
fig.show()