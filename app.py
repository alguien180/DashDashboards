#import micropip
#await micropip.install('dash-mantine-components')
#await micropip.install('dash-iconify')
from dash import Dash, html, dcc
import dash_mantine_components as dmc


app = Dash(__name__)
server = app.server

projects_tab=dmc.Container(
    [
        dmc.Title("Dashboard Hub",order=1),
        dmc.Text("Step 3: Tabs are working.", c= "dimmed"),
    ],
    size="md",
    pt=30,
)

resume_tab=dmc.Container(
    [
        dmc.Title("Resume", order=2),
        dmc.Text("Step 3: Placeholder recume content.",c="dimmed"),
    ],
    size="md",
    pt=30,
)

references_tab=dmc.Container(
    [
    dmc.Title("Resume",order=2),
    dmc.Text("Step 3: Placeholser resume content", c="dimmed"),    
    ],
    size="md",
    pt=30,
)

references_tab= dmc.Container(
    [
        dmc.Title("References",order=2),
        dmc.Text("Step 3: Placeholder references content",c="dimmed"),

    ],
    size="md",
    pt=30,
)


app.layout = dmc.MantineProvider(
    theme={"colorScheme":"dark"},
    withGlobalClasses =True,
    children=[
        dmc.Tabs(
            [
                #Tab buttons (top row)
                dmc.TabsList(
                    [
                    dmc.TabsTab("Projects",value="projects"),
                    dmc.TabsTab("Resume", value="resume"),
                    dmc.TabsTab("References",value="references"),
                    ]
                ),
            
            
            #Tab content panels
            dmc.TabsPanel(projects_tab, value="projects"),
            dmc.TabsPanel(resume_tab,value="resume"),
            dmc.TabsPanel(references_tab,value="references"),
            ],
            value="projects",
            variant="pills",
            orientation="horizontal",
        ),
    ],
)



if __name__ == "__main__":
    print("Starting Dash server on http")
    app.run(debug=False)