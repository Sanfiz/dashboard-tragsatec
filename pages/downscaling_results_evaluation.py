from dash import html, dcc, register_page, callback, Input, Output
import dash_bootstrap_components as dbc
from components.nav_arrows import nav_arrows

register_page(
    __name__,
    path="/downscaling/results/evaluation",
    name="Downscaling Results — Evaluation"
)

PROXY_PREFIX = "/user/esp9221/proxy/8055/"
BASE = f"{PROXY_PREFIX}assets/imgs_downscaling/evaluation"

SEASON_OPTIONS = [
    {"label": "Winter", "value": "DJF"},
    {"label": "Spring", "value": "MAM"},
    {"label": "Summer", "value": "JJA"},
    {"label": "Autumn", "value": "SON"},
]

layout = dbc.Container([

    html.H4("Seasonal Evaluation - Downscaled Precipitation",
            style={"textAlign": "center", "color": "#003060", "marginBottom": "25px"}),

    html.Label("Season", style={"fontWeight": "bold", "textAlign": "left"}),

    dcc.Dropdown(
        id="eval-season",
        options=SEASON_OPTIONS,
        value="DJF",
        clearable=False,
        style={"width": "40%", "marginBottom": "25px"}
    ),

    html.Img(
        id="eval-image",
        style={
            "maxWidth": "70%",
            "display": "block",
            "margin": "0 auto",
            "borderRadius": "10px",
            "boxShadow": "0 0 12px rgba(0,0,0,0.25)",
            "marginTop": "-50px"
        }
    ),

    nav_arrows(
        prev_href=f"{PROXY_PREFIX}downscaling/results",
        next_href=f"{PROXY_PREFIX}weighting",
        prev_text="Back",
        next_text="Go to Weighting"
    )

], style={"padding": "40px"})


@callback(
    Output("eval-image", "src"),
    Input("eval-season", "value")
)
def update_eval_image(season):
    filename = f"pr_ysacc_{season}_downERA5_1deg_hpc-ecmwf_def.png"
    return f"{BASE}/{filename}"
