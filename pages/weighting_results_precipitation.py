import dash
from dash import html, dcc, register_page, callback, Input, Output
import dash_bootstrap_components as dbc
from components.nav_arrows import nav_arrows

# Registrar la página
register_page(
    __name__,
    path="/weighting/results/precipitation",
    name="Weighting EOF Results - Precipitation"
)

# Prefijo proxy ECMWF
PROXY_PREFIX = "/user/esp9221/proxy/8055/"
BASE = f"{PROXY_PREFIX}assets/imgs_weighting/precipitation"

# Dropdown options
MODEL_OPTIONS = [
    {"label": "ECMWF", "value": "ECMWF"},
    {"label": "DWD",   "value": "DWD"},
    {"label": "CMCC",  "value": "CMCC"}
]

VAR_OPTIONS = [
    {"label": "Anomalies",  "value": "ANOM"},
    {"label": "Terciles",   "value": "TERCILES"},
    {"label": "Correlation", "value": "CORR"}
]

REGION_OPTIONS = [
    {"label": "Iberia", "value": "Iberia"},
    {"label": "MedCOF", "value": "MedCOF"},
]


# ===========================================
# LAYOUT
# ===========================================
layout = dbc.Container([

    dbc.Row([

        # -----------------------------------
        # LEFT COLUMN — DROPDOWNS
        # -----------------------------------
        dbc.Col([
            html.Label("Model", style={"fontWeight": "bold"}),
            dcc.Dropdown(
                id="wprec-model",
                options=MODEL_OPTIONS,
                value="ECMWF",
                clearable=False,
                style={"marginBottom": "20px", "width": "80%"}
            ),

            html.Label("Variable", style={"fontWeight": "bold"}),
            dcc.Dropdown(
                id="wprec-variable",
                options=VAR_OPTIONS,
                value="ANOM",
                clearable=False,
                style={"marginBottom": "20px", "width": "80%"}
            ),

            html.Label("Region", style={"fontWeight": "bold"}),
            dcc.Dropdown(
                id="wprec-region",
                options=REGION_OPTIONS,
                value="Iberia",
                clearable=False,
                style={"marginBottom": "25px", "width": "80%"}
            ),
            #html.Div("DEBUG REGION DROPDOWN FOUND", id="debug-region", style={"color": "blue"})

        ], md=2),

        # -----------------------------------
        # RIGHT COLUMN — IMAGES
        # -----------------------------------
        dbc.Col([

            dbc.Row(id="wprec-images-row", className="g-3", children=[

                # RAW IMAGE (LEFT)
                dbc.Col(id="wprec-raw-col", children=[
                    html.H5(
                        id="wprec-raw-title",
                        style={"textAlign": "center",
                               "color": "#003060",
                               "marginBottom": "10px"}
                    ),

                    html.Img(
                        id="wprec-raw-img",
                        style={
                            "width": "100%",
                            "display": "block",
                            "margin": "0 auto",
                            "borderRadius": "8px",
                            "boxShadow": "0 0 12px rgba(0,0,0,0.30)"
                        }
                    )
                ], md=6),

                # WEIGHTED IMAGE (RIGHT)
                dbc.Col(id="wprec-wei-col", children=[
                    html.H5(
                        id="wprec-wei-title",
                        children="Tunned Precipitation DJF 2025-2026",
                        style={"textAlign": "center",
                               "color": "#003060",
                               "marginBottom": "10px"}
                    ),

                    html.Img(
                        id="wprec-wei-img",
                        style={
                            "width": "100%",
                            "display": "block",
                            "margin": "0 auto",
                            "borderRadius": "8px",
                            "boxShadow": "0 0 12px rgba(0,0,0,0.30)"
                        }
                    )
                ], md=6),

            ]),

        ], md=9),

    ]),

    # -------- NAV ARROWS --------
    nav_arrows(
        prev_href=f"{PROXY_PREFIX}weighting/results",
        prev_text="Back"
    ),

], style={"padding": "40px"})


# ===========================================
# CALLBACK
# ===========================================
@callback(
    Output("wprec-raw-img", "src"),
    Output("wprec-wei-img", "src"),
    Output("wprec-raw-col", "style"),
    Output("wprec-wei-col", "style"),
    Output("wprec-raw-title", "children"),
    Output("wprec-wei-title", "style"),
    Input("wprec-model", "value"),
    Input("wprec-variable", "value"),
    Input("wprec-region", "value"),
)
def update_precip_images(model, var, region):

    model_lower = model.lower()

    # --------------------------------------------------------
    # CASO TERCILES → Solo 1 figura
    # --------------------------------------------------------
    if var == "TERCILES":

        one_fig = (
            f"{BASE}/terciles_tprate_{model_lower}_lead112025_DJF_{region}.png"
        )

        raw_src = one_fig
        wei_src = None

        raw_style = {"display": "block", "width": "100%"}
        wei_style = {"display": "none"}

        raw_title = "" 
        wei_title_style = {"display": "none"}

        return raw_src, wei_src, raw_style, wei_style, raw_title, wei_title_style

    # --------------------------------------------------------
    # CASOS NORMALES (ANOM / CORR)
    # --------------------------------------------------------
    raw = f"{BASE}/RAW_fore_{model}-DJF_tprate_{region}_{var}.png"
    wei = f"{BASE}/WEI_fore_{model}-DJF_tprate_{region}_{var}.png"

    raw_style = {"display": "block"}
    wei_style = {"display": "block"}

    raw_title = f"Copernicus Precipitation DJF 2025-2026"

    wei_title_style = {
        "textAlign": "center",
        "color": "#003060",
        "marginBottom": "10px"
    }

    return raw, wei, raw_style, wei_style, raw_title, wei_title_style
