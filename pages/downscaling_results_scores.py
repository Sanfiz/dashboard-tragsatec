import dash
from dash import html, dcc, register_page, callback, Input, Output
import dash_bootstrap_components as dbc
from components.nav_arrows import nav_arrows

register_page(
    __name__,
    path="/downscaling/results/scores",
    name="Downscaling Results - Scores"
)

PROXY_PREFIX = "/user/esp9221/proxy/8055/"
BASE = f"{PROXY_PREFIX}assets/imgs_downscaling/scores"

# ======================
# Dropdown options
# ======================

SCORE_OPTIONS = [
    {"label": "BSS Lower Tercile", "value": "BSS_lower"},
    {"label": "BSS Upper Tercile", "value": "BSS_upper"},
    {"label": "Temporal Correlation", "value": "r"},
    {"label": "ROC Area Lower Tercile", "value": "ROC_lower"},
    {"label": "ROC Area Upper Tercile", "value": "ROC_upper"},
]

# Mapping from dropdown -> filenames (EOBS vs AEMET)
FILEMAP = {
    "BSS_lower": {
        "EOBS":  "prNDJFM_BSS_lower_mw1_E-OBSv16_MW1_ecmf_s5_1997-2016.png",
        "AEMET": "prNDJFM_BSS_lower_mw1_AEMET_MW2_S51.NDJFM_1997-2016.png"
    },
    "BSS_upper": {
        "EOBS":  "prNDJFM_BSS_upper_mw1_E-OBSv16_MW1_ecmf_s5_1997-2016.png",
        "AEMET": "prNDJFM_BSS_upper_mw1_AEMET_MW2_S51.NDJFM_1997-2016.png"
    },
    "r": {
        "EOBS":  "prNDJFM_r_mw1_E-OBSv16_MW1_ecmf_s5_1997-2016.png",
        "AEMET": "prNDJFM_r_mw1_AEMET_MW2_S51.NDJFM_1997-2016.png"
    },
    "ROC_lower": {
        "EOBS":  "prNDJFM_rocAreaLower_mw1_E-OBSv16_MW1_ecmf_s5_1997-2016.png",
        "AEMET": "prNDJFM_rocAreaLower_mw1_AEMET_MW2_S51.NDJFM_1997-2016.png"
    },
    "ROC_upper": {
        "EOBS":  "prNDJFM_rocAreaUpper_mw1_E-OBSv16_MW1_ecmf_s5_1997-2016.png",
        "AEMET": "prNDJFM_rocAreaUpper_mw1_AEMET_MW2_S51.NDJFM_1997-2016.png"
    },
}

# ======================
# LAYOUT
# ======================

layout = dbc.Container([

    html.H2(
        "Downscaled Precipitation Scores",
        style={"textAlign": "center", "color": "#003060", "marginBottom": "30px"}
    ),

    html.P(
        """
        Explore the comparison between raw Copernicus/E-OBS scores and AEMET downscaled scores 
        for NDJFM precipitation. Select a score metric to visualise both maps side by side.
        """,
        style={
            "textAlign": "center",
            "maxWidth": "800px",
            "margin": "0 auto 40px auto",
            "color": "#003060",
            "fontSize": "0.95rem"
        }
    ),

    dbc.Row([

        # -----------------------------------
        # LEFT — DROPDOWN
        # -----------------------------------
        dbc.Col([
            html.Label("Select Score", style={"fontWeight": "bold"}),
            dcc.Dropdown(
                id="score-select",
                options=SCORE_OPTIONS,
                value="BSS_lower",
                clearable=False,
                style={"marginBottom": "25px"}
            ),
        ], md=3),

        # -----------------------------------
        # RIGHT — IMAGES: EOBS vs AEMET
        # -----------------------------------
        dbc.Col([

            dbc.Row([

                # EOBS LEFT
                dbc.Col([
                    html.H5("Copernicus / E-OBS",
                            style={"textAlign": "center", "color": "#003060"}),
                    html.Img(
                        id="eobs-img",
                        style={
                            "width": "100%",
                            "borderRadius": "8px",
                            "boxShadow": "0 0 12px rgba(0,0,0,0.25)"
                        }
                    )
                ], md=6),

                # AEMET RIGHT
                dbc.Col([
                    html.H5("AEMET Downs / ROCIO_IBEB",
                            style={"textAlign": "center", "color": "#003060"}),
                    html.Img(
                        id="aemet-img",
                        style={
                            "width": "100%",
                            "borderRadius": "8px",
                            "boxShadow": "0 0 12px rgba(0,0,0,0.25)"
                        }
                    )
                ], md=6),

            ], className="g-3"),

        ], md=9),

    ]),

    # -------- NAV ARROWS --------
    nav_arrows(
        prev_href=f"{PROXY_PREFIX}downscaling/results/terciles",
        prev_text="Back"
    ),

], style={"padding": "40px"})


# ======================
# CALLBACK
# ======================

@callback(
    Output("eobs-img", "src"),
    Output("aemet-img", "src"),
    Input("score-select", "value")
)
def update_score_images(score_key):

    files = FILEMAP[score_key]

    eobs_path = f"{BASE}/{files['EOBS']}"
    aemet_path = f"{BASE}/{files['AEMET']}"

    return eobs_path, aemet_path
