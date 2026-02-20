import dash
from dash import html, dcc, register_page
import dash_bootstrap_components as dbc
from components.nav_arrows import nav_arrows

# Proxy for JupyterHub
PROXY_PREFIX = "/user/esp9221/proxy/8055/"
IMG_BASE = f"{PROXY_PREFIX}assets/imgs_weighting/pls"

# Register page
register_page(
    __name__,
    path="/weighting/results/pls",
    name="Weighting Results - PLS",
    title="Weighting PLS"
)

# ============================
# LAYOUT
# ============================
layout = dbc.Container([

    html.H2(
        "PLS-Based Weighting Results",
        style={
            "textAlign": "center",
            "color": "#003060",
            "marginBottom": "30px"
        }
    ),

    html.P(
        """
        These results illustrate the impact of applying ensemble weighting based on targeted 
        teleconnections derived via Partial Least Squares (PLS) regression. This method is designed 
        to improve warm-season skill by constructing variability modes optimised for Iberian 
        temperature or precipitation predictability.
        """,
        style={
            "maxWidth": "850px",
            "textAlign": "center",
            "margin": "0 auto 40px auto",
            "fontSize": "0.95rem",
            "lineHeight": "1.5"
        }
    ),

    # -------------------------------------------------
    # RESULTS PLACEHOLDER CARDS
    # -------------------------------------------------
    dbc.Row([
        
        # PRECIPITATION (PR)
        dbc.Col(
            html.Div([
                html.H5("Precipitation (PR)",
                        style={"textAlign": "center", "color": "#003060"}),

                html.Div(
                    "PLS-weighted vs RAW results will be displayed here.",
                    style={
                        "padding": "40px",
                        "backgroundColor": "rgba(0,0,0,0.05)",
                        "borderRadius": "10px",
                        "textAlign": "center",
                        "fontStyle": "italic",
                        "color": "#555"
                    }
                )
            ]),
            md=6,
            className="mb-4"
        ),

    ], className="justify-content-center"),

    # -------------------------
    # NAVIGATION ARROWS
    # -------------------------
    nav_arrows(
        prev_href=f"{PROXY_PREFIX}weighting/results",
        prev_text="Back to Weighting Results"
    )

], fluid=True, style={"padding": "40px"})
