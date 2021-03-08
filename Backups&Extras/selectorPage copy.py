import base64
from pathlib import Path

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash import callback_context
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from app import app, database

# ---------------------------------------- DATA ----------------------------------------
user_rowid, first_name, last_name, gender, email, password = database.get_user_details()
gender_item = {"Female": "Women", "Male": "Men"}
print(user_rowid, first_name, last_name, gender, email, password)


# --------------------------------------- IMAGES ---------------------------------------
def process_image(img):
    img_encoded = base64.b64encode(open(img, "rb").read())
    return f"data:image/png;base64,{img_encoded.decode()}"


def process_binary_image(img):
    img_encoded = base64.b64encode(img)
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

# --------------------------------------- NAVBAR ---------------------------------------
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
            children=[dbc.DropdownMenuItem("Options", header=True)],
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

# --------------------------------------- CARDS ----------------------------------------
headwear = (
    dbc.Card(
        [
            dbc.CardImg(
                src=headwear_placeholder_men,
                id="card_img_headwear",
                top=True,
            ),
            dbc.Row(
                [
                    dbc.Button(
                        children="🔀",
                        id="button_headwear_randomise",
                        color="primary",
                        className="m-2",
                    ),
                    dbc.Button(
                        children="✓",
                        id="button_headwear_tick",
                        color="primary",
                        className="m-2",
                    ),
                    dbc.Button(
                        children="✖",
                        id="button_headwear_cross",
                        color="primary",
                        className="m-2",
                    ),
                ],
                justify="center",
            ),
        ],
        className="card mb-4 border-0",
    ),
)


topwear = (
    dbc.Card(
        [
            dbc.CardImg(
                src=topwear_placeholder_men,
                id="card_img_topwear",
                top=True,
            ),
            dbc.Row(
                [
                    dbc.Button(
                        children="🔀",
                        id="button_topwear_randomise",
                        color="primary",
                        className="m-2",
                    ),
                    dbc.Button(
                        children="✓",
                        id="button_topwear_tick",
                        color="primary",
                        className="m-2",
                    ),
                    dbc.Button(
                        children="✖",
                        id="button_topwear_cross",
                        color="primary",
                        className="m-2",
                    ),
                ],
                justify="center",
            ),
        ],
        className="card mb-4 border-0",
    ),
)

bottomwear = (
    dbc.Card(
        [
            dbc.CardImg(
                src=bottomwear_placeholder_men,
                id="card_img_bottomwear",
                top=True,
            ),
            dbc.Row(
                [
                    dbc.Button(
                        children="🔀",
                        id="button_bottomwear_randomise",
                        color="primary",
                        className="m-2",
                    ),
                    dbc.Button(
                        children="✓",
                        id="button_bottomwear_tick",
                        color="primary",
                        className="m-2",
                    ),
                    dbc.Button(
                        children="✖",
                        id="button_bottomwear_cross",
                        color="primary",
                        className="m-2",
                    ),
                ],
                justify="center",
            ),
        ],
        className="card mb-4 border-0",
    ),
)


footwear = (
    dbc.Card(
        [
            dbc.CardImg(
                src=shoes_placeholder_men,
                id="card_img_footwear",
                top=True,
            ),
            dbc.Row(
                [
                    dbc.Button(
                        children="🔀",
                        id="button_footwear_randomise",
                        color="primary",
                        className="m-2",
                    ),
                    dbc.Button(
                        children="✓",
                        id="button_footwear_tick",
                        color="primary",
                        className="m-2",
                    ),
                    dbc.Button(
                        children="✖",
                        id="button_footwear_cross",
                        color="primary",
                        className="m-2",
                    ),
                ],
                justify="center",
            ),
        ],
        className="card mb-4 border-0",
    ),
)

button_generate = dbc.Button(
    "Generate",
    id="button_generate",
    color="primary",
)

button_save = dbc.Button(
    "Save",
    id="button_save",
    color="primary",
)


