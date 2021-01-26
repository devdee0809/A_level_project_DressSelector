import base64

import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from app import app, database

# ---------------------------------------- DATA ----------------------------------------
logo_image = "logo.png"

# --------------------------------------- IMAGES ---------------------------------------
ds_logo_encoded = base64.b64encode(open(logo_image, "rb").read())
ds_logo_decoded = f"data:image/png;base64,{ds_logo_encoded.decode()}"

# --------------------------------------- CARDS ----------------------------------------
signup_card = dbc.Card(
    [
        dbc.CardImg(src=ds_logo_decoded, top=True),
        dbc.CardBody(
            [
                dbc.Input(
                    id="input_user_name_signup",
                    placeholder="user name",
                    type="text",
                    className="mb-3",
                ),
                dbc.Input(
                    id="input_password_signup",
                    placeholder="password",
                    type="text",
                    className="mb-3",
                ),
                dbc.Input(
                    id="input_first_name_signup",
                    placeholder="first name",
                    type="text",
                    className="mb-3",
                ),
                dbc.Input(
                    id="input_last_name_signup",
                    placeholder="last name",
                    type="text",
                    className="mb-3",
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupAddon("Gender", addon_type="prepend",),
                        dbc.Select(
                            id="input_gender_select",
                            options=[
                                {"label": "Female", "value": 1},
                                {"label": "Male", "value": 2},
                            ],
                        ),
                    ],
                    className="mb-3",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Button(
                                children="delete",
                                id="button_delete_signup",
                                color="primary",
                                className="m-3",
                                href="/login",
                            ),
                        ),
                        dbc.Col(
                            dbc.Button(
                                children="update",
                                id="button_update_signup",
                                color="primary",
                                className="m-3",
                            ),
                        ),
                    ]
                ),
            ]
        ),
    ],
    color="light",
    inverse=True,
)

alert_signup = dbc.Alert(id="alert_signup", dismissable=True, is_open=False,)

# --------------------------------------- LAYOUT ---------------------------------------
app.layout = dbc.Container(
    [
        html.Div(
            [
                # row1: signup
                dbc.Row(
                    dbc.Col(signup_card, width={"size": 6, "offset": 3},),
                    align="center",
                    className="m-5",
                ),
                # row2: alert
                dbc.Row(
                    dbc.Col(alert_signup, width={"size": 6, "offset": 3},),
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
        Output("alert_signup", "is_open"),
        Output("alert_signup", "color"),
        Output("alert_signup", "children"),
    ],
    [Input("button_update_signup", "n_clicks")],
    [
        State("input_user_name_signup", "value"),
        State("input_password_signup", "value"),
        State("input_first_name_signup", "value"),
        State("input_last_name_signup", "value"),
        State("input_gender_select", "value"),
    ],
)
def validate_signup(
    button_update_signup_n_clicks,
    input_user_name_signup_value,
    input_password_signup_value,
    input_first_name_signup_value,
    input_last_name_signup_value,
    input_gender_select_value,
):
    if button_update_signup_n_clicks:
        if (
            input_user_name_signup_value is not None
            and ~input_user_name_signup_value.isspace()
        ):

            if (
                input_password_signup_value is not None
                and ~input_password_signup_value.isspace()
            ):

                if (
                    input_first_name_signup_value is not None
                    and ~input_first_name_signup_value.isspace()
                ):
                    if (
                        input_last_name_signup_value is not None
                        and ~input_last_name_signup_value.isspace()
                    ):

                        if input_gender_select_value is not None:
                            database.create_new_user(
                                first_name=input_first_name_signup_value,
                                last_name=input_last_name_signup_value,
                                gender=input_gender_select_value,
                                email=input_user_name_signup_value,
                                password=input_password_signup_value,
                            )
                            return (
                                True,
                                "success",
                                "Account created successfully, please go back and login with your new details",
                            )

                        else:
                            return (
                                True,
                                "danger",
                                "Please enter your gender.",
                            )

                    else:
                        return (
                            True,
                            "danger",
                            "Please enter your last name.",
                        )

                else:
                    return (
                        True,
                        "danger",
                        "Please enter your first name.",
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


# ------------------------------------- CALLBACKS --------------------------------------


app.run_server(
    debug=True, host="0.0.0.0", port="8080",
)
