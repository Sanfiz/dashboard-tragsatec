import dash
from dash import html, register_page, dcc
import dash_bootstrap_components as dbc
from components.nav_arrows import nav_arrows   

register_page(__name__, path="/downscaling", name="● Downscaling ●")

PROXY_PREFIX = "/user/esp9221/proxy/8055/"
IMG_BASE = f"{PROXY_PREFIX}assets/imgs_downscaling"

layout = dbc.Container([

    dbc.Row([

        # ----------------------
        # METHODOLOGY BUTTON
        # ----------------------
        dbc.Col(
            dcc.Link(
                html.Img(
                    src=f"{IMG_BASE}/methodology.png",
                    style={
                        "maxWidth": "60%",    
                        "cursor": "pointer",
                        "borderRadius": "99px",
                        "boxShadow": "0 4px 14px rgba(0,0,0,0.2)",
                        "display": "block",
                        "margin": "0 auto"
                    }
                ),
                href=f"{PROXY_PREFIX}downscaling/methodology",
                className="text-decoration-none"
            ),
            md=4,
            className="d-flex justify-content-center"
        ),

        # ----------------------
        # RESULTS BUTTON
        # ----------------------
        dbc.Col(
            dcc.Link(
                html.Img(
                    src=f"{IMG_BASE}/results.png",
                    style={
                        "maxWidth": "60%",
                        "cursor": "pointer",
                        "borderRadius": "99px",
                        "boxShadow": "0 0 12px rgba(0,0,0,0.15)",
                        "display": "block",
                        "margin": "0 auto"
                    }
                ),
                href=f"{PROXY_PREFIX}downscaling/results",
                className="text-decoration-none"
            ),
            md=4,
            className="d-flex justify-content-center"
        ),

    ], className="justify-content-center align-items-center my-4"),


    # ----------------------
    # NAVIGATION ARROWS
    # ----------------------
    nav_arrows(
        prev_href=f"{PROXY_PREFIX}",          # <- Home
        next_href=f"{PROXY_PREFIX}weighting", # ->  Weighting
        prev_text="Back to Home",
        next_text="Go to Weighting"
    )

], fluid=True)
