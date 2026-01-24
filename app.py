#import micropip
#await micropip.install('dash-mantine-components')
#await micropip.install('dash-iconify')


from dash import Dash, html, dcc

def asset(name:str)-> str:
    "Return the URL to an image in /assets"
    return app.get_asset_url(name)

app = Dash(__name__)
server = app.server
app.layout = html.Dic(
    [
        html.H1("Dashboard Hub"),
        html.P ("Step 1: deployed successfully"),
    ],
    style={"padding":"20px"},
)

if __name__ =="main":
    app.run(debug=False)