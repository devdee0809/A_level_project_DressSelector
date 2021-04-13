from pathlib import Path

import dash
import dash_bootstrap_components as dbc

from database.query import DataBase

# create an object of the database before creating the main app
database = DataBase(
    Path(
        "database",
        "database.db",
    )
)

# create the main app
app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.FLATLY],
)

server = app.server
