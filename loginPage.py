import base64
import time

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash import callback_context
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from app import app, database

# ---------------------------------------- DATA ----------------------------------------
logo_image = "logo.png"

# --------------------------------------- IMAGES ---------------------------------------
ds_logo_encoded = base64.b64encode(open(logo_image, "rb").read())

img_ds = html.Img(
    src=f"data:image/png;base64,{ds_logo_encoded.decode()}",
    style={
        "float": "centre",
        "width": "50%",
    },
)

# --------------------------------------- CARDS ----------------------------------------
login_card = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Input(
                    id="input_user_name_login",
                    placeholder="user name",
                    type="text",
                    className="mb-3",
                ),
                dbc.Input(
                    id="input_password_login",
                    placeholder="password",
                    type="text",
                    className="mb-3",
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
                            href="/signup",
                        ),
                    ]
                ),
            ]
        ),
    ],
    color="light",
    inverse=True,
)

alert_login = dbc.Alert(
    id="alert_login",
    dismissable=True,
    is_open=False,
)

# --------------------------------------- LAYOUT ---------------------------------------
layout = dbc.Container(
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
                        login_card,
                        width={"size": 6, "offset": 3},
                    ),
                    align="center",
                    className="m-5",
                ),
                # row3: alert
                dbc.Row(
                    dbc.Col(
                        alert_login,
                        width={"size": 6, "offset": 3},
                    ),
                    align="center",
                    className="m-5",
                ),
            ]
        )
    ]
)


# ------------------------------------- CALLBACKS --------------------------------------
@app.callback(
    [
        Output("alert_login", "is_open"),
        Output("alert_login", "color"),
        Output("alert_login", "children"),
    ],
    [
        Input("button_login", "n_clicks"),
    ],
    [
        State("input_user_name_login", "value"),
        State("input_password_login", "value"),
    ],
)
def validate_login(
    button_login_n_clicks,
    input_user_name_login_value,
    input_password_login_value,
):
    if button_login_n_clicks:
        if (
            input_user_name_login_value is not None
            and ~input_user_name_login_value.isspace()
        ):
            if (
                input_password_login_value is not None
                and ~input_password_login_value.isspace()
            ):
                if database.check_user_exists(
                    by="email", value=input_user_name_login_value
                ) and database.check_password_is_correct(
                    password=input_password_login_value
                ):
                    return (
                        True,
                        "success",
                        "Please wait while we redirect you",
                    )
                else:
                    return (
                        True,
                        "danger",
                        "Incorrect Username or Password entered",
                    )

            else:
                return (
                    True,
                    "danger",
                    "Please enter your password.",
                )
        else:
            return (
                True,
                "danger",
                "Please enter your username.",
            )
    else:
        raise PreventUpdate


@app.callback(
    Output("url", "pathname"),
    [
        Input("button_login", "n_clicks"),
        Input("alert_login", "color"),
    ],
)
def change_pathname(
    button_login_n_clicks,
    alert_login_color,
):
    if button_login_n_clicks and alert_login_color == "success":
        time.sleep(1)
        return "/selector"

    else:
        raise PreventUpdate
