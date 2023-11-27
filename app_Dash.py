import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, html, dcc, callback, Output, Input, dash_table


app = Dash(__name__)


# Load and format the data -------------------------------------------------------------

df_reviews = pd.read_csv("Data/philly_reviews_asba.csv")
df_businesses = df_reviews.iloc[:, 1:15].drop_duplicates()
df_top10 = pd.read_csv("Data/top_10_coffee_shops.csv")
bi_grams_results = pd.read_csv('Data/top_10_bigrams.csv')
bi_grams_results = bi_grams_results.iloc[:, 1:]
# join the composite (average) sentiment for each business
df_temporary = df_reviews[['business_id', 'pss']].groupby('business_id').mean().reset_index()
df_businesses = pd.merge(df_businesses, df_temporary[['business_id','pss']],on='business_id', how='left')

# -----------------------------------------------------------------------------------------



# Create the geographic map, with each business as one point on the map
map_fig = px.scatter_mapbox(df_businesses, lat = 'latitude', lon = 'longitude',
                        #radius = 30,
                        center = dict(lat = 39.99, lon = -75.1), # manual- Philidelphia
                        zoom = 10,
                        mapbox_style = 'carto-positron', # this lowkey map style lets our color scheme stand out more
                        size_max = 20,
                        size = [70]*len(df_businesses), #each point is size 70
                        color = 'pss', # color based on avg of sentiment scores
                        color_continuous_scale = 'tealrose_r',
                        opacity=1,
                        width=1000,
                        height=500,
                        hover_name='name',
                        hover_data= {
                            #"size": False,   
                            "latitude": False,
                            "longitude": False,
                            "address": True,
                            #"attributes": True
                        },
                        labels={'pss': 'avg positive sentiment'}
                        )


# app layout including other visualizations
app.layout = html.Div([
    html.H1(children='Coffee Re-Brewer', style={'textAlign':'center'}),

    html.Div([

        html.Div([
            html.H2(children='Top 10 Coffee Shops by Sentiment Analysis'),
            # The top 10 coffee shops
            dash_table.DataTable(df_top10.to_dict('records'), [{"name": i, "id": i} for i in df_top10[['name', 'composite_score']]])
            ], style={'width': '30%', 'float': 'left', 'margin-right': '5%', 'margin-top': '0%'}),

        html.Div([
            html.H2(children='The Landscape of Coffee Quality'),
                # put the geo-map in the html structure
                dcc.Graph(figure=map_fig)
            ], style={'width': '55%', 'float': 'right', 'margin-left': '5%', 'margin-top': '0%'}),

    ], style={'width': '65%', 'float': 'left'}),


    html.Div([
        html.H2(children='Coffee Sentiment Over Time'),
        # dropdown of sentiment over time -- see update_graph() below
        dcc.Dropdown(df_reviews.name.unique(), 'Vineyards Cafe', id='dropdown-selection'),
        dcc.Graph(id='graph-content'),
        ], style={'width': '65%', 'float': 'left'}),
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df_reviews[df_reviews.name==value]
    return px.scatter(dff, x='review_date', y='pss', color=dff['pss'], color_continuous_scale='tealrose_r',#['red', 'green'],
                      hover_name='review_text', facet_col_wrap=30,
                      size = [30]*len(dff),
                      labels={'review_date':'date of customer review', 'pss': 'coffee sentiment score'}
                      )

if __name__ == '__main__':
    app.run(debug=True)