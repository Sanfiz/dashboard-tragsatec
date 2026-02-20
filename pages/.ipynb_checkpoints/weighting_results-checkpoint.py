import dash
from dash import html, dcc, register_page
import dash_bootstrap_components as dbc
from components.nav_arrows import nav_arrows

# Necesario para cargar imágenes en JupyterHub
PROXY_PREFIX = "/user/esp9221/proxy/8055/"
IMG_BASE = f"{PROXY_PREFIX}assets/imgs_weighting"

# Registrar la página
register_page(
    __name__,
    path="/weighting/results",
    name="Weighting - Results"
)

# Estilo card redonda con sombra
CARD_STYLE = {
    "maxWidth": "60%",
    "cursor": "pointer",
    "borderRadius": "99px",
    "boxShadow": "0 4px 14px rgba(0,0,0,0.18)",
    "display": "block",
    "margin": "0 auto"
}

layout = dbc.Container(
    [

        html.H4(
            "Weighting EOF Results",
            style={"textAlign": "center", "color": "#003060", "marginBottom": "40px"}
        ),

        html.P(
            """
            Explore the weighted seasonal forecast results.
            Each field is shown before and after applying the ensemble weighting based on EOF and PLS.
            """,
            style={"textAlign": "center", "maxWidth": "800px", "margin": "0 auto 40px auto",
                   "fontSize": "0.95rem"}
        ),

        dbc.Row(
            [

                # PRECIPITATION
                dbc.Col(
                    dcc.Link(
                        html.Div([
                            html.Img(
                                src=f"{IMG_BASE}/precipitation.png",
                                style=CARD_STYLE
                            ),
        
                        ]),
                        href=f"{PROXY_PREFIX}weighting/results/precipitation",
                        className="text-decoration-none"
                    ),
                    md=4,
                    className="d-flex justify-content-center"
                ),

                # TEMPERATURE
                dbc.Col(
                    dcc.Link(
                        html.Div([
                            html.Img(
                                src=f"{IMG_BASE}/temperature.png",
                                style=CARD_STYLE
                            ),
              
                        ]),
                        href=f"{PROXY_PREFIX}weighting/results/temperature",
                        className="text-decoration-none"
                    ),
                    md=4,
                    className="d-flex justify-content-center"
                ),

                # PLS
                dbc.Col(
                    dcc.Link(
                        html.Div([
                            html.Img(
                                src=f"{IMG_BASE}/pls.png",
                                style=CARD_STYLE
                            ),
              
                        ]),
                        href=f"{PROXY_PREFIX}weighting/results/pls",
                        className="text-decoration-none"
                    ),
                    md=4,
                    className="d-flex justify-content-center"
                ),






                

            ],
            className="justify-content-center g-4"
        ),

        # ----------------------
        # NAVIGATION ARROWS
        # ----------------------
        nav_arrows(
            prev_href=f"{PROXY_PREFIX}weighting",
            next_href=f"{PROXY_PREFIX}funding",
            prev_text="Back to Weighting Main",
            next_text="Go to Funding"
        )

        
    ],
    fluid=True,
    style={"padding": "40px"}
)
