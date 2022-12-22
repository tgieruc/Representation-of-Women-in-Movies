import plotly.express as px
from dash import Dash, dcc, html, Input, Output, no_update
import plotly.graph_objects as go
import pandas as pd
import pickle

data_folder = '../data/'
pickle_folder = data_folder + 'pickles/'

characters = pickle.load(open(pickle_folder + 'characters.p', 'rb'))
movies = pickle.load(open(pickle_folder + 'movies.p', 'rb'))
df_actors = pickle.load(open("actors_with_image.p","rb"))


fig = px.bar(df_actors, y='actor_metric', x='actor_name', color ="combined_gender")
fig.update_layout( xaxis={'categoryorder':'array', 'categoryarray':df_actors.actor_name})

fig.update_traces(hoverinfo="none", hovertemplate=None)

app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id="graph-basic-2", figure=fig, clear_on_unhover=True),
    dcc.Tooltip(id="graph-tooltip"),
])

@app.callback(
    Output("graph-tooltip", "show"),
    Output("graph-tooltip", "bbox"),
    Output("graph-tooltip", "children"),
    Input("graph-basic-2", "hoverData"),
)
def display_hover(hoverData):
    if hoverData is None:
        return False, no_update, no_update

    # demo only shows the first point, but other points may also be available
    pt = hoverData["points"][0]
    bbox = pt["bbox"]
    num = pt["pointNumber"]
    name = pt["x"]


    df_row = df_actors.loc[df_actors["actor_name"] == name]
    img_src = df_row['img_link']

    children = [
        html.Div([
            html.Img(src=img_src, style={"width": "100%"}),
        ], style={'width': '200px', 'white-space': 'normal'})
    ]

    return True, bbox, children


if __name__ == "__main__":
    app.run_server(debug=False, host = "localhost", port = 8005)