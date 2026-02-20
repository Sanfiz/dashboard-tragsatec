import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

# CONFIGURA DE PROXY PARA JUPYTERHUB 
JUPYTERHUB_USER = "esp9221"
JUPYTERHUB_PORT = 8055
JUPYTERHUB_ROUTE = f"/user/{JUPYTERHUB_USER}/proxy/{JUPYTERHUB_PORT}/"
 
AEMET_BLUE = "#003060"
# ----------------------------------------------------

# Inicia la app
app = dash.Dash(__name__,use_pages=True,requests_pathname_prefix=JUPYTERHUB_ROUTE,external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server # Necesario para Flask/WSGI


BACKGROUND_STYLE = {
    'backgroundImage': f'url("{JUPYTERHUB_ROUTE}assets/fondo-isobaras.jpg")',
    'backgroundSize': 'cover',
    'backgroundAttachment': 'fixed',
    'backgroundRepeat': 'no-repeat',
    'backgroundPosition': 'center center',
    'minHeight': '100vh',
    'backgroundColor': '#f8f9fa'}


# --- COMPONENTES DEL ENCABEZADO ---

def header_logos():
    """logos AEMET y Tragsatec"""
    return dbc.Container(
        html.Div(
            [html.Img(src=f"{JUPYTERHUB_ROUTE}assets/imagen-logo1.svg",className="logo-aemet me-3"),
                html.Img(src=f"{JUPYTERHUB_ROUTE}assets/tragsatec.jpg",className="logo-tragsatec ms-4"),
            ],
            className="d-flex align-items-center py-3"),fluid=True,
        className="bg-white border-bottom shadow-sm" # Fondo blanco y una ligera sombra
    )


def navbar_menu():
    return dbc.Navbar(
        dbc.Container([
            dbc.NavbarBrand(""),
            dbc.Nav(
                [
                    dbc.NavLink("Home   ", href=JUPYTERHUB_ROUTE, active="exact", className="nav-link-aemet"),
                    dbc.NavLink("|", active="exact", className="nav-link-aemet"),
                    dbc.NavLink("Data   ", href=f"{JUPYTERHUB_ROUTE}data", active="exact", className="nav-link-aemet"),
                    dbc.NavLink("|", active="exact", className="nav-link-aemet"),
                    dbc.NavLink("Downscaling   ", href=f"{JUPYTERHUB_ROUTE}downscaling", active="exact", className="nav-link-aemet"),
                    dbc.NavLink("|", active="exact", className="nav-link-aemet"),
                    dbc.NavLink("Weighting   ", href=f"{JUPYTERHUB_ROUTE}weighting", active="exact", className="nav-link-aemet"),
                    dbc.NavLink("|", active="exact", className="nav-link-aemet"),
                    dbc.NavLink("Funding   ", href=f"{JUPYTERHUB_ROUTE}funding", active="exact", className="nav-link-aemet"),
                ],
                className="p-0 ms-auto",
                navbar=True,
            ),
        ]),
        className="navbar-aemet p-0",   
        dark=True,
        expand="lg")

    


# --- 2. DEFINICIÓN DEL LAYOUT PRINCIPAL ---

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),

    header_logos(), # logos y titulo
    navbar_menu(),  # menu de navegacion

    # contenido de la página actual
    dbc.Container(dash.page_container, fluid=True, className="py-5" ),

    # pie de pagina
    html.Footer(
        dbc.Container(
            html.Div([html.P("Marta Dominguez ● Sabela Sanfiz", className="mb-0")],
                className="text-muted",
                style={"fontSize": "10px"}),
            fluid=True),
        className="mt-auto py-3 bg-white")
    ], style = {
        **BACKGROUND_STYLE,
        "display": "flex",
        "flexDirection": "column",
        "minHeight": "100vh"
    } )


# --- 3. EJECUCIÓN DEL SERVIDOR ---
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=JUPYTERHUB_PORT,
        debug=True
    )