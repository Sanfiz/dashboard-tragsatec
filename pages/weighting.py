import dash
from dash import html, register_page, dcc
import dash_bootstrap_components as dbc
from components.nav_arrows import nav_arrows

register_page(__name__, path="/weighting", name="● Weighting ●")

PROXY_PREFIX = "/user/esp9221/proxy/8055/"
IMG_BASE = f"{PROXY_PREFIX}assets/imgs_weighting"

layout = dbc.Container(
    [

        # ===========================
        #   MENU PRINCIPAL (4 ICONOS)
        # ===========================
        dbc.Row(
            [

                # WHY
                dbc.Col(
                    dcc.Link(
                        html.Img(
                            src=f"{IMG_BASE}/why_wei.png",
                            style={
                                "maxWidth": "60%",
                                "cursor": "pointer",
                                "borderRadius": "40px",
                                "boxShadow": "0 4px 14px rgba(0,0,0,0.2)",
                                "display": "block",
                                "margin": "0 auto"
                            }
                        ),
                        href=f"{PROXY_PREFIX}weighting/why",
                    ),
                    md=3,
                    className="d-flex justify-content-center p-0"
                ),

                # METHODOLOGY
                dbc.Col(
                    dcc.Link(
                        html.Img(
                            src=f"{IMG_BASE}/methodology_wei.png",
                            style={
                                "maxWidth": "60%",
                                "cursor": "pointer",
                                "borderRadius": "40px",
                                "boxShadow": "0 4px 14px rgba(0,0,0,0.2)",
                                "display": "block",
                                "margin": "0 auto"
                            }
                        ),
                        href=f"{PROXY_PREFIX}weighting/methodology",
                    ),
                    md=3,
                    className="d-flex justify-content-center p-0"
                ),

                # RESULTS
                dbc.Col(
                    dcc.Link(
                        html.Img(
                            src=f"{IMG_BASE}/results_wei.png",
                            style={
                                "maxWidth": "60%",
                                "cursor": "pointer",
                                "borderRadius": "40px",
                                "boxShadow": "0 0 12px rgba(0,0,0,0.15)",
                                "display": "block",
                                "margin": "0 auto"
                            }
                        ),
                        href=f"{PROXY_PREFIX}weighting/results",
                    ),
                    md=3,
                    className="d-flex justify-content-center p-0"
                ),

                # TAKE-HOME
                dbc.Col(
                    dcc.Link(
                        html.Img(
                            src=f"{IMG_BASE}/conclusions.png",
                            style={
                                "maxWidth": "60%",
                                "cursor": "pointer",
                                "borderRadius": "40px",
                                "boxShadow": "0 4px 14px rgba(0,0,0,0.2)",
                                "display": "block",
                                "margin": "0 auto"
                            }
                        ),
                        href=f"{PROXY_PREFIX}weighting/conclusions",
                    ),
                    md=3,
                    className="d-flex justify-content-center p-0"
                ),

            ],
            className="g-0 justify-content-center align-items-center my-4"
        ),

        # ================
        # NAVIGATION ARROWS
        # ================
        nav_arrows(
            prev_href=f"{PROXY_PREFIX}",
            next_href=f"{PROXY_PREFIX}weighting",
            prev_text="Back to Downscaling",
            next_text="Go to Funding"
        )
    ],
    fluid=True,
)
