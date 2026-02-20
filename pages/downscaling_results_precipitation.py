from dash import html, register_page, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
from components.nav_arrows import nav_arrows

# ---------------------------------------
# REGISTER PAGE
# ---------------------------------------
register_page(
    __name__,
    path="/downscaling/results/precipitation",
    name="Downscaling Results — Precipitation"
)

PROXY_PREFIX = "/user/esp9221/proxy/8055/"

# Carpetas de las figuras
BASE_MAIN = f"{PROXY_PREFIX}assets/imgs_downscaling/precipitation"

# ---- MODELOS ----
MODEL_OPTIONS = [
    {"label": "ECMWF", "value": "ecmwf"},
]

# ---- FIGURAS 2/4 SUBPLOTS ----
FIG_OPTIONS = [
    {"label": "2 Subplots", "value": "2subplot"},
    {"label": "4 Subplots", "value": "4subplot"},
]


# ============================
# LAYOUT
# ============================
layout = html.Div([

    html.H6("Downscaled Precipitation Extended Winter 2025-2026",
            style={"textAlign": "center",
                   "color": "#003060",
                   "marginBottom": "30px"}),

    dbc.Container([

        dbc.Row([

            # -----------------------------------
            # COL 1 — DROPDOWNS
            # -----------------------------------
            dbc.Col([
                html.Label("Model",
                           style={"fontWeight": "bold",
                                  "textAlign": "center",
                                  "display": "block",
                                  "marginBottom": "5px"}),

                dcc.Dropdown(
                    id="precip-model",
                    options=MODEL_OPTIONS,
                    value="ecmwf",
                    clearable=False,
                    style={
                        "width": "80%",
                        "margin": "0 auto 20px auto",
                        "borderRadius": "8px"
                    }
                ),

                html.Label("Figure Type",
                           style={"fontWeight": "bold",
                                  "textAlign": "center",
                                  "display": "block",
                                  "marginBottom": "5px"}),

                dcc.Dropdown(
                    id="precip-figure",
                    options=FIG_OPTIONS,
                    value="2subplot",
                    clearable=False,
                    style={
                        "width": "80%",
                        "margin": "0 auto 20px auto",
                        "borderRadius": "8px"
                    }
                ),
            ], md=3),

            # -----------------------------------
            # COL 2 — IMAGE
            # -----------------------------------
            dbc.Col(
                html.Div(
                    html.Img(
                        id="precip-image",
                        style={
                            "maxWidth": "100%",
                            "display": "block",
                            "margin": "0 auto",
                            "borderRadius": "10px",
                            "boxShadow": "0 0 12px rgba(0,0,0,0.2)"
                        }
                    ),
                ),
                md=9,
                className="d-flex align-items-start"
            ),

        ], className="align-items-start"),


        # ---------- NAV ARROWS ----------
        nav_arrows(
            prev_href=f"{PROXY_PREFIX}downscaling/results",
            next_href=f"{PROXY_PREFIX}downscaling/results/terciles",
            prev_text="Back",
            next_text="Next: Terciles"
        ),

    ], fluid=False, style={"maxWidth": "1200px"})

], style={"padding": "40px"})


# ============================
# CALLBACK SUPERIOR
# ============================
@callback(
    Output("precip-image", "src"),
    Input("precip-model", "value"),
    Input("precip-figure", "value")
)
def update_precip_image(model, fig_type):

    filename = f"Precip_ecmwf-s51_2025-NDJFM_pr_5m_{fig_type}.png"
    return f"{BASE_MAIN}/{model}/{filename}"
