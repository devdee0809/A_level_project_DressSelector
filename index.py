import time

import dash_core_components as dcc
import dash_html_components as html
from dash import callback_context
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

import loginPage
import selectorPage
import signupPage
from app import app

# define the main app layout
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content"),]
)


# change the main app page layout depending on the pathname
# if the pathname is not defined, use login layout
@app.callback(
    Output("page-content", "children"), Input("url", "pathname"),
)
def change_page_layout(pathname):
    if pathname == "/login":
        return loginPage.layout
    elif pathname == "/signup":
        return signupPage.layout
    elif pathname == "/selector":
        return selectorPage.layout
    else:
        return loginPage.layout


if __name__ == "__main__":
    app.run_server(
        debug=True, host="0.0.0.0", port="8080",
    )
