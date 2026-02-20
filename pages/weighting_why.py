import dash
from dash import html, dcc, register_page
import dash_bootstrap_components as dbc
from components.nav_arrows import nav_arrows

# Register page
register_page(
    __name__,
    path="/weighting/why",
    name="Weighting – Why?"
)


CARD_STYLE = {
    "padding": "18px 22px",
    "borderRadius": "12px",
    "backgroundColor": "white",
    "boxShadow": "0 2px 8px rgba(0,0,0,0.12)",
    "marginBottom": "18px",
    "fontSize": "15px",
    "lineHeight": "1.5"
}


# Proxy for JupyterHub
PROXY_PREFIX = "/user/esp9221/proxy/8055/"
IMG_BASE = f"{PROXY_PREFIX}assets/imgs_weighting"


# ==========================
# LAYOUT
# ==========================
layout = dbc.Container(

    [

        # Title
    html.H2(
        "Goal",
        style={
            "textAlign": "center",
            "color": "#003060",
            "marginBottom": "40px"
        }
    ),
    
    html.P(
        """
        To identify windows of opportunity for improving the predictability 
        of winter precipitation and spring temperature over the Iberian Peninsula 
        and the broader Mediterranean (MedCOF) region.
        """,
        style={"fontSize": "1.05rem", "lineHeight": "1.55", 
               "maxWidth": "900px", "margin": "0 auto","marginBottom": "40px"}
    ),
    
    
            
    # Title
    html.H4(
        "Euro-Atlantic Circulation as a Driver of Skill",
        style={
            "textAlign": "center",
            "color": "#003060",
            "marginBottom": "10px"
        }
    ),
            
            
    dbc.Container([
    
                # 1 — NAO
                html.Div(
                    [
                        html.Strong(
                            "Due to strong NAO-driven circulation over the Iberia & Mediterranean region, "
                            "winter precipitation, and to a lesser extent temperature, shows relatively high skill."
                        ),
                    ],
                    style={**CARD_STYLE, "padding": "20px 24px"}  # un poco más espacioso
                ),


                # 2 — Beyond best-NAO
        html.Div(
            [
                html.Strong("Beyond best-NAO"), html.Br(),
                "Why not to investigate methodology that goes beyond a simple NAO-based approach, "
                "capturing additional modes of Euro-Atlantic variability relevant for Iberia."
            ],
            style=CARD_STYLE
        ),


        
            # 3 — EOF/PLS
            html.Div(
                [
                    html.Strong("EOF/PLS + Ensemble Weighting: isolating dominant Euro-Atlantic modes"), html.Br(),
                    "NAO (North Atlantic Oscillation), EA (East Atlantic), SCA (Scandinavian pattern), EAWR (East Atlantic–Western Russia)"
                ],
                style=CARD_STYLE
            ),
    

    
    ], style={"maxWidth": "850px"}),

        
  

        # Navigation arrows
        nav_arrows(
            prev_href=f"{PROXY_PREFIX}weighting",
            next_href=f"{PROXY_PREFIX}weighting/methodology",
            prev_text="Back to Main Weighting Menu",
            next_text="Go to Methodology"
        ),

    ],

    fluid=True,
    style={"padding": "40px"}
)
