import dash
from dash import html, dcc, register_page
import dash_bootstrap_components as dbc
from components.nav_arrows import nav_arrows

# Register page
register_page(
    __name__,
    path="/weighting/why",
    name="Weighting – Why?"
)

# Proxy for JupyterHub
PROXY_PREFIX = "/user/esp9221/proxy/8055/"
IMG_BASE = f"{PROXY_PREFIX}assets/imgs_weighting"


# ==========================
# LAYOUT
# ==========================
layout = dbc.Container(

    [

        # Title
        html.H2(
            "Why Ensemble Weighting?",
            style={
                "textAlign": "center",
                "color": "#003060",
                "marginBottom": "40px"
            }
        ),

        # Intro text
        html.P(
            """
            Seasonal forecasts contain valuable dynamical information, but ensemble members often 
            represent very different large-scale circulation patterns. Traditional ensemble averaging 
            tends to smooth out this variability, reducing the forecast signal precisely where it is 
            most meaningful.
            """,
            style={"fontSize": "1.05rem", "lineHeight": "1.55", "maxWidth": "900px", "margin": "0 auto"}
        ),

        html.Br(),

        html.P(
            """
            Ensemble weighting aims to give more influence to members whose circulation state resembles 
            the expected (or observed) large-scale pattern. By doing so, we avoid:
            """,
            style={"fontSize": "1.05rem", "lineHeight": "1.55", "maxWidth": "900px", "margin": "0 auto"}
        ),

        html.Ul(
            [
                html.Li("Dilution of NAO/EA signals due to opposite-phase members"),
                html.Li("Over-smoothed spatial patterns in temperature or precipitation anomalies"),
                html.Li("Loss of predictive power during highly dynamical seasons (DJF–MAM)"),
            ],
            style={
                "fontSize": "1rem",
                "lineHeight": "1.55",
                "maxWidth": "850px",
                "margin": "0 auto",
                "paddingLeft": "40px",
                "marginTop": "10px"
            }
        ),

        html.Br(),

        html.Br(),

        # Additional explanation text
        html.P(
            """
            The key idea is that forecast skill is strongly linked to the atmospheric circulation, 
            particularly over the Euro-Atlantic sector. Modes such as NAO, EA, SCA, or targeted 
            teleconnections derived through PLS explain a significant fraction of temperature and 
            precipitation variability over Iberia.
            """,
            style={"fontSize": "1.05rem", "lineHeight": "1.55", "maxWidth": "900px", "margin": "0 auto"}
        ),

        html.Br(),

        html.P(
            """
            Weighting ensemble members based on their projected circulation state allows us to 
            retain physically consistent patterns, enhance forecast signals, and improve skill for 
            variables tightly coupled to large-scale dynamics.
            """,
            style={
                "fontSize": "1.05rem",
                "lineHeight": "1.55",
                "maxWidth": "900px",
                "margin": "0 auto",
                "marginBottom": "60px"
            }
        ),

        # Navigation arrows
        nav_arrows(
            prev_href=f"{PROXY_PREFIX}weighting",
            next_href=f"{PROXY_PREFIX}weighting/methodology",
            prev_text="Back to Main Weighting Menu",
            next_text="Go to Methodology"
        ),

    ],

    fluid=True,
    style={"padding": "40px"}
)
