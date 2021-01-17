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
    [
        dcc.Location(id="url", refresh=False),
        html.Div(id="page-content"),
    ]
)


# change the main app page layout depending on the pathname
# if the pathname is not defined, use login layout
@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname"),
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


# dcc.Link('Navigate to "/page-2"', href='/page-2')
# @app.callback(
#     Output("url", "pathname"),
#     [
#         Input("button_login", "n_clicks"),
#         Input("button_signup", "n_clicks"),
#         Input("button_back_signup", "n_clicks"),
#         Input("button_create_signup", "n_clicks"),
#         Input("alert_login", "color"),
#         Input("alert_signup", "color"),
#     ],
# )
# def change_pathname(
#     button_login_n_clicks,
#     button_signup_n_clicks,
#     button_back_signup_n_clicks,
#     button_create_signup_n_clicks,
#     alert_login_color,
#     alert_signup_color,
# ):
#     ctx = callback_context

#     if not ctx.triggered:
#         raise PreventUpdate

#     else:
#         button_id = ctx.triggered[0]["prop_id"].split(".")[0]

#         if button_id == "button_login" and alert_login_color == "success":
#             time.sleep(1)
#             return "/selector"

#         elif button_id == "button_signup":
#             time.sleep(1)
#             return "/signup"

#         elif button_id == "button_back_signup":
#             time.sleep(0.5)
#             return "/login"

#         elif button_id == "button_create_signup" and alert_signup_color == "success":
#             time.sleep(1)
#             return "/login"

#         else:
#             raise PreventUpdate


if __name__ == "__main__":
    app.run_server(
        debug=True,
        host="0.0.0.0",
        port="8080",
    )
