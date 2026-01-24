import dash 
import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
from pathlib import Path

app = Dash(__name__)

# import and cleand data (importing csv into pandas)
BASE_DIR=Path(__file__).resolve().parent
csv_path = BASE_DIR.parent / "intro_bees.csv"
df = pd.read_csv(csv_path)

df = df.groupby(['State','ANSI','Affected by', 'Year', 'state_code'])[['Pct of Colonies Impacted']].mean()
df.reset_index(inplace=True)
print(df[:5])

#----------------
#App layout
#where the actual dashboard is
app.layout = html.Div([
    html.H1("Web Application Dashboards with Dash", style={'text-align':'center'}),

    dcc.Dropdown(id="slct_year",
                options=[
                     {"label":"2015","value":2015},
                     {"label":"2016","value":2016},
                     {"label":"2017","value":2017},
                     {"label":"2018", "value":2018}],
                multi=False,
                value=2015,
                style={'width':"40%"}
                 ),
    html.Div(id='output_container',children=[]),
    html.Br(), #space
    dcc.Graph(id='my_bee_map',figure={})

])
# -------------
# Connect the Plotly graphs with Dash Components

@app.callback(
    Output(component_id='output_container', component_property='children'),
    Output(component_id='my_bee_map', component_property='figure'),
    Input(component_id='slct_year',component_property='value'),
)

def upgrade_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The year chosen by user was: {}".format(option_slctd)

    dff = df.copy()
    dff = dff[dff["Year"] == option_slctd]
    dff = dff[dff["Affected by"]=="Varroa_mites"]

#Plotly Express
    fig = px.choropleth(

        dff,
        locationmode='USA-states',
        locations='state_code',
        scope="usa",
        color="Pct of Colonies Impacted",
        hover_data=['State','Pct of Colonies Impacted'],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={'Pct of Colonies Impacted':'% of Bee Colonies'},
        template='plotly_dark'
    )
    return container, fig
#---main
if __name__=='__main__':
    app.run(debug=True)