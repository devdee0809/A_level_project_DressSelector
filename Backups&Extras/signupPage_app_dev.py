import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.FLATLY],
)


# ---------------------------------------- DATA ----------------------------------------

# --------------------------------------- CARDS ----------------------------------------
card_login = dbc.Card(
    [
        # dbc.CardHeader(
        #     children="Components",
        #     className="card-header mb-0",
        # ),
        dbc.CardBody(
            [
                dbc.Input(
                    id="input_user_name",
                    placeholder="user name",
                    type="text",
                    className="mb-3",
                ),
                dbc.Input(
                    id="input_password",
                    placeholder="password",
                    type="text",
                    className="mb-3",
                ),
                dbc.Collapse(
                    [
                        dbc.Input(
                            id="input_first_name",
                            placeholder="first name",
                            type="text",
                            className="mb-3",
                        ),
                        dbc.Input(
                            id="input_last_name",
                            placeholder="last name",
                            type="text",
                            className="mb-3",
                        ),
                        dbc.DropdownMenu(
                            label="Gender",
                            children=[
                                dbc.DropdownMenuItem("Female"),
                                dbc.DropdownMenuItem("Male"),
                                dbc.DropdownMenuItem("Prefer Not To Say"),

                            ],
                            className="mb-3",
                        ),
                    ],
                    id="collapse",
                ),
                dbc.Row(
                    [
                        dbc.Button(
                            children="login",
                            id="button_login",
                            color="primary",
                            className="m-3",
                        ),
                        dbc.Button(
                            children="signup",
                            id="button_signup",
                            color="primary",
                            className="m-3",
                        ),
                    ]
                ),
            ]
        ),
    ],
    color="light",
    inverse=True,
)

alert = dbc.Alert(
    id="alert",
    dismissable=True,
    is_open=False,
)


# --------------------------------------- LAYOUT ---------------------------------------
app.layout = dbc.Container(
    [
        html.Div(
            [
                # row1: logos
                dbc.Row(
                    dbc.Col(
                        html.Div("TITLE"),
                        width={"size": 6, "offset": 3},
                    ),
                    align="center",
                    className="m-5",
                ),
                # row2: login
                dbc.Row(
                    dbc.Col(
                        card_login,
                        width={"size": 6, "offset": 3},
                    ),
                    align="center",
                    className="m-5",
                ),
                # row3: success
                dbc.Row(
                    dbc.Col(
                        alert,
                        width={"size": 6, "offset": 3},
                    ),
                    align="center",
                    className="m-5",
                ),
                html.Div(id="app-1-display-value"),
                dcc.Link("Go to App 2", href="/apps/app2"),
            ]
        )
    ]
)


# ------------------------------------- CALLBACKS --------------------------------------
@app.callback(
    [
        Output("alert", "is_open"),
        Output("alert", "color"),
        Output("alert", "children"),
    ],
    [
        Input("button_login", "n_clicks"),
    ],
    [
        State("input_user_name", "value"),
        State("input_password", "value"),
    ],
)
def login(
    login_button_n_clicks,
    input_user_name_value,
    input_password_value,
):
    if login_button_n_clicks:
        if input_user_name_value is not None and ~input_user_name_value.isspace():
            if input_password_value is not None and ~input_password_value.isspace():
                if (
                    input_user_name_value == "test.email@gmail.com"
                    and input_password_value == "1234"
                ):
                    return True, "success", "Please wait while we redirect you"
                else:
                    return True, "danger", "Incorrect Username or Password entered"

            else:
                return True, "danger", "Please enter your password username."

        else:
            return True, "danger", "Please enter your username."
    else:
        raise PreventUpdate


@app.callback(
    Output("collapse", "is_open"),
    [Input("button_signup", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(button_signup_n_clicks, collapse_is_open):
    if button_signup_n_clicks:
        return not collapse_is_open
    return collapse_is_open


# @app.callback(
#     Output("collapse", "label"),
#     [Input("children", )]


app.run_server(
    debug=True,
    host="0.0.0.0",
    port="8080",
)
