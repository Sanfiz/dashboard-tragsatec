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
    {"label": "CMCC",  "value": "CMCC"},
]

VAR_OPTIONS = [
    {"label": "Anomalies",  "value": "ANOM"},
    {"label": "Terciles",   "value": "TERCILES"},
    {"label": "Correlation", "value": "CORR"},
]


# ===========================================
# LAYOUT
# ===========================================
layout = dbc.Container([

    html.H2("EOF Weighted vs Raw - Precipitation",
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
                id="wprec-model",
                options=MODEL_OPTIONS,
                value="ECMWF",
                clearable=False,
                style={"marginBottom": "25px"}
            ),

            html.Label("Variable", style={"fontWeight": "bold"}),
            dcc.Dropdown(
                id="wprec-variable",
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

            dbc.Row([

                # RAW IMAGE (LEFT)
                dbc.Col([
                    html.H5("RAW Forecast",
                        style={
                            "textAlign": "center",
                            "color": "#003060",
                            "marginBottom": "10px"
                        }
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
                dbc.Col([
                    html.H5("Weighted Forecast",
                        style={
                            "textAlign": "center",
                            "color": "#003060",
                            "marginBottom": "10px"
                        }
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

            ], className="g-3"),  # spacing between columns

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
    Input("wprec-model", "value"),
    Input("wprec-variable", "value")
)
def update_precip_images(model, var):

    # RAW image filename
    raw = f"{BASE}/RAW_fore_{model}-DJF_tprate_Iberia_{var}.png"

    # WEIGHTED image filename
    wei = f"{BASE}/WEI_fore_{model}-DJF_tprate_Iberia_{var}.png"

    return raw, wei
