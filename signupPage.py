import base64

import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from app import app, database

# ---------------------------------------- DATA ----------------------------------------
gender_int_to_str = {"1": "Female", "2": "Male"}

# --------------------------------------- IMAGES ---------------------------------------
logo_image = "logo.png"
ds_logo_encoded = base64.b64encode(open(logo_image, "rb").read())
ds_logo_decoded = f"data:image/png;base64,{ds_logo_encoded.decode()}"

# --------------------------------------- CARDS ----------------------------------------
# create signup card with text fields and buttons to create account and go back to login page
signup_card = dbc.Card(
    [
        dbc.CardImg(src=ds_logo_decoded, top=True),
        dbc.CardBody(
            [
                # text fields for user to input information
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
                        # create dropdown menu for gender
                        dbc.InputGroupAddon(
                            "Gender",
                            addon_type="prepend",
                        ),
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
                # create buttons below text boxes
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Button(
                                # back button
                                children="back",
                                id="button_back_signup",
                                color="primary",
                                className="m-3",
                                href="/login",
                                external_link=True,
                            ),
                            width={"size": "auto"},
                        ),
                        dbc.Col(
                            dbc.Button(
                                # create button
                                children="create",
                                id="button_create_signup",
                                color="primary",
                                className="m-3",
                            ),
                            width={"size": "auto"},
                        ),
                    ],
                    justify="center",
                ),
            ]
        ),
    ],
    color="light",
    inverse=True,
)

# alert for visual confirmation
alert_signup = dbc.Alert(
    id="alert_signup",
    dismissable=True,
    is_open=False,
)

# --------------------------------------- LAYOUT ---------------------------------------
layout = dbc.Container(
    [
        html.Div(
            [
                # row1: signup
                dbc.Row(
                    dbc.Col(
                        signup_card,
                        width={"size": 6, "offset": 3},
                    ),
                    align="center",
                    className="m-5",
                ),
                # row2: alert
                dbc.Row(
                    dbc.Col(
                        alert_signup,
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
# AppCallback to create new user
@app.callback(
    [
        Output("alert_signup", "is_open"),
        Output("alert_signup", "color"),
        Output("alert_signup", "children"),
    ],
    [Input("button_create_signup", "n_clicks")],
    [
        State("input_user_name_signup", "value"),
        State("input_password_signup", "value"),
        State("input_first_name_signup", "value"),
        State("input_last_name_signup", "value"),
        State("input_gender_select", "value"),
    ],
)
def create_new_user(
    button_create_signup_n_clicks,
    input_user_name_signup_value,
    input_password_signup_value,
    input_first_name_signup_value,
    input_last_name_signup_value,
    input_gender_select_value,
):
    if button_create_signup_n_clicks:
        if (
            # if user name is not blank
            input_user_name_signup_value is not None
            and ~input_user_name_signup_value.isspace()
        ):

            if (
                # if password is not blank
                input_password_signup_value is not None
                and ~input_password_signup_value.isspace()
            ):

                if (
                    # if first name is not blank
                    input_first_name_signup_value is not None
                    and ~input_first_name_signup_value.isspace()
                ):
                    if (
                        # if last name is not blank
                        input_last_name_signup_value is not None
                        and ~input_last_name_signup_value.isspace()
                    ):

                        if input_gender_select_value is not None:
                            # if gender is not blank
                            database.create_new_user(
                                # create new user with user inputs
                                first_name=input_first_name_signup_value,
                                last_name=input_last_name_signup_value,
                                gender=gender_int_to_str[input_gender_select_value],
                                email=input_user_name_signup_value,
                                password=input_password_signup_value,
                            )
                            return (
                                # changes alert attributes for visual feedback
                                True,
                                "success",
                                "Account created successfully, please go back and login with your new details",
                            )

                        else:
                            return (
                                # changes alert attributes for visual feedback
                                True,
                                "danger",
                                "Please enter your gender.",
                            )

                    else:
                        return (
                            # changes alert attributes for visual feedback
                            True,
                            "danger",
                            "Please enter your last name.",
                        )

                else:
                    return (
                        # changes alert attributes for visual feedback
                        True,
                        "danger",
                        "Please enter your first name.",
                    )

            else:
                return (
                    # changes alert attributes for visual feedback
                    True,
                    "danger",
                    "Please enter your password.",
                )

        else:
            return (
                # changes alert attributes for visual feedback
                True,
                "danger",
                "Please enter your username.",
            )
    else:
        raise PreventUpdate
