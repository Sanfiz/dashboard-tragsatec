import dash
from dash import html, dcc, register_page, callback, Input, Output
import dash_bootstrap_components as dbc
from components.nav_arrows import nav_arrows


IMG_BASE = f"/assets/imgs_weighting/pls"

# Register page
register_page(
    __name__,
    path="/weighting/results/pls",
    name="Weighting Results - PLS",
    title="Weighting PLS"
)

# ============================
# LAYOUT
# ============================
layout = dbc.Container([

    #html.H2("PLS-Based Weighting Results",style={"textAlign": "center","color": "#003060","marginBottom": "30px"}),

    # ============================
    # BLOQUE SUPERIOR: SCORECARDS
    # ============================


    dbc.Row([
        dbc.Col([
            html.Label("Variable", style={"fontWeight": "bold"}),
            dcc.Dropdown(
                id="pls-score-var",
                options=[
                    {"label": "Temperature", "value": "t2m"},
                    {"label": "Precipitation", "value": "tprate"},
                ],
                value="t2m",
                clearable=False
            )
        ], md=3),
    ], className="mb-3"),

    dbc.Row(
        [
            # Izquierda: EOF_minus_RAW_scorecard
            dbc.Col([

                html.H4(" EOF Weighted Tunned minus RAW Copernicus",style={
                        "textAlign": "center",
                        "color": "#003060",
                        "marginTop": "10px",
                        "marginBottom": "15px"
                    }
                ),



                
                html.Img(
                    id="pls-score-left-img",
                    style={
                        "width": "100%",
                        "borderRadius": "10px",
                        "boxShadow": "0 0 12px rgba(0,0,0,0.25)",
                        "display": "block",
                        "margin": "0 auto"
                    }
                ),
            ],
                md=6,
                className="mb-4"
            ),

            # Derecha: PLS_minus_RAW_scorecard
            dbc.Col([

                html.H4(" PLS Weighted Tunned minus RAW Copernicus",style={
                        "textAlign": "center",
                        "color": "#003060",
                        "marginTop": "10px",
                        "marginBottom": "15px"
                    }
                ),




                
                html.Img(
                    id="pls-score-right-img",
                    style={
                        "width": "100%",
                        "borderRadius": "10px",
                        "boxShadow": "0 0 12px rgba(0,0,0,0.25)",
                        "display": "block",
                        "margin": "0 auto"
                    }
                ),
            ],
                md=6,
                className="mb-4"
            ),
        ],
        className="g-3"
    ),

    html.Hr(style={"margin": "40px 0"}),

    # ===================================
    # BLOQUE INFERIOR: 2METHODS + STMONTH
    # ===================================
    html.H6(
        "Correlation Difference between Methods",
        style={
            "textAlign": "left",
            "color": "#003060",
            "marginTop": "10px",
            "marginBottom": "15px"
        }
    ),

    dbc.Row([
        dbc.Col([
            html.Label("Variable ", style={"fontWeight": "bold"}),
            dcc.Dropdown(
                id="pls-2m-var",
                options=[
                    {"label": "Temperature ", "value": "t2m"},
                    {"label": "Precipitation ", "value": "tprate"},
                    {"label": "Pressure ", "value": "msl"},
                ],
                value="t2m",
                clearable=False
            )
        ], md=3),

        dbc.Col([
            html.Label("Start month (stmonth)", style={"fontWeight": "bold"}),
            dcc.Dropdown(
                id="pls-2m-stmonth",
                options=[
                    {"label": f"{m:02d}", "value": f"{m:02d}"} for m in range(1, 13)
                ],
                value="01",
                clearable=False
            )
        ], md=3),
    ], className="mb-3"),

    dbc.Row([
        dbc.Col(
            html.Img(
                id="pls-2m-img",
                style={
                    "width": "80%",
                    "borderRadius": "10px",
                    "boxShadow": "0 0 12px rgba(0,0,0,0.25)",
                    "display": "block",
                    "margin": "0 auto"
                }
            ),
            md=10
        )
    ], className="justify-content-center mb-4"),

    # -------------------------
    # NAVIGATION ARROWS
    # -------------------------
    nav_arrows(
        prev_href=f"{/weighting/results",
        prev_text="Back"
    )

], fluid=True, style={"padding": "40px"})


# ============================
# CALLBACKS
# ============================
@callback(
    Output("pls-score-left-img", "src"),
    Output("pls-score-right-img", "src"),
    Input("pls-score-var", "value")
)
def update_scorecards(var):
    """
    Arriba: dos scorecards según variable (t2m / tprate).
    Izquierda: EOF_minus_RAW_scorecard_<var>.png
    Derecha:   PLS_minus_RAW_scorecard_<var>.png
    """
    left = f"{IMG_BASE}/EOF_minus_RAW_scorecard_{var}.png"
    right = f"{IMG_BASE}/PLS_minus_RAW_scorecard_{var}.png"
    return left, right


@callback(
    Output("pls-2m-img", "src"),
    Input("pls-2m-var", "value"),
    Input("pls-2m-stmonth", "value")
)
def update_2methods_image(var, stmonth):
    """
    Abajo: imagen 2methods_diff_corr_<var>_Iberia.png
    dentro de la carpeta correspondiente al start month:
    stmonthXX/2methods_diff_corr_<var>_Iberia.png
    """
    img_path = f"{IMG_BASE}/stmonth{stmonth}/2methods_diff_corr_{var}_Iberia.png"
    return img_path