# user_buttons = (
#     dbc.Card(
#         [
#             dbc.CardBody(
#                 [
#                     dbc.Row(
#                         [
#                             dbc.Col(
#                                 dbc.Button(
#                                     children="generate",
#                                     id="button_generate",
#                                     color="primary",
#                                     className="m-2",
#                                 ),
#                                 width={"size": "auto"},
#                             ),
#                             dbc.Col(
#                                 dbc.Button(
#                                     children="save",
#                                     id="button_save",
#                                     color="primary",
#                                     className="m-2",
#                                 ),
#                                 width={"size": "auto"},
#                             ),
#                         ],
#                         justify="center",
#                     ),
#                 ]
#             ),
#         ],
#         className="card mb-4 border-0",
#     ),
# )

# --------------------------------------- LAYOUT ---------------------------------------
app.layout = dbc.Container(
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
                        dbc.Col(
                            headwear,
                        ),
                        dbc.Col(
                            topwear,
                        ),
                        dbc.Col(
                            bottomwear,
                        ),
                        dbc.Col(
                            footwear,
                        ),
                    ],
                    className="mt-4",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            button_generate,
                            width={
                                "size": 3,
                                "offset": 2,
                            },
                        ),
                        dbc.Col(
                            button_save,
                            width={
                                "size": 3,
                            },
                        ),
                    ],
                    justify="center",
                    no_gutters=True,
                ),
            ]
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True, port=8868)


# ------------------------------------- CALLBACKS --------------------------------------
# @app.callback(
#     Output("card_img_headwear", "src"),
#     [
#         Input("button_headwear_randomise", "n_clicks"),
#         Input("button_generate", "n_clicks"),
#     ],
# )
# def randomise_headwear(
#     button_headwear_randomise_n_clicks,
#     button_generate_n_clicks,
# ):
#     if button_headwear_randomise_n_clicks or button_generate_n_clicks:
#         item = database.select_random_item("Headwear", gender_item[gender])
#         image_blob = item[5]
#         return process_binary_image(image_blob)
#     else:
#         raise PreventUpdate


# @app.callback(
#     Output("card_img_topwear", "src"),
#     [
#         Input("button_topwear_randomise", "n_clicks"),
#         Input("button_generate", "n_clicks"),
#     ],
# )
# def randomise_topwear(
#     button_topwear_randomise_n_clicks,
#     button_generate_n_clicks,
# ):
#     if button_topwear_randomise_n_clicks or button_generate_n_clicks:
#         item = database.select_random_item("Topwear", gender_item[gender])
#         image_blob = item[5]
#         return process_binary_image(image_blob)
#     else:
#         raise PreventUpdate


# # @app.callback(
# #     Output("card_img_bottomwear", "src"),
# #     [
# #         Input("button_bottomwear_randomise", "n_clicks"),
# #         Input("button_generate", "n_clicks"),
# #     ],
# # )
# # def randomise_bottomwear(
# #     button_bottomwear_randomise_n_clicks,
# #     button_generate_n_clicks,
# # ):
# #     if button_bottomwear_randomise_n_clicks or button_generate_n_clicks:
# #         ctx = callback_context
# #         button_id = ctx.triggered[0]["prop_id"].split(".")[0]

# #         if button_id == "button_bottomwear_randomise" or button_id == "button_generate":
# #             item = database.select_random_item("Bottomwear", gender_item[gender])
# #             image_blob = item[5]
# #             return process_binary_image(image_blob)

# #         else:
# #             raise PreventUpdate

# #     else:
# #         raise PreventUpdate


# # @app.callback(
# #     Output("card_img_footwear", "src"),
# #     [
# #         Input("button_footwear_randomise", "n_clicks"),
# #         Input("button_generate", "n_clicks"),
# #     ],
# # )
# # def randomise_shoes(
# #     button_footwear_randomise_n_clicks,
# #     button_generate_n_clicks,
# # ):
# #     if button_footwear_randomise_n_clicks or button_generate_n_clicks:
# #         ctx = callback_context
# #         button_id = ctx.triggered[0]["prop_id"].split(".")[0]

# #         if button_id == "button_footwear_randomise" or button_id == "button_generate":
# #             item = database.select_random_item("Shoes", gender_item[gender])
# #             image_blob = item[5]
# #             return process_binary_image(image_blob)

# #         else:
# #             raise PreventUpdate

# #     else:
# #         raise PreventUpdate
