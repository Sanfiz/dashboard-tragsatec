import dash
from dash import html, dcc, register_page, callback, Input, Output
import dash_bootstrap_components as dbc
from components.nav_arrows import nav_arrows

# Registrar página
register_page(
    __name__,
    path="/weighting/results/temperature",
    name="Weighting Results - Temperature"
)


BASE = f"/assets/imgs_weighting/temperature"


# ------------------------------
# Dropdown options
# ------------------------------
MODEL_OPTIONS = [
    {"label": "ECMWF", "value": "ECMWF"},
    {"label": "DWD",   "value": "DWD"},
    {"label": "CMCC",  "value": "CMCC"},
]

VAR_OPTIONS = [
    {"label": "Anomalies",  "value": "ANOM"},
    {"label": "Terciles",   "value": "TERCILES"},
    {"label": "Correlation", "value": "CORR"},
]


# =============================
# LAYOUT
# =============================
layout = dbc.Container([

    html.H6("Weighted Temperature Winter 2025-2026",
        style={
            "textAlign": "center",
            "color": "#003060",
            "marginBottom": "30px"
        }),

    dbc.Row([

        # -----------------------------------
        # LEFT COLUMN — DROPDOWNS
        # -----------------------------------
        dbc.Col([
            html.Label("Model", style={"fontWeight": "bold"}),
            dcc.Dropdown(
                id="wtemp-model",
                options=MODEL_OPTIONS,
                value="ECMWF",
                clearable=False,
                style={"marginBottom": "25px"}
            ),

            html.Label("Variable", style={"fontWeight": "bold"}),
            dcc.Dropdown(
                id="wtemp-variable",
                options=VAR_OPTIONS,
                value="ANOM",
                clearable=False,
                style={"marginBottom": "25px"}
            ),
        ], md=3),

        # -----------------------------------
        # RIGHT COLUMN — RAW & WEI SIDE-BY-SIDE
        # -----------------------------------
        dbc.Col([

            dbc.Row(id="wtemp-images-row", className="g-3", children=[

                # RAW IMAGE (LEFT)
                dbc.Col(id="wtemp-raw-col", children=[
                    html.H5(
                        id="wtemp-raw-title",
                        children="RAW Forecast",
                        style={
                            "textAlign": "center",
                            "color": "#003060",
                            "marginBottom": "10px"
                        }
                    ),

                    html.Img(
                        id="wtemp-raw-img",
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
                dbc.Col(id="wtemp-wei-col", children=[
                    html.H5(
                        id="wtemp-wei-title",
                        children="Weighted Forecast",
                        style={
                            "textAlign": "center",
                            "color": "#003060",
                            "marginBottom": "10px"
                        }
                    ),

                    html.Img(
                        id="wtemp-wei-img",
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
        prev_href=f"/weighting/results",
        prev_text="Back"
    ),
    

], style={"padding": "40px"})


# =============================
# CALLBACK
# =============================
@callback(
    Output("wtemp-raw-img", "src"),
    Output("wtemp-wei-img", "src"),
    Output("wtemp-raw-col", "style"),
    Output("wtemp-wei-col", "style"),
    Output("wtemp-raw-title", "children"),
    Output("wtemp-wei-title", "style"),
    Input("wtemp-model", "value"),
    Input("wtemp-variable", "value")
)
def update_temperature_images(model, var):

    # --------------------------------------------------------
    # CASO TERCILES → SOLO UNA FIGURA
    # --------------------------------------------------------
    if var == "TERCILES":
        model_lower = model.lower()
        one_fig = f"{BASE}/terciles_t2m_{model_lower}_lead112025_DJF.png"

        # RAW contendrá la única figura
        raw_src = one_fig

        # Se oculta WEIGHTED
        wei_src = None

        # RAW ocupa todo el ancho
        raw_style = {"display": "block", "width": "100%"}

        # Ocultar columna derecha entera
        wei_style = {"display": "none"}

        # Sin títulos
        raw_title = ""  # evita "RAW Forecast"
        wei_title_style = {"display": "none"}

        return raw_src, wei_src, raw_style, wei_style, raw_title, wei_title_style



    # --------------------------------------------------------
    # CASO NORMAL (ANOM / CORR)
    # --------------------------------------------------------
    raw = f"{BASE}/RAW_fore_{model}-DJF_t2m_Iberia_{var}.png"
    wei = f"{BASE}/WEI_fore_{model}-DJF_t2m_Iberia_{var}.png"

    raw_style = {"display": "block"}
    wei_style = {"display": "block"}

    raw_title = "RAW Forecast"
    wei_title_style = {
        "textAlign": "center",
        "color": "#003060",
        "marginBottom": "10px"
    }

    return raw, wei, raw_style, wei_style, raw_title, wei_title_style
