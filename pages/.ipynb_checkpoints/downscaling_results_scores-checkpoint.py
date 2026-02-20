from dash import html, register_page
from components.nav_arrows import nav_arrows

register_page(
    __name__,
    path="/downscaling/results/scores",
    name="Downscaling Results - Scores"
)

PROXY_PREFIX = "/user/esp9221/proxy/8055/"

layout = html.Div([

    html.H2(
        "Downscaling Results — Scores",
        style={"textAlign": "center", "color": "#003060"}
    ),

    # -------- NAV ARROWS --------
    nav_arrows(
        prev_href=f"{PROXY_PREFIX}downscaling",
        prev_text="Back to Downscaling Menu"
    ),

], style={"padding": "40px"})
