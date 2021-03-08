import base64
from pathlib import Path

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from dash_bootstrap_components._components.Col import Col
from dash_bootstrap_components._components.Row import Row

from app import app, database

# ---------------------------------------- DATA ----------------------------------------

# --------------------------------------- IMAGES ---------------------------------------
def process_image(img):
    img_encoded = base64.b64encode(open(img, "rb").read())
    return f"data:image/png;base64,{img_encoded.decode()}"


headwear_placeholder_men = process_image(
    Path("images", "Headwear", "PlaceHolderMen.png"),
)

topwear_placeholder_men = process_image(
    Path("images", "Topwear", "PlaceHolderMen.png"),
)

bottomwear_placeholder_men = process_image(
    Path("images", "Bottomwear", "PlaceHolderMen.png"),
)

shoes_placeholder_men = process_image(
    Path("images", "Shoes", "PlaceHolderMen.png"),
)

# --------------------------------------- CARDS ----------------------------------------
headwear = (
    dbc.Card(
        [
            dbc.CardImg(
                src=headwear_placeholder_men,
                id="card_img_headwear",
                top=True,
            ),
        ]
    ),
)


topwear = (
    dbc.Card(
        [
            dbc.CardImg(
                src=topwear_placeholder_men,
                top=True,
            ),
        ]
    ),
)

bottomwear = (
    dbc.Card(
        [
            dbc.CardImg(
                src=bottomwear_placeholder_men,
                top=True,
            ),
        ]
    ),
)


footwear = (
    dbc.Card(
        [
            dbc.CardImg(
                src=shoes_placeholder_men,
                top=True,
            ),
        ]
    ),
)

delete_button = (
    dbc.Card(
        [
            dbc.CardBody(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.Button(
                                    children="Delete",
                                    id="button_delete",
                                    color="primary",
                                ),
                            ),
                        ],
                    ),
                ]
            ),
        ],
        className="border-0",
    ),
)


download_button = (
    dbc.Card(
        [
            dbc.CardBody(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.Button(
                                    children="Download",
                                    id="button_download",
                                    color="primary",
                                ),
                            ),
                        ],
                    ),
                ]
            ),
        ],
        className="border-0",
    ),
)


left_button = (
    dbc.Card(
        [
            dbc.CardBody(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.Button(
                                    children="⬅",
                                    id="left_button",
                                    color="primary",
                                ),
                            ),
                        ],
                    ),
                ]
            ),
        ],
        className="border-0",
    ),
)
right_button = (
    dbc.Card(
        [
            dbc.CardBody(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.Button(
                                    children="➡",
                                    id="right_button",
                                    color="primary",
                                ),
                            ),
                        ],
                    ),
                ]
            ),
        ],
        className="border-0",
    ),
)
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(
            dbc.NavLink(
                "Dress Selector",
                href="/selector",
                id="dress_selector",
                external_link=True,
            ),
        ),
        dbc.NavItem(
            dbc.NavLink(
                "Saved Outfits",
                href="/wardrobe",
                id="wardrobe",
                external_link=True,
            ),
        ),
        dbc.NavItem(
            dbc.NavLink(
                "Account Details",
                href="/accountdetails",
                id="account_details",
                external_link=True,
            ),
        ),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Options", header=True),
                # dbc.DropdownMenuItem("Saved Outfits", href="#"),
                # dbc.DropdownMenuItem("Account Details", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="Navigation",
    brand_href="#",
    color="primary",
    dark=True,
)

# --------------------------------------- LAYOUT ---------------------------------------
layout = dbc.Container(
    [
        html.Div(
            [
                dbc.Row(
                    dbc.Col(
                        navbar,
                    ),
                ),
                dbc.Row(
                    [
                        dbc.Col(headwear, width=3),
                        dbc.Col(topwear, width=3),
                    ],
                    justify="center",
                    className="mt-3",
                ),
                dbc.Row(
                    [
                        dbc.Col(bottomwear, width=3),
                        dbc.Col(footwear, width=3),
                    ],
                    justify="center",
                    className="mt-3",
                ),
                dbc.Row(
                    dbc.Col(
                        dbc.Row(
                            [
                                dbc.Col(
                                    dbc.Row(
                                        dbc.Col(
                                            left_button,
                                            width={"size": "10%"},
                                        ),
                                        justify="start",
                                        no_gutters=True,
                                    ),
                                ),
                                dbc.Col(
                                    dbc.Row(
                                        dbc.Col(
                                            delete_button,
                                            width={"size": "10%"},
                                        ),
                                        justify="end",
                                        no_gutters=True,
                                    ),
                                ),
                                dbc.Col(
                                    dbc.Row(
                                        dbc.Col(
                                            download_button,
                                            width={"size": "10%"},
                                        ),
                                        justify="start",
                                        no_gutters=True,
                                    ),
                                ),
                                dbc.Col(
                                    dbc.Row(
                                        dbc.Col(
                                            right_button,
                                            width={"size": "10%"},
                                        ),
                                        justify="end",
                                        no_gutters=True,
                                    ),
                                ),
                            ],
                            no_gutters=True,
                            justify="center",
                        ),
                        width={"size": 6, "offset": 3},
                    ),
                ),
            ],
        )
    ]
)

# ------------------------------------- CALLBACKS --------------------------------------
