from dash import html, register_page, dcc
import dash_bootstrap_components as dbc

register_page(__name__, path="/")

# Definir la ruta del proxy (DEBE coincidir con la de app.py)
# Definir la ruta del proxy aquí para que los botones de navegación grandes funcionen.
# Si el usuario o puerto cambian, debe actualizarse en app.py Y en home.py.
PROXY_PREFIX = "/user/esp9221/proxy/8055/"


AEMET_BLUE = "#003060"

# Estilo para los botones/tarjetas (similar al que usa AEMET para las opciones)
CARD_STYLE = {
    "width": "90%", 
    "padding": "40px", 
    "borderRadius": "10px", 
    "boxShadow": "0 4px 12px rgba(0, 0, 0, 0.1)",
    "border": "1px solid #dee2e6", 
    "backgroundColor": "white",
    "textAlign": "center",
    "transition": "all 0.3s ease", 
    "cursor": "pointer",
    "margin": "0 auto"}


layout = dbc.Container([
    dbc.Row([
        # Módulo Downscaling
        dbc.Col(
            # Usamos un dcc.Link que contiene un Div para que toda la tarjeta sea clickable
            dcc.Link(
                html.Div(
                    [
                        # Icono opcional para Downscaling (ejemplo: un icono de flecha/mapa)
                        html.I(className="bi bi-arrow-down-right-square-fill", style={"fontSize": "3rem", "color": AEMET_BLUE, "marginBottom": "15px"}),
                        html.H4("Downscaling", className="fw-bold mb-3"),

                        html.Img(
                            src=f"{PROXY_PREFIX}assets/downscaling_iberia.png", 
                            alt="Imagen del método de Downscaling",
                            style={"maxWidth": "80%", "height": "auto", "marginBottom": "20px", "borderRadius": "5px", "boxShadow": "0 2px 8px rgba(0,0,0,0.1)"}),
     
                        html.P("Access the visualisation and analysis of the outputs from the downscaling process.", className="text-muted"),
                    ],
                    id="downscaling-card",
                    style=CARD_STYLE,
                    className="d-flex flex-column align-items-center justify-content-center h-100"
                ),
                href=f"{PROXY_PREFIX}downscaling",
                className="text-decoration-none" # Quita el subrayado del enlace
            ),
            md=6, 
            className="mb-4" 
        ),
        
        # Módulo Ensemble Weighting
        dbc.Col(
            # Usamos un dcc.Link que contiene un Div para que toda la tarjeta sea clickable
            dcc.Link(
                html.Div(
                    [
                        # Icono opcional para Weighting (ejemplo: un icono de balanza/ajuste)
                        html.I(className="bi bi-sliders", style={"fontSize": "3rem", "color": AEMET_BLUE, "marginBottom": "15px"}),
                        html.H4("Ensemble Weighting", className="fw-bold mb-3"),

                        html.Img(
                            src=f"{PROXY_PREFIX}assets/method2-image.png", 
                            alt="Imagen del método de Weighting",
                            style={"maxWidth": "80%", "height": "auto", "marginBottom": "20px", "borderRadius": "5px", "boxShadow": "0 2px 8px rgba(0,0,0,0.1)"}
                        ),


                        
                        html.P("Explore the methodology and results of the ensemble weighting applied to seasonal forecasting.", className="text-muted"),
                    ],
                    id="weighting-card",
                    style=CARD_STYLE,
                    className="d-flex flex-column align-items-center justify-content-center h-100"
                ),
                href=f"{PROXY_PREFIX}weighting",
                className="text-decoration-none" # Quita el subrayado del enlace
            ),
            md=6,
            className="mb-4"
        )
    ], className="g-4 justify-content-center")
], fluid=True)