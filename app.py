import pandas as pd
import plotly.express as px
import json

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
fig.show()
