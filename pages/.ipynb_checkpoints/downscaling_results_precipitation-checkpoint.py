from dash import html, register_page, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
from components.nav_arrows import nav_arrows

register_page(
    __name__,
    path="/downscaling/results/precipitation",
    name="Downscaling Results — Precipitation"
)

PROXY_PREFIX = "/user/esp9221/proxy/8055/"
BASE = f"{PROXY_PREFIX}assets/imgs_downscaling/precipitation"


# ---- OPCIONES DE MODELOS ----
MODEL_OPTIONS = [
    {"label": "ECMWF", "value": "ecmwf"},
    # {"label": "CMCC", "value": "cmcc"},  
    # {"label": "DWD", "value": "dwd"},
]

# ---- OPCIONES DE FIGURAS ----
FIG_OPTIONS = [
    {"label": "2 Subplots", "value": "2subplot"},
    {"label": "4 Subplots", "value": "4subplot"},
]

layout = html.Div([
    
    html.H2("Downscaling Results for Precipitation",
        style={"textAlign": "center", "color": "#003060", "marginBottom": "30px"}),

    dbc.Container([

        dbc.Row([dbc.Col([
        
        # SELECT MODEL 
        html.Label("Model",style={"fontWeight": "bold","textAlign": "center","display": "block","width": "100%","marginBottom": "5px"}),
        dcc.Dropdown(id="precip-model",options=MODEL_OPTIONS,value="ecmwf",clearable=False,
                        style={"width": "80%","fontSize": "0.85rem","margin": "0 auto 20px auto"}
                    ),

        # SELECT FIGURE
        html.Label("Figure",style={"fontWeight": "bold","textAlign": "center","display": "block","width": "100%","marginBottom": "5px"}),
        dcc.Dropdown(id="precip-figure",options=FIG_OPTIONS,value="2subplot",clearable=False,
            style={"width": "80%", "fontSize": "0.85rem","margin": "0 auto 20px auto"}

               ),
                    ],
                    md=3,  
                    className="d-flex flex-column justify-content-start align-items-start"
                ),

    dbc.Col(         
        # FIGURAS
        html.Div(
            html.Img(id="precip-image",src="",
                style={"maxWidth": "90%","display": "block","margin": "0 auto","borderRadius": "10px","boxShadow": "0 0 12px rgba(0,0,0,0.2)"}
                        ),
                        className="d-flex justify-content-center"
                    ),
                    md=9
                ),

            ],
            className="align-items-start"
        ),

        # -------- NAV ARROWS --------
        nav_arrows(
            prev_href=f"{PROXY_PREFIX}downscaling/results",
            next_href=f"{PROXY_PREFIX}downscaling/results/terciles",
            prev_text="Back",
            next_text="Next: Terciles"
        ),

        

    ], fluid=False, style={"maxWidth": "1200px"})

], style={"padding": "40px"})


# ---- CALLBACK ----
@callback(
    Output("precip-image", "src"),
    Input("precip-model", "value"),
    Input("precip-figure", "value")
)
def update_precip_image(model, fig_type):

    # NOMBRE EXACTO DEL ARCHIVO (tal como lo tienes)
    filename = f"Precip_ecmwf-s51_2025-NDJFM_pr_5m_{fig_type}.png"

    # RUTA FINAL COMPLETA
    return f"{BASE}/{model}/{filename}"
