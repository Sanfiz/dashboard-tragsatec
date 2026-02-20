from dash import html, register_page
from components.nav_arrows import nav_arrows

PROXY_PREFIX = "/user/esp9221/proxy/8055/"

register_page(__name__, path="/downscaling/methodology", name="Downscaling Methodology")

layout = html.Div([

    html.H2(
        "Downscaling — Methodology",
        style={"textAlign": "center", "color": "#003060"}
    ),

    html.P(
        "Pedir Contenido Marta",
        style={"maxWidth": "900px", "margin": "20px auto"}
    ),

    nav_arrows(
        prev_href=f"{PROXY_PREFIX}downscaling",
        next_href=f"{PROXY_PREFIX}downscaling/results",
        prev_text="Back to Downscaling Main",
        next_text="Go to Downscaling Results"
    )

], style={"padding": "40px"})
