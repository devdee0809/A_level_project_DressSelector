# dcc.Link('Navigate to "/page-2"', href='/page-2')
# @app.callback(
#     Output("url", "pathname"),
#     [
#         Input("button_login", "n_clicks"),
#         Input("button_signup", "n_clicks"),
#         Input("button_back_signup", "n_clicks"),
#         Input("button_create_signup", "n_clicks"),
#         Input("alert_login", "color"),
#         Input("alert_signup", "color"),
#     ],
# )
# def change_pathname(
#     button_login_n_clicks,
#     button_signup_n_clicks,
#     button_back_signup_n_clicks,
#     button_create_signup_n_clicks,
#     alert_login_color,
#     alert_signup_color,
# ):
#     ctx = callback_context

#     if not ctx.triggered:
#         raise PreventUpdate

#     else:
#         button_id = ctx.triggered[0]["prop_id"].split(".")[0]

#         if button_id == "button_login" and alert_login_color == "success":
#             time.sleep(1)
#             return "/selector"

#         elif button_id == "button_signup":
#             time.sleep(1)
#             return "/signup"

#         elif button_id == "button_back_signup":
#             time.sleep(0.5)
#             return "/login"

#         elif button_id == "button_create_signup" and alert_signup_color == "success":
#             time.sleep(1)
#             return "/login"

#         else:
#             raise PreventUpdate

# @app.callback(
#     Output("collapse", "is_open"),
#     [Input("button_signup", "n_clicks")],
#     [State("collapse", "is_open")],
# )
# def collapse_signup(button_signup_n_clicks, collapse_is_open):
#     if button_signup_n_clicks:
#         return not collapse_is_open
#     return collapse_is_open
