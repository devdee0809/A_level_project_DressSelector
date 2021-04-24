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


headwear_placeholder = process_image(
    Path("images", "Headwear", "PlaceHolder.png"),
)

topwear_placeholder = process_image(
    Path("images", "Topwear", "PlaceHolder.png"),
)

bottomwear_placeholder = process_image(
    Path("images", "Bottomwear", "PlaceHolder.png"),
)

footwear_placeholder = process_image(
    Path("images", "Shoes", "PlaceHolder.png"),
)

# --------------------------------------- NAVBAR ---------------------------------------
# create navbar
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
            # dropdown menu for furture proofing
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
    # Headwear Card
    dbc.Card(
        [
            dbc.CardImg(
                src=headwear_placeholder,
                id="card_img_headwear",
                top=True,
            ),
            dbc.Row(
                [
                    dbc.Button(
                        # randomise button
                        children="🔀",
                        id="button_headwear_randomise",
                        color="primary",
                        className="m-2",
                    ),
                    dbc.Button(
                        # like button
                        children="✓",
                        id="button_headwear_tick",
                        color="primary",
                        disabled=True,
                        className="m-2",
                    ),
                    dbc.Button(
                        # dislike button
                        children="✖",
                        id="button_headwear_cross",
                        color="primary",
                        disabled=True,
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
    # Topwear Card
    dbc.Card(
        [
            dbc.CardImg(
                src=topwear_placeholder,
                id="card_img_topwear",
                top=True,
            ),
            dbc.Row(
                [
                    dbc.Button(
                        # randomise button
                        children="🔀",
                        id="button_topwear_randomise",
                        color="primary",
                        className="m-2",
                    ),
                    dbc.Button(
                        # like button
                        children="✓",
                        id="button_topwear_tick",
                        color="primary",
                        disabled=True,
                        className="m-2",
                    ),
                    dbc.Button(
                        # dislike button
                        children="✖",
                        id="button_topwear_cross",
                        color="primary",
                        disabled=True,
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
    # Bottomwear Card
    dbc.Card(
        [
            dbc.CardImg(
                src=bottomwear_placeholder,
                id="card_img_bottomwear",
                top=True,
            ),
            dbc.Row(
                [
                    dbc.Button(
                        # randomise button
                        children="🔀",
                        id="button_bottomwear_randomise",
                        color="primary",
                        className="m-2",
                    ),
                    dbc.Button(
                        # like button
                        children="✓",
                        id="button_bottomwear_tick",
                        color="primary",
                        disabled=True,
                        className="m-2",
                    ),
                    dbc.Button(
                        # dislike button
                        children="✖",
                        id="button_bottomwear_cross",
                        color="primary",
                        disabled=True,
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
    # Footwear Card
    dbc.Card(
        [
            dbc.CardImg(
                src=footwear_placeholder,
                id="card_img_footwear",
                top=True,
            ),
            dbc.Row(
                [
                    dbc.Button(
                        # randomise button
                        children="🔀",
                        id="button_footwear_randomise",
                        color="primary",
                        className="m-2",
                    ),
                    dbc.Button(
                        # like button
                        children="✓",
                        id="button_footwear_tick",
                        color="primary",
                        disabled=True,
                        className="m-2",
                    ),
                    dbc.Button(
                        # dislike button
                        children="✖",
                        id="button_footwear_cross",
                        color="primary",
                        disabled=True,
                        className="m-2",
                    ),
                ],
                justify="center",
            ),
        ],
        className="card mb-4 border-0",
    ),
)

user_buttons = (
    # create user buttons
    dbc.Card(
        [
            dbc.CardBody(
                [
                    # row 1
                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.Button(
                                    # generate button
                                    children="generate",
                                    id="button_generate",
                                    color="primary",
                                    className="m-2",
                                ),
                                width={"size": "auto"},
                            ),
                            dbc.Col(
                                dbc.Button(
                                    # save button
                                    children="save",
                                    id="button_save",
                                    color="primary",
                                    disabled=True,
                                    className="m-2",
                                ),
                                width={"size": "auto"},
                            ),
                        ],
                        justify="center",
                    ),
                ]
            ),
        ],
        className="card mb-4 border-0",
    ),
)

# --------------------------------------- LAYOUT ---------------------------------------
layout = dbc.Container(
    [
        html.Div(
            [
                # row 1
                dbc.Row(
                    dbc.Col(
                        navbar,
                    ),
                ),
                # row 2
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
                # to store item IDs of current outfit displayed
                dcc.Store(
                    id="store_items_id",
                    storage_type="session",
                    data={
                        "headwear_item_id": None,
                        "topwear_item_id": None,
                        "bottomwear_item_id": None,
                        "footwear_item_id": None,
                    },
                ),
                # row 3
                dbc.Row(
                    dbc.Col(
                        user_buttons,
                        width=4,
                    ),
                    className="m-2",
                    align="center",
                    justify="center",
                ),
                # not good idea, leave in here till solution found
                # dbc.Tooltip(
                #     "New Outfit",
                #     target="button_generate",
                #     placement="bottom",
                # ),
                # dbc.Tooltip(
                #     "New Headwear",
                #     target="button_headwear_randomise",
                #     placement="bottom",
                # ),
                # dbc.Tooltip(
                #     "New Topwear",
                #     target="button_topwear_randomise",
                #     placement="bottom",
                # ),
                # dbc.Tooltip(
                #     "New Bottomwear",
                #     target="button_bottomwear_randomise",
                #     placement="bottom",
                # ),
                # dbc.Tooltip(
                #     "New Footwear",
                #     target="button_footwear_randomise",
                #     placement="bottom",
                # ),
                # dbc.Tooltip(
                #     "I want more of this",
                #     target="button_headwear_tick",
                #     placement="bottom",
                # ),
                # dbc.Tooltip(
                #     "I want more of this",
                #     target="button_topwear_tick",
                #     placement="bottom",
                # ),
                # dbc.Tooltip(
                #     "I want more of this",
                #     target="button_bottomwear_tick",
                #     placement="bottom",
                # ),
                # dbc.Tooltip(
                #     "I want more of this",
                #     target="button_footwear_tick",
                #     placement="bottom",
                # ),
                # dbc.Tooltip(
                #     "Don't show me this again",
                #     target="button_headwear_cross",
                #     placement="bottom",
                # ),
                # dbc.Tooltip(
                #     "Don't show me this again",
                #     target="button_topwear_cross",
                #     placement="bottom",
                # ),
                # dbc.Tooltip(
                #     "Don't show me this again",
                #     target="button_bottomwear_cross",
                #     placement="bottom",
                # ),
                # dbc.Tooltip(
                #     "Don't show me this again",
                #     target="button_footwear_cross",
                #     placement="bottom",
                # ),
            ]
        )
    ]
)


# ------------------------------------- CALLBACKS --------------------------------------
# AppCallback for generating random item when randomise button or generate button is clicked
@app.callback(
    [
        Output("card_img_headwear", "src"),
        Output("card_img_topwear", "src"),
        Output("card_img_bottomwear", "src"),
        Output("card_img_footwear", "src"),
        Output("store_items_id", "data"),
    ],
    [
        Input("button_headwear_randomise", "n_clicks"),
        Input("button_topwear_randomise", "n_clicks"),
        Input("button_bottomwear_randomise", "n_clicks"),
        Input("button_footwear_randomise", "n_clicks"),
        Input("button_generate", "n_clicks"),
    ],
    State("store_items_id", "data"),
)
def randomise(
    # when randomise button of one of four cards is clicked
    button_headwear_randomise_n_clicks,
    button_topwear_randomise_n_clicks,
    button_bottomwear_randomise_n_clicks,
    button_footwear_randomise_n_clicks,
    button_generate_n_clicks,
    store_items_id_data,
):
    if (
        # if any of the four randomise buttons are clicked
        button_headwear_randomise_n_clicks
        or button_topwear_randomise_n_clicks
        or button_bottomwear_randomise_n_clicks
        or button_footwear_randomise_n_clicks
        or button_generate_n_clicks
    ):
        ctx = callback_context
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

        if button_id == "button_headwear_randomise":
            # Headwear card randomise button is clicked
            item = database.select_random_item("Headwear", gender_item[gender])
            # retrieve random headwear item according to user gender
            image_blob = item[5]
            item_id = item[0]

            store_items_id_data["headwear_item_id"] = item_id

            print(store_items_id_data)

            return (
                # headwear image returned
                process_binary_image(image_blob),
                None,
                None,
                None,
                # headwear ID stored
                store_items_id_data,
            )

        elif button_id == "button_topwear_randomise":
            # Topwear card randomise button is clicked
            item = database.select_random_item("Topwear", gender_item[gender])
            # retrieve random topwear item according to user gender
            image_blob = item[5]
            item_id = item[0]

            store_items_id_data["topwear_item_id"] = item_id

            print(store_items_id_data)

            return (
                None,
                # topwear image returned
                process_binary_image(image_blob),
                None,
                None,
                # topwear ID stored
                store_items_id_data,
            )

        elif button_id == "button_bottomwear_randomise":
            # Bottomwear card randomise button is clicked
            item = database.select_random_item("Bottomwear", gender_item[gender])
            # retrieve random bottomwear item according to user gender
            image_blob = item[5]
            item_id = item[0]

            store_items_id_data["bottomwear_item_id"] = item_id

            print(store_items_id_data)

            return (
                # bottomwear image returned
                None,
                None,
                process_binary_image(image_blob),
                None,
                # bottomwear ID stored
                store_items_id_data,
            )

        elif button_id == "button_footwear_randomise":
            # Footwear card randomise button is clicked
            item = database.select_random_item("Shoes", gender_item[gender])
            # retrieve random footwear item according to user gender
            image_blob = item[5]
            item_id = item[0]

            store_items_id_data["footwear_item_id"] = item_id

            print(store_items_id_data)

            return (
                None,
                None,
                None,
                # footwear image returned
                process_binary_image(image_blob),
                # footwear ID stored
                store_items_id_data,
            )

        elif button_id == "button_generate":
            # generate button is clicked
            item_headwear = database.select_random_item("Headwear", gender_item[gender])
            # random headwear item loaded
            item_topwear = database.select_random_item("Topwear", gender_item[gender])
            # random topwear item loaded
            item_bottomwear = database.select_random_item(
                "Bottomwear", gender_item[gender]
            )
            # random bottomwear item loaded
            item_footwear = database.select_random_item("Shoes", gender_item[gender])
            # random footwear item loaded

            store_items_id_data["headwear_item_id"] = item_headwear[0]
            # displayed headwear item ID stored
            store_items_id_data["topwear_item_id"] = item_topwear[0]
            # displayed topwear item ID stored
            store_items_id_data["bottomwear_item_id"] = item_bottomwear[0]
            # displayed bottomwear item ID stored
            store_items_id_data["footwear_item_id"] = item_footwear[0]
            # displayed footwear item ID stored

            print(store_items_id_data)

            return (
                process_binary_image(item_headwear[5]),
                process_binary_image(item_topwear[5]),
                process_binary_image(item_bottomwear[5]),
                process_binary_image(item_footwear[5]),
                # random outfit is displayed
                store_items_id_data,
                # all item IDs updated in the store
            )

    else:
        raise PreventUpdate


# AppCallback to enable Headwear preference buttons
@app.callback(
    [
        Output("button_headwear_tick", "disabled"),
        Output("button_headwear_cross", "disabled"),
    ],
    Input("store_items_id", "data"),
    # Listens for when store is updated
)
def enable_headwear_preferences_buttons(store_items_id_data):

    if store_items_id_data["headwear_item_id"]:
        return False, False
        # if store contains any headwear item id, enable preference buttons
    else:
        raise PreventUpdate


# AppCallback to enable Headwear preference buttons
@app.callback(
    [
        Output("button_topwear_tick", "disabled"),
        Output("button_topwear_cross", "disabled"),
    ],
    Input("store_items_id", "data"),
    # Listens for when store is updated
)
def enable_topwear_preferences_buttons(store_items_id_data):

    if store_items_id_data["topwear_item_id"]:
        return False, False
        # if store contains any topwear item id, enable preference buttons
    else:
        raise PreventUpdate


# AppCallback to enable Headwear preference buttons
@app.callback(
    [
        Output("button_bottomwear_tick", "disabled"),
        Output("button_bottomwear_cross", "disabled"),
    ],
    Input("store_items_id", "data"),
    # Listens for when store is updated
)
def enable_bottomwear_preferences_buttons(store_items_id_data):

    if store_items_id_data["bottomwear_item_id"]:
        return False, False
        # if store contains any bottomwear item id, enable preference buttons
    else:
        raise PreventUpdate


# AppCallback to enable Headwear preference buttons
@app.callback(
    [
        Output("button_footwear_tick", "disabled"),
        Output("button_footwear_cross", "disabled"),
    ],
    Input("store_items_id", "data"),
    # Listens for when store is updated
)
def enable_footwear_preferences_buttons(store_items_id_data):

    if store_items_id_data["footwear_item_id"]:
        return False, False
        # if store contains any bottomwear item id, enable preference buttons
    else:
        raise PreventUpdate


# AppCallback for enabling save button
@app.callback(
    Output("button_save", "disabled"),
    Input("store_items_id", "data"),
    # Listens for when store is updated
)
def enable_save_button(store_items_id_data):

    if (
        store_items_id_data["headwear_item_id"]
        and store_items_id_data["topwear_item_id"]
        and store_items_id_data["bottomwear_item_id"]
        and store_items_id_data["footwear_item_id"]
    ):
        return False
        # if all there item IDs for headwear, topwear, bottomwear and footwear, then enable save button
    else:
        raise PreventUpdate


# AppCallback for headwear preference buttons
@app.callback(
    [
        Output("button_headwear_tick", "color"),
        Output("button_headwear_cross", "color"),
        # changes colour of buttons
        # green for Like
        # red for Dislike
    ],
    [
        Input("button_headwear_randomise", "n_clicks"),
        # this ensures there is an item being displayed
        Input("button_headwear_tick", "n_clicks"),
        Input("button_headwear_cross", "n_clicks"),
    ],
    State("store_items_id", "data"),
)
def save_headwear_preferences(
    button_headwear_randomise_n_clicks,
    button_headwear_tick_n_clicks,
    button_headwear_cross_n_clicks,
    store_items_id_data,
):
    if (
        button_headwear_randomise_n_clicks
        or button_headwear_tick_n_clicks
        or button_headwear_cross_n_clicks
    ):
        ctx = callback_context
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

        # reset preferences whenever randomise is clicked
        if button_id == "button_headwear_randomise":
            return "primary", "primary"

        else:

            headwear_item_id = store_items_id_data["headwear_item_id"]
            # check if a preference already exists
            preference_exists = database.check_preference_exists(
                user_rowid,
                headwear_item_id,
            )

            if button_id == "button_headwear_tick":
                if preference_exists:
                    # update preference if it already exists - Like
                    database.update_preference(
                        True,
                        user_rowid,
                        headwear_item_id,
                    )
                else:
                    # create a preference if it does not exist - Like
                    database.add_preference(
                        user_rowid,
                        headwear_item_id,
                        True,
                    )
                return "success", "primary"

            elif button_id == "button_headwear_cross":
                # update preference if it already exists - Dislike
                if preference_exists:
                    database.update_preference(
                        False,
                        user_rowid,
                        headwear_item_id,
                    )
                else:
                    # create a preference if it does not exist - Dislike
                    database.add_preference(
                        user_rowid,
                        headwear_item_id,
                        False,
                    )
                return "primary", "danger"

    else:
        raise PreventUpdate


# AppCallback for topwear preference buttons
@app.callback(
    [
        Output("button_topwear_tick", "color"),
        Output("button_topwear_cross", "color"),
        # changes colour of buttons
        # green for Like
        # red for Dislike
    ],
    [
        Input("button_topwear_randomise", "n_clicks"),
        # this ensures there is an item being displayed
        Input("button_topwear_tick", "n_clicks"),
        Input("button_topwear_cross", "n_clicks"),
    ],
    State("store_items_id", "data"),
)
def save_topwear_preferences(
    button_topwear_randomise_n_clicks,
    button_topwear_tick_n_clicks,
    button_topwear_cross_n_clicks,
    store_items_id_data,
):
    if (
        button_topwear_randomise_n_clicks
        or button_topwear_tick_n_clicks
        or button_topwear_cross_n_clicks
    ):
        ctx = callback_context
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

        # reset preferences whenever randomise is clicked
        if button_id == "button_headwear_randomise":
            return "primary", "primary"

        else:

            topwear_item_id = store_items_id_data["topwear_item_id"]
            # check if a preference already exists
            preference_exists = database.check_preference_exists(
                user_rowid,
                topwear_item_id,
            )

            if button_id == "button_topwear_tick":
                if preference_exists:
                    # update preference if it already exists - Like
                    database.update_preference(
                        True,
                        user_rowid,
                        topwear_item_id,
                    )
                else:
                    # create a preference if it does not exist - Like
                    database.add_preference(
                        user_rowid,
                        topwear_item_id,
                        True,
                    )
                return "success", "primary"

            elif button_id == "button_topwear_cross":
                if preference_exists:
                    # update preference if it already exists - Dislike
                    database.update_preference(
                        False,
                        user_rowid,
                        topwear_item_id,
                    )
                else:
                    # create a preference if it does not exist - Dislike
                    database.add_preference(
                        user_rowid,
                        topwear_item_id,
                        False,
                    )
                return "primary", "danger"

    else:
        raise PreventUpdate


# AppCallback for bottomwear preference buttons
@app.callback(
    [
        Output("button_bottomwear_tick", "color"),
        Output("button_bottomwear_cross", "color"),
        # changes colour of buttons
        # green for Like
        # red for Dislike
    ],
    [
        Input("button_bottomwear_randomise", "n_clicks"),
        # this ensures there is an item being displayed
        Input("button_bottomwear_tick", "n_clicks"),
        Input("button_bottomwear_cross", "n_clicks"),
    ],
    State("store_items_id", "data"),
)
def save_bottomwear_preferences(
    button_bottomwear_randomise_n_clicks,
    button_bottomwear_tick_n_clicks,
    button_bottomwear_cross_n_clicks,
    store_items_id_data,
):
    if (
        button_bottomwear_randomise_n_clicks
        or button_bottomwear_tick_n_clicks
        or button_bottomwear_cross_n_clicks
    ):
        ctx = callback_context
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

        # reset preferences whenever randomise is clicked
        if button_id == "button_headwear_randomise":
            return "primary", "primary"

        else:

            bottomwear_item_id = store_items_id_data["bottomwear_item_id"]
            # check if a preference already exists
            preference_exists = database.check_preference_exists(
                user_rowid,
                bottomwear_item_id,
            )

            if button_id == "button_bottomwear_tick":
                if preference_exists:
                    # update preference if it already exists - Like
                    database.update_preference(
                        True,
                        user_rowid,
                        bottomwear_item_id,
                    )
                else:
                    # create a preference if it does not exist - Like
                    database.add_preference(
                        user_rowid,
                        bottomwear_item_id,
                        True,
                    )
                return "success", "primary"

            elif button_id == "button_bottomwear_cross":
                if preference_exists:
                    # update preference if it already exists - Dislike
                    database.update_preference(
                        False,
                        user_rowid,
                        bottomwear_item_id,
                    )
                else:
                    # create a preference if it does not exist - Dislike
                    database.add_preference(
                        user_rowid,
                        bottomwear_item_id,
                        False,
                    )
                return "primary", "danger"

    else:
        raise PreventUpdate


# AppCallback for bottomwear preference buttons
@app.callback(
    [
        Output("button_footwear_tick", "color"),
        Output("button_footwear_cross", "color"),
        # changes colour of buttons
        # green for Like
        # red for Dislike
    ],
    [
        Input("button_footwear_randomise", "n_clicks"),
        # this ensures there is an item being displayed
        Input("button_footwear_tick", "n_clicks"),
        Input("button_footwear_cross", "n_clicks"),
    ],
    State("store_items_id", "data"),
)
def save_footwear_preferences(
    button_footwear_randomise_n_clicks,
    button_footwear_tick_n_clicks,
    button_footwear_cross_n_clicks,
    store_items_id_data,
):
    if (
        button_footwear_randomise_n_clicks
        or button_footwear_tick_n_clicks
        or button_footwear_cross_n_clicks
    ):
        ctx = callback_context
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

        # reset preferences whenever randomise is clicked
        if button_id == "button_headwear_randomise":
            return "primary", "primary"

        else:

            footwear_item_id = store_items_id_data["footwear_item_id"]
            # check if a preference already exists
            preference_exists = database.check_preference_exists(
                user_rowid,
                footwear_item_id,
            )

            if button_id == "button_footwear_tick":
                if preference_exists:
                    # update preference if it already exists - Like
                    database.update_preference(
                        True,
                        user_rowid,
                        footwear_item_id,
                    )
                else:
                    # create a preference if it does not exist - Like
                    database.add_preference(
                        user_rowid,
                        footwear_item_id,
                        True,
                    )
                return "success", "primary"

            elif button_id == "button_footwear_cross":
                if preference_exists:
                    # update preference if it already exists - Dislike
                    database.update_preference(
                        False,
                        user_rowid,
                        footwear_item_id,
                    )
                else:
                    # create a preference if it does not exist - Dislike
                    database.add_preference(
                        user_rowid,
                        footwear_item_id,
                        False,
                    )
                return "primary", "danger"

    else:
        raise PreventUpdate


# AppCallback for saving outfits
@app.callback(
    [
        Output("button_save", "color"),
        # changes colour of save button
        # green
        Output("button_save", "children"),
    ],
    [
        Input("button_headwear_randomise", "n_clicks"),
        Input("button_topwear_randomise", "n_clicks"),
        Input("button_bottomwear_randomise", "n_clicks"),
        Input("button_footwear_randomise", "n_clicks"),
        Input("button_generate", "n_clicks"),
        Input("button_save", "n_clicks"),
        # any randomise button should be clicked to create an outfit
    ],
    State("store_items_id", "data"),
)
def save_outfit(
    button_headwear_randomise_n_clicks,
    button_topwear_randomise_n_clicks,
    button_bottomwear_randomise_n_clicks,
    button_footwear_randomise_n_clicks,
    button_generate_n_clicks,
    button_save_n_clicks,
    store_items_id_data,
):

    if (
        button_headwear_randomise_n_clicks
        or button_topwear_randomise_n_clicks
        or button_bottomwear_randomise_n_clicks
        or button_footwear_randomise_n_clicks
        or button_generate_n_clicks
        or button_save_n_clicks
    ):

        ctx = callback_context
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

        if button_id == "button_save":
            # save button is clicked

            headwear_item_id = store_items_id_data["headwear_item_id"]
            topwear_item_id = store_items_id_data["topwear_item_id"]
            bottomwear_item_id = store_items_id_data["bottomwear_item_id"]
            footwear_item_id = store_items_id_data["footwear_item_id"]
            # loading item IDs from store

            # check if an outfit already exists with loaded item IDs
            outfit_exists = database.check_outfit_exists(
                user_rowid,
                headwear_item_id,
                topwear_item_id,
                bottomwear_item_id,
                footwear_item_id,
            )

            if not outfit_exists:
                # save if outfit does not exist
                database.save_outfit(
                    user_rowid,
                    headwear_item_id,
                    topwear_item_id,
                    bottomwear_item_id,
                    footwear_item_id,
                )

            return "success", "saved"

        else:
            return "primary", "save"

    else:
        raise PreventUpdate
