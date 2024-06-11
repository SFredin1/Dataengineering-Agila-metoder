import matplotlib.pyplot as plt
import plotly_express as px
import numpy as np
import pandas as pd
import dash
from dash import Dash, dcc, html
from sklearn import datasets

# Simple plot using matplotlib
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

# Example using plotly express
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length")
fig.show()

# Simple DataFrame using pandas
df = pd.DataFrame({
    'A': np.random.randn(5),
    'B': np.random.randn(5)
})
print(df)

# Simple Dash app
app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)