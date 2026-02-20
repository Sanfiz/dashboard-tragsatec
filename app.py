import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

# ---------------------------------------------------------------------------------------------------

# CONFIGURA GENERAL PARA RENDER.COM
JUPYTERHUB_ROUTE = "/"

 
# ---------------------------------------------------------------------------------------------------
# SETUP
AEMET_BLUE = "#b8dbcb"

# Inicia la app
app = dash.Dash(__name__,use_pages=True,requests_pathname_prefix=JUPYTERHUB_ROUTE,external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server 


BACKGROUND_STYLE = {
    'backgroundImage': f'linear-gradient(rgba(255,255,255,0.5), rgba(255,255,255,0.5)), url("{JUPYTERHUB_ROUTE}assets/fondo-gris.png")',
    'backgroundSize': 'cover',
    'backgroundAttachment': 'fixed',
    'backgroundRepeat': 'no-repeat',
    'backgroundPosition': 'center center',
    'minHeight': '100vh'}



# --- 1. ENCABEZADO ---

def header_logos():
    """logos y Titulo"""
    return dbc.Container(
        html.Div([
                html.Img(src=f"/assets/tragsatec.jpg",className="logo-tragsatec me-4"),
                html.Img(src=f"/assets/aemet_azul.png",className="logo-aemet me-3"),
                
                html.H3("Seasonal Forecasting",style={"marginLeft": "350px","color": "#b0b2b5","fontWeight": "400",},),   
                html.H4("Developed by Tragsatec for AEMET",style={"marginLeft": "auto","color": "#b0b2b5","fontWeight": "100",},), 
            ],
            className="d-flex align-items-center py-3"),fluid=True,
        className="bg-white border-bottom shadow-sm" # Fondo 
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
                    dbc.NavLink("|", active="exact", className="nav-link-aemet"),
                    dbc.NavLink("What's Next  ", href=f"{JUPYTERHUB_ROUTE}whatsnext", active="exact", className="nav-link-aemet"),

                ],
                className="p-0 ms-auto",
                navbar=True,
            ),
        ]),
        className="navbar-aemet p-0",   
        dark=True,
        expand="lg")

    


# --- 2. LAYOUT PRINCIPAL ---

app.layout = html.Div([

    dcc.Location(id='url', refresh=False),

    header_logos(),
    navbar_menu(),

    # ---- CONTENIDO  ----
    dbc.Container(
        dash.page_container,
        fluid=True,
        className="py-5",
        style={"flex": "1"}
    ),

    # ---- FOOTER ----
    html.Footer(
    dbc.Container(
        html.Div(
            [
                html.P("Marta Domínguez & Sabela Sanfiz (Tragsatec) ● Esteban Rodríguez (AEMET)",
                    className="mb-0",
                    style={"color": "grey"}
                ),
            ],
            className="text-muted",
            style={"fontSize": "11px", "textAlign": "center"},
        ),
        fluid=True
    ),
    className="py-3"
)
],
                      
style={**BACKGROUND_STYLE, "display": "flex", "flexDirection": "column", "minHeight": "100vh"})

# --- 3. EXECUTE SERVER ---
if __name__ == '__main__':
    #app.run( host='0.0.0.0', port=JUPYTERHUB_PORT, debug=True)
    app.run(host='0.0.0.0', port=8055, debug=True)

