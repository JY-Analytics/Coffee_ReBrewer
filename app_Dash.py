#from flask import Flask, render_template, request
#import json
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, html, dcc, callback, Output, Input


app = Dash(__name__)

df_reviews = pd.read_csv("Data/philly_reviews_asba.csv")
#df_reviews['date'] = pd.to_datetime(df_reviews['date'], format='%B %d, %Y')
df_businesses = df_reviews.iloc[:, 1:15].drop_duplicates()


fig2 = go.Figure(data=go.Scattergeo(
        lon = df_businesses['longitude'],
        lat = df_businesses['latitude'],
        text = df_businesses['name'],
        mode = 'markers',
        marker_color = df_businesses['stars_x'],
        ))

fig2.update_layout(title = 'Coffee Shops in Philadelphia <br>(hover for more info)', 
    geo=dict(showland=True), autosize=False, width=1200, height=800)
fig2.update_geos(fitbounds="locations")


app.layout = html.Div([
    html.H1(children='Coffee Re-Brewer', style={'textAlign':'center'}),
    dcc.Dropdown(df_reviews.name.unique(), 'Vineyards Cafe', id='dropdown-selection'),
    dcc.Graph(id='graph-content'),
    dcc.Graph(figure=fig2)

])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df_reviews[df_reviews.name==value]
    return px.scatter(dff, x='date', y='pss', color='name', title='Coffee Sentiment over Time')

if __name__ == '__main__':
    app.run(debug=True)