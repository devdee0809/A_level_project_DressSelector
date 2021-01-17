
# @app.callback(
#     Output("collapse", "is_open"),
#     [Input("button_signup", "n_clicks")],
#     [State("collapse", "is_open")],
# )
# def collapse_signup(button_signup_n_clicks, collapse_is_open):
#     if button_signup_n_clicks:
#         return not collapse_is_open
#     return collapse_is_open
