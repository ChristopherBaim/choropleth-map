import pandas as pd
import plotly.express as px
import json
import dash
import dash_core_components as dcc
import dash_html_components as html


with open('MA10p_GeoJSON.geojson') as f:
  towns = json.load(f)

df = pd.read_csv("MADataIDs.csv", dtype={"NAME": str})
for x in towns["features"]:
    x['id'] = x['properties']['NAME']

fig = px.choropleth(df, geojson=towns, locations='NAME', color='Rep',
                           color_continuous_scale="bluered",
                           range_color=(0, 1),
                           labels={'Dem':'Democrat Vote %'},
                            )

fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
#fig.show()

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title="polls"

########### Set up the layout
app.layout = html.Div(children=[
    html.H1("Choropleth Map of MA 2016 Election"),
    dcc.Graph(
        id='MA',
        figure=fig
    )
    ]
)

if __name__ == '__main__':
    app.run_server()
