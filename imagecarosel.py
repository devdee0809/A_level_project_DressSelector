import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import numpy as np

filenames = [
    "https://raw.githubusercontent.com/plotly/datasets/master/mitochondria.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/6/6c/HeLa_cells_stained_with_Hoechst_33258.jpg",
]

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app = dash.Dash()

app.layout = html.Div(
    [
        html.Div(id="img", className="six columns"),
        html.Div(id="img2", className="six columns"),
        html.Button(id="next", n_clicks=0, children="Next", style={"fontSize": 14}),
        dcc.Interval(id="interval", interval=3000),
    ]
)


@app.callback(Output("img", "children"), [Input("next", "n_clicks")])
def shownext(clicks):
    if clicks > 0:
        print("in shownext")
        return [html.H3("Triggered by button"), html.Img(src=filenames[clicks % 2])]


@app.callback(Output("img2", "children"), [Input("interval", "n_intervals")])
def display_image(n):
    if n is None:
        return dash.no_update
    print("in interval")
    return [html.H3("Triggered by interval"), html.Img(src=filenames[n % 2])]


if __name__ == "__main__":
    app.run_server(debug=True, port=8868)
