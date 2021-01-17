from inspect import indentsize

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash_bootstrap_components._components.CardBody import CardBody
from dash_bootstrap_components._components.Col import Col

from app import app, database

# ---------------------------------------- DATA ----------------------------------------

# --------------------------------------- IMAGES ---------------------------------------

# --------------------------------------- CARDS ----------------------------------------
headwear = (
    dbc.Card(
        [
            dbc.CardBody(html.P("Headwear", className="card-text")),
            dbc.CardImg(
                src="/Users/devdeepak/Desktop/GitHub/DressSelector/dash/images/2467.jpg",
                top=True,
            ),
            dbc.Row(
                [
                    dbc.Button(
                        children="🔀",
                        id="headwear_randomisce",
                        color="primary",
                        className="m-3",
                    ),
                    dbc.Button(
                        children="✓",
                        id="headwear_tick",
                        color="primary",
                        className="m-3",
                    ),
                    dbc.Button(
                        children="✖",
                        id="headwear_cross",
                        color="primary",
                        className="m-3",
                    ),
                ],
                justify="center",
            ),
        ]
    ),
)


topwear = (
    dbc.Card(
        [
            dbc.CardBody(html.P("Topwear", className="card-text")),
            dbc.CardImg(
                src="/Users/devdeepak/Desktop/GitHub/DressSelector/dash/images/2467.jpg",
                top=True,
            ),
            dbc.Row(
                [
                    dbc.Button(
                        children="🔀",
                        id="topwear_randomise",
                        color="primary",
                        className="m-3",
                    ),
                    dbc.Button(
                        children="✓",
                        id="topwear_tick",
                        color="primary",
                        className="m-3",
                    ),
                    dbc.Button(
                        children="✖",
                        id="topwear_cross",
                        color="primary",
                        className="m-3",
                    ),
                ],
                justify="center",
            ),
        ]
    ),
)

bottomwear = (
    dbc.Card(
        [
            dbc.CardBody(html.P("Bottomwear", className="card-text")),
            dbc.CardImg(
                src="/Users/devdeepak/Desktop/GitHub/DressSelector/dash/images/2467.jpg",
                top=True,
            ),
            dbc.Row(
                [
                    dbc.Button(
                        children="🔀",
                        id="bottomwear_randomise",
                        color="primary",
                        className="m-3",
                    ),
                    dbc.Button(
                        children="✓",
                        id="bottomwear_tick",
                        color="primary",
                        className="m-3",
                    ),
                    dbc.Button(
                        children="✖",
                        id="bottomwear_cross",
                        color="primary",
                        className="m-3",
                    ),
                ],
                justify="center",
            ),
        ]
    ),
)


footwear = (
    dbc.Card(
        [
            dbc.CardBody(html.P("Footwear", className="card-text")),
            dbc.CardImg(
                src="/Users/devdeepak/Desktop/GitHub/DressSelector/dash/images/2467.jpg",
                top=True,
            ),
            dbc.Row(
                [
                    dbc.Button(
                        children="🔀",
                        id="footwear_randomise",
                        color="primary",
                        className="m-3",
                    ),
                    dbc.Button(
                        children="✓",
                        id="footwear_tick",
                        color="primary",
                        className="m-3",
                    ),
                    dbc.Button(
                        children="✖",
                        id="footwear_cross",
                        color="primary",
                        className="m-3",
                    ),
                ],
                justify="center",
            ),
        ]
    ),
)

user_buttons = (
    dbc.Card(
        [
            dbc.CardBody(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.Button(
                                    children="generate",
                                    id="button_generate",
                                    color="primary",
                                    className="m-3",
                                ),
                                width={"size": "auto"},
                            ),
                            dbc.Col(
                                dbc.Button(
                                    children="save",
                                    id="button_save",
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
        ]
    ),
)

user_details = (
    (
        dbc.Card(
            dbc.CardBody(
                dbc.Row(
                    [
                        html.H4("User Details", className="card-title"),
                        html.P(
                            "this is the stuff the user sees", className="card-text"
                        ),
                    ],
                    justify="center",
                ),
            ),
        ),
    ),
)


# --------------------------------------- LAYOUT ---------------------------------------
app.layout = dbc.Container(
    [
        html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(headwear, width=3,),
                        dbc.Col(topwear, width=3,),
                        dbc.Col(user_details, width=3,),
                    ],
                    justify="centre",
                ),
                dbc.Row(
                    [dbc.Col(bottomwear, width=3,), dbc.Col(footwear, width=3,),],
                    justify="end",
                ),
                dbc.Row(
                    dbc.Col(user_buttons, width=4,), className="m-3", justify="start",
                ),
                html.Div(id="app-2-display-value"),
                dcc.Link("Go to App 1", href="/app1"),
            ]
        )
    ]
)
# ------------------------------------- CALLBACKS --------------------------------------


app.run_server(
    debug=True, host="0.0.0.0", port="8080",
)

