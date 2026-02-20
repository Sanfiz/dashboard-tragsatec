from dash import html, register_page, dcc
import dash_bootstrap_components as dbc
from components.nav_arrows import nav_arrows

register_page(__name__, path="/downscaling/results", name="Downscaling Results")

PROXY_PREFIX = "/user/esp9221/proxy/8055/"
IMG_BASE = f"{PROXY_PREFIX}assets/imgs_downscaling"

# --- ESTILO MEJORADO PARA MINI-CARDS ---
MINI_CARD = {
    "padding": "18px",
    "borderRadius": "16px",
    "backgroundColor": "white",
    "textAlign": "center",
    "boxShadow": "0 2px 10px rgba(0,0,0,0.10)",
    "cursor": "pointer",
    "transition": "0.3s",
    "width": "85%",
    "margin": "0 auto"
}

def small_card(img, link):
    return dbc.Col(
        dcc.Link(
            html.Div([
                html.Img(
                    src=img,
                    style={
                        "maxWidth": "60%",
                        "borderRadius": "10px",
                        "marginBottom": "10px",
                        "boxShadow": "0 0 10px rgba(0,0,0,0.12)"
                    }
                )
            ], style=MINI_CARD),
            href=link,
            className="text-decoration-none"
        ),
        md=3,
        className="d-flex justify-content-center"
    )


layout = dbc.Container([

        html.Div(
            [
                html.P(
                    "Downscaling results are organised into three products: "
                    "Precipitation, Precipitation Terciles, and Precipitation Scores.",
                    style={"marginBottom": "9px"}
                ),
                html.Br(),
                html.Br(),
                html.P(
                    "Select a category to explore the corresponding maps and analysis."
                )
            ],
            style={
                "textAlign": "center",
                "fontSize": "1rem",
                "maxWidth": "700px",
                "margin": "0 auto 30px auto",
                "color": "#003060"
            }
        ),


    # MINI-CARDS
    dbc.Row(
        [
            small_card(
                f"{IMG_BASE}/precipitation/precipitation.png",
                f"{PROXY_PREFIX}downscaling/results/precipitation"
            ),
            small_card(
                f"{IMG_BASE}/terciles/tercile.png",
                f"{PROXY_PREFIX}downscaling/results/terciles"
            ),
            small_card(
                f"{IMG_BASE}/scores/scores.png",
                f"{PROXY_PREFIX}downscaling/results/scores"
            ),
        ],
        className="g-4 justify-content-center"
    ),

    # NAVEGACIÓN
    nav_arrows(
        prev_href=f"{PROXY_PREFIX}downscaling/methodology",
        next_href=f"{PROXY_PREFIX}weighting",
        prev_text="Back to Downscaling Methodology",
        next_text="Go to Weighting Menu"
    )

], fluid=True)
