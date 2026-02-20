import dash
from dash import html, register_page, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from components.nav_arrows import nav_arrows

register_page(
    __name__,
    path="/downscaling/results/terciles",
    name="Downscaling Results — Terciles"
)


BASE = f"/assets/imgs_downscaling/terciles/ecmwf"

# ---- REGIONES ----
REGIONS = [
    {"label": "Andalucía", "value": "Andalucía"},
    {"label": "Castilla-La Mancha", "value": "Castilla-La_Mancha"},
    {"label": "Galicia", "value": "Galicia"},
]

layout = html.Div([

    html.H2("Downscaled Terciles",
        style={"textAlign": "center", "color": "#003060", "marginBottom": "30px"}),

    dbc.Container([

        # ============================================================
        #   IMAGEN PRINCIPAL (CLICABLE)
        # ============================================================
        html.Div(
            html.Img(
                id="terciles-main-image",
                n_clicks=0,
                src=f"{BASE}/terciles_ecmwf_lead102025_NDJFM.png",
                style={
                    "maxWidth": "90%",
                    "display": "block",
                    "margin": "0 auto 40px auto",
                    "borderRadius": "10px",
                    "boxShadow": "0 0 12px rgba(0,0,0,0.2)",
                    "cursor": "pointer"
                }
            )
        ),

        # ============================================================
        #   DROPDOWN PARA REGIÓN
        # ============================================================
        html.Label("Select Autonomous Community",
            style={"fontWeight": "bold", "textAlign": "center",
                   "display": "block", "width": "100%", "marginBottom": "5px"}),

        dcc.Dropdown(
            id="terciles-region",
            options=REGIONS,
            value="Andalucía",
            clearable=False,
            style={"width": "40%", "fontSize": "0.9rem",
                   "margin": "0 auto 30px auto"}
        ),

        # ============================================================
        #   IMAGEN POR COMUNIDAD AUTÓNOMA
        # ============================================================
        html.Div(
            html.Img(
                id="terciles-image",
                src="",
                style={
                    "maxWidth": "90%",
                    "display": "block",
                    "margin": "0 auto",
                    "borderRadius": "10px",
                    "boxShadow": "0 0 12px rgba(0,0,0,0.2)"
                }
            ),
            className="d-flex justify-content-center"
        ),

        # ============================================================
        #   MODAL PARA AMPLIAR IBERIA
        # ============================================================
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Terciles Iberian Peninsula")),

                dbc.ModalBody(
                    dbc.Row([
                
                        # ---- COLUMNA IZQUIERDA: IMAGEN GRANDE ----
                        dbc.Col(
                            html.Img(
                                id="modal-terciles-image",
                                src=f"{BASE}/terciles_ecmwf_lead102025_NDJFM.png",
                                style={"width": "100%", "maxWidth": "1400px", "height": "auto", "borderRadius": "10px"}
                            ),
                            md=10
                        ),
                
                        # ---- COLUMNA DERECHA: TEXTO ----
                        dbc.Col(
                                html.Div([
                                    html.H6("1. What are we looking at?", 
                                            style={"color": "#003060", "marginBottom": "8px", "textAlign": "center"}),
                                
                                    html.P(
                                        """
                                        Most likely tercile category of seasonal precipitation 
                                        (below, near, or above-normal) for the Iberian Peninsula. 
                                        Each grid point displays the probability associated with the forecast 
                                        ensemble for the upcoming season.
                                        """,
                                        style={"fontSize": "0.7rem", "lineHeight": "1.4"}
                                    ),
                                
                                    html.H6("2. How were the tercile probabilities computed?",
                                            style={"color": "#003060", "marginTop": "20px", "marginBottom": "10px", "textAlign": "center"}),
                                
                                    html.P(
                                        """
                                        Tercile thresholds (33% and 66%) were calculated from the C3S hindcast 
                                        for the period 1996–2016, defining the lower, middle, and upper terciles.
                                        These thresholds were applied to all forecast ensemble members to count 
                                        how many fall in each category. Probabilities follow:
                                        """,
                                        style={"fontSize": "0.7rem", "lineHeight": "1.4"}
                                    ),
                                
                                    html.P(
                                        "P = (members in tercile) / (total ensemble members)",
                                        style={"fontSize": "0.7rem", "fontStyle": "italic", "lineHeight": "1.6", "textAlign": "center"}
                                    ),
                                
                                    html.H6("3. What do we observe?",
                                            style={"color": "#003060", "marginTop": "20px", "marginBottom": "10px", "textAlign": "center"}),
                                
                                    html.P(
                                        """
                                        The downscaled precipitation (right) shows more realistic
                                        precipitation gradients than the raw forecast (left). Regions with higher 
                                        probability values indicate where the model ensemble shows stronger agreement 
                                        on a specific tercile outcome for the season.
                                        """,
                                        style={"fontSize": "0.7rem", "lineHeight": "1.4"}
                                    ),
                                ]),


                            md=2,
                            className="d-flex flex-column justify-content-start"
                        ),
                
                    ])
                ),

                dbc.ModalFooter(
                    dbc.Button("Close", id="close-terciles-modal", n_clicks=0)
                ),
            ],
            id="terciles-modal",
            size="xl",
            is_open=False,
            scrollable=True,
        ),

        # -------- NAV ARROWS --------
        nav_arrows(
            prev_href=f"/downscaling/results/precipitation",
            next_href=f"/downscaling/results/scores",
            prev_text="Back",
            next_text="Next: Scores"
        ),

        
    ], style={"maxWidth": "1100px"})

], style={"padding": "40px"})


# ---- CALLBACKS ----
@callback(
    Output("terciles-image", "src"),
    Input("terciles-region", "value")
)
def update_region_image(region):
    filename = f"terciles_ecmwf_lead102025_NDJFM_{region}.png"
    return f"{BASE}/{filename}"


@callback(
    Output("terciles-modal", "is_open"),
    Input("terciles-main-image", "n_clicks"),
    Input("close-terciles-modal", "n_clicks"),
    prevent_initial_call=True
)
def toggle_modal(open_click, close_click):
    ctx = dash.callback_context
    if not ctx.triggered:
        raise PreventUpdate
    trigger = ctx.triggered[0]["prop_id"].split(".")[0]
    return trigger == "terciles-main-image"
