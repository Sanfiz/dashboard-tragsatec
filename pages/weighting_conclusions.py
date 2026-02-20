import dash
from dash import html, dcc, register_page
import dash_bootstrap_components as dbc
from components.nav_arrows import nav_arrows

# Register page
register_page(
    __name__,
    path="/weighting/conclusions",
    name="Weighting – Conclusions",
    title="● Weighting Conclusions ●"
)

PROXY_PREFIX = "/user/esp9221/proxy/8055/"
AEMET_BLUE = "#003060"

# ===========================
#           LAYOUT
# ===========================
layout = dbc.Container(
    [

        html.H2(
            "Final Take-Home Messages",
            className="text-center mb-4",
            style={"color": AEMET_BLUE}
        ),

        # ===========================
        # CONCLUSIONS BLOCK
        # ===========================
        dbc.Row(
            dbc.Col(
                html.Div(
                    [
                        html.H4("Conclusions", style={"textAlign": "center", "color": AEMET_BLUE}),
                        html.Ul(
                            [
                                html.Li(
                                    html.Span([
                                        html.B("Clear winter window of opportunity"),
                                        " to improve Iberian precipitation forecasts using ",
                                        html.B("EOF-based"),
                                        " ensemble weighting."
                                    ])
                                ),
                                html.Li(
                                    html.Span([
                                        "Preliminary gains for 2-m temperature in spring with ",
                                        html.B("PLS"),
                                        ", with potential benefits in other lower-skill periods."
                                    ])
                                ),
                            ],
                            style={
                                "fontSize": "1.05rem",
                                "lineHeight": "1.55",
                                "maxWidth": "850px",
                                "margin": "0 auto"
                            },
                        )
                    ],
                    style={"padding": "25px", "border": "2px dashed #b33", "borderRadius": "8px"}
                ),
                md=10
            ),
            className="justify-content-center mb-4"
        ),

        # ===========================
        # OUTLOOK BLOCK
        # ===========================
        dbc.Row(
            dbc.Col(
                html.Div(
                    [
                        html.H4("Outlook", style={"textAlign": "center", "color": AEMET_BLUE}),
                        html.Ul(
                            [
                                html.Li(
                                    html.Span([
                                        "Short term: ",
                                        html.B("Research under development → Refine the methodology"),
                                        " (feature selection, cross-validation, weighting)."
                                    ])
                                ),
                                html.Li(
                                    html.Span([
                                        "Long long-term: Operationalise ",
                                        html.B("EOF/PLS-based"),
                                        " ensemble weighting for Iberia and integrate it into the operational workflow."
                                    ])
                                ),
                            ],
                            style={
                                "fontSize": "1.05rem",
                                "lineHeight": "1.55",
                                "maxWidth": "850px",
                                "margin": "0 auto"
                            },
                        )
                    ],
                    style={"padding": "25px", "border": "2px dashed #b33", "borderRadius": "8px"}
                ),
                md=10
            ),
            className="justify-content-center"
        ),

        html.Br(),

        # ========================
        # NAVIGATION
        # ========================
        nav_arrows(
            prev_href=f"{PROXY_PREFIX}weighting/results",
            next_href=f"{PROXY_PREFIX}weighting",
            prev_text="Back to Results",
            next_text="Return to Weighting Menu"
        ),
    ],
    fluid=True,
    style={"padding": "40px"}
)
