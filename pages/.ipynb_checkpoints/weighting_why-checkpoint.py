import dash
from dash import html, dcc, register_page
import dash_bootstrap_components as dbc
from components.nav_arrows import nav_arrows
import plotly.graph_objects as go 

PROXY_PREFIX = "/user/esp9221/proxy/8055/" 

register_page(
    __name__,
    path="/weighting/methodology",
    name="Weighting - Methodology"
)




def make_diagram():
    """Diagrama interactivo """
    
    AEMET_BLUE = "#0A5EB8"
    AEMET_BLUE_DARK = "#0A304A"
    AEMET_BLUE_LIGHT = "#E6F1FA"
    
    fig_diagram = go.Figure()
    fig_diagram.update_xaxes(visible=False, range=[0, 12])
    fig_diagram.update_yaxes(visible=False, range=[0, 8])
    fig_diagram.update_layout(clickmode="event+select")

    fig_diagram.data = fig_diagram.data[::-1]

    
    shapes = []
    annots = []
    
    box_w = 2
    box_h = 1.2
    y_top = 5.3
    y_bot = 2.4
    
    
    # ------------------------------
    # Función inline para cajas
    # ------------------------------
    def add_box(x, y, w, h, text):
        
        shapes.append(dict(
            type="rect",x0=x, y0=y,x1=x + w, 
            y1=y + h,line=dict(color=AEMET_BLUE, width=2),
            fillcolor=AEMET_BLUE_LIGHT))
        
        annots.append(dict(
            x=x + w/2,
            y=y + h/2,
            text=text,
            showarrow=False,
            font=dict(size=15, color=AEMET_BLUE_DARK),
            xanchor="center",
            yanchor="middle"))
    
    # ------------------------------
    # Función inline para flechas
    # ------------------------------
    def add_arrow(x1, y1, x2, y2):
        shapes.append(dict(
            type="line",
            x0=x1, y0=y1,
            x1=x2, y1=y2,
            line=dict(color=AEMET_BLUE_DARK, width=2),
            arrowhead=3))
    
    
    x1 = 2.5
    x2 = 5
    x3 = 7.5
    
    # --- BOX 1 COMO TRACE INTERACTIVO (SIN SHAPE) ---
    fig_diagram.add_trace(go.Scatter(
        x=[x1, x1 + box_w, x1 + box_w, x1, x1],
        y=[y_top, y_top, y_top + box_h, y_top + box_h, y_top],
        fill="toself",
        fillcolor=AEMET_BLUE_LIGHT,
        line=dict(color=AEMET_BLUE, width=2),
        name="click_box1",
        hoverinfo="skip"
    ))
    
    # Texto de la caja 1
    annots.append(dict(
        x=x1 + box_w/2,
        y=y_top + box_h/2,
        text="ERA5 MSLP<br>Climatology 1940–2021",
        showarrow=False,
        font=dict(size=15, color=AEMET_BLUE_DARK),
        xanchor="center",
        yanchor="middle"
    ))
    
    # --- El resto de cajas siguen con shapes ---
    add_box(x2, y_top, box_w, box_h, "MSLP anomalies<br>3-month aggregated")
    add_box(x3, y_top, box_w, box_h, "EOF decomposition<br>4 EOFs & PCs kept<br>Variability modes")

    annots.append(dict(
        x=5, y=y_top + box_h/2,
        ax=4.5, ay=y_top + box_h/2,
        xref="x", yref="y",
        axref="x", ayref="y",
        showarrow=True, arrowhead=3, arrowsize=1.2, arrowwidth=2, arrowcolor=AEMET_BLUE_DARK))
    
    annots.append(dict(
        x=7.5, y=y_top + box_h/2, #sentido de la flecha
        ax=7, ay=y_top + box_h/2, #donde comienza la flecha
        xref="x", yref="y",
        axref="x", ayref="y",
        showarrow=True, arrowhead=3, arrowsize=1.2, arrowwidth=2, arrowcolor=AEMET_BLUE_DARK))
    
    
    # ------------------------------
    # Cajas fila inferior
    # ------------------------------
    add_box(x1, y_bot, box_w, box_h, "Ensemble<br>Hindcast / Forecast<br>MSLP anomalies")
    add_box(x2, y_bot, box_w, box_h, "Project into EOF/PLS<br>ERA5 → PCs per member")
    add_box(x3, y_bot, box_w, box_h, "Weight calculation<br>wᵢ(h) based on PC distance")
    
    annots.append(dict(
        x=5, y=y_bot + box_h/2,
        ax=4.5, ay=y_bot + box_h/2,
        xref="x", yref="y",
        axref="x", ayref="y",
        showarrow=True, arrowhead=3, arrowsize=1.2, arrowwidth=2, arrowcolor=AEMET_BLUE_DARK))
    
    annots.append(dict(
        x=7.5, y=y_bot + box_h/2,
        ax=7, ay=y_bot + box_h/2,
        xref="x", yref="y",
        axref="x", ayref="y",
        showarrow=True, arrowhead=3, arrowsize=1.2, arrowwidth=2, arrowcolor=AEMET_BLUE_DARK))
    
    
    # flecha vertical
    annots.append(dict(x=x3+1, y=y_bot + box_h,ax=x3+1, ay=y_top,xref="x", yref="y",axref="x", ayref="y",showarrow=True, arrowhead=3, arrowsize=1.2, arrowwidth=2, arrowcolor=AEMET_BLUE_DARK))
    
    
    # ------------------------------
    # Final
    # ------------------------------
    
    annots.append(dict(
        x=6, y=1.0,
        text=("The EOF modes are derived from ERA5.<br>"
              "The ensemble is projected onto these modes,<br>"
              "and weighted by similarity to the perfect forecast PCs."),
        showarrow=False,
        font=dict(size=15, color=AEMET_BLUE_DARK),
        xanchor="center"))
    
    
    # apply shapes + annotations
    fig_diagram.update_layout(
        shapes=shapes,
        annotations=annots,
        height=600,
        margin=dict(l=20, r=20, t=20, b=20),
        plot_bgcolor="white", hovermode=False)
    
    fig_diagram.update_layout(clickmode="event+select")

    return fig_diagram



layout = dbc.Container([

        html.H2("Weighting Methodology",style={"textAlign": "center","color": "#003060","marginBottom": "40px"}),

        dcc.Graph(
            id="diagram",
            figure=make_diagram(),
            config={"displayModeBar": True},
            style={"width": "80%", "margin": "0 auto"}
        ),
        html.Div(id="diagram-output", style={"textAlign": "center", "marginTop": "20px"}),

        html.Div(
            [

                # =======================================================================
                # 1. Variability Modes (EOF or PLS)
                # =======================================================================
                html.H4(
                    "1. Variability Modes: EOF or PLS",
                    style={"color": "#003060", "marginTop": "10px"}
                ),

                html.P(
                    """ Large-scale Euro-Atlantic circulation patterns strongly shape seasonal predictability over Iberia. 
                        These variability modes often exhibit higher forecast skill than the target variables (T2M, PR) themselves, 
                        making them an essential component of postprocessing strategies.
                    """,
                    style={"fontSize": "0.95rem", "lineHeight": "1.45"}
                ),

                html.P(
                    """
                    Two different approaches are used to extract these modes:
                    """,
                    style={"fontSize": "0.95rem", "lineHeight": "1.45", "marginTop": "5px"}
                ),

                html.Ul([

                    # EOF description
                    html.Li(
                        html.P(
                            """
                            EOF-based modes: computed from ERA5 MSLP anomalies over the North Atlantic–
                            European sector (90°W–60°E, 20°–85°N). The first four EOFs capture the main
                            Euro-Atlantic teleconnection patterns - NAO, EA, EAWR and SCA - that influence
                            Iberian temperature and precipitation.
                            """,
                            style={"fontSize": "0.95rem", "lineHeight": "1.45"}
                        )
                    ),

                    # EOF Figure
                    html.Div(
                        [
                            html.Img(
                                src=f"{PROXY_PREFIX}assets/imgs_weighting/ERA5_EOFs_DJF.png",
                                style={
                                    "maxWidth": "70%",
                                    "display": "block",
                                    "margin": "20px auto",
                                    "borderRadius": "10px",
                                    "boxShadow": "0 0 12px rgba(0,0,0,0.25)"
                                }
                            ),
                            html.P(
                                "Example: Leading winter EOFs of ERA5 MSLP anomalies, used as variability "
                                "modes for ensemble weighting.",
                                style={
                                    "textAlign": "center",
                                    "fontSize": "0.9rem",
                                    "fontStyle": "italic",
                                    "marginTop": "10px"
                                }
                            )
                        ]
                    ),

                    # PLS description
                    html.Li(
                        html.P(
                            """
                            PLS-based modes: targeted teleconnections derived using Partial Least Squares 
                            (PLS) regression. MSLP anomalies are used as predictors, while Iberian 
                            temperature (T2M) or precipitation (PR) anomalies serve as predictands. 
                            These modes optimise the circulation patterns most relevant for each surface 
                            variable, improving warm-season temperature skill (AMJ–ASO).
                            """,
                            style={"fontSize": "0.95rem", "lineHeight": "1.45"}
                        )
                    ),
                ]),

                # =======================================================================
                # PREPRINT REFERENCE + FIGURE (ADDED)
                # =======================================================================

                html.P(
                    [
                        """
                        The PLS methodology and its application to seasonal ensemble weighting 
                        are fully described in the study 
                        """,
                        html.A(
                            "“Targeted Teleconnections and their Application to the Postprocessing of Climate Predictions”",
                            href="https://egusphere.copernicus.org/preprints/2025/egusphere-2025-3664/",
                            target="_blank",
                            style={"fontWeight": "bold", "color": "#003060"}
                        ),
                        """
                        by Clementine Dalelane (2025).
                        """
                    ],
                    style={"fontSize": "0.9rem", "lineHeight": "1.45"}
                ),

                # === FIGURA PREPRINT (AÑADIDA AQUÍ) ===
                html.Div(
                    [
                        html.Img(
                            src=f"{PROXY_PREFIX}assets/imgs_weighting/preprint.png",
                            style={
                                "maxWidth": "70%",
                                "display": "block",
                                "margin": "25px auto 10px auto",
                                "borderRadius": "10px",
                                "boxShadow": "0 0 12px rgba(0,0,0,0.25)"
                            }
                        ),
                        html.P(
                            "Graphical abstract of the preprint describing the PLS-based methodology.",
                            style={
                                "textAlign": "center",
                                "fontSize": "0.85rem",
                                "fontStyle": "italic",
                                "marginTop": "8px"
                            }
                        )
                    ]
                ),

                # =======================================================================
                # 2. Ensemble Member Weighting
                # =======================================================================

                html.Br(),
                html.H4(
                    "2. Ensemble Member Weighting",
                    style={"color": "#003060", "marginTop": "20px"}
                ),

                html.P(
                    """
                    Ensemble weighting assigns higher weights to ensemble members whose circulation phase 
                    (EOF or PLS mode projection) is closer to the observed or predicted mode. This framework 
                    generalises subsampling (0/1 weighting) and enhances dynamical consistency, especially 
                    for winter NAO-related patterns.
                    """,
                    style={"fontSize": "0.95rem", "lineHeight": "1.45"}
                ),

                html.P(
                    """
                    The improvement achievable through weighting depends on two factors:
                    """,
                    style={"fontSize": "0.95rem", "lineHeight": "1.45"}
                ),

                html.Ul([
                    html.Li(
                        html.P(
                            "How much variance of the target variable (T2M, PR) is explained by the modes.",
                            style={"fontSize": "0.95rem", "lineHeight": "1.45"}
                        )
                    ),
                    html.Li(
                        html.P(
                            "How accurately the modes themselves can be predicted.",
                            style={"fontSize": "0.95rem", "lineHeight": "1.45"}
                        )
                    ),
                ]),

                html.P(
                    """
                    EOF-based weighting improves T2M and PR forecasts in winter and early spring, while 
                    PLS-based modes provide added value for warm-season temperature forecasts. 
                    Precipitation benefits less in summer due to its convective and locally driven nature.
                    """,
                    style={"fontSize": "0.95rem", "lineHeight": "1.45"}
                ),

            ],
            style={"maxWidth": "1000px", "margin": "0 auto"}
        ),

        # ----------------------
        # NAVIGATION ARROWS
        # ----------------------
        nav_arrows(
            prev_href=f"{PROXY_PREFIX}weighting",
            next_href=f"{PROXY_PREFIX}weighting/results",
            prev_text="Back to Weighting Menu",
            next_text="Go to Results"
        )

    ],                 
    fluid=True,
    style={"padding": "40px"}
)



# =====================================================
# CALLBACK: CLIC EN CAJA 1 → TRAER AL FRENTE
# =====================================================

from dash import callback, Input, Output, no_update

@callback(
    Output("diagram-output", "children"),
    Output("diagram", "figure"),
    Input("diagram", "clickData"),
)
def click_box(clickData):

    fig = make_diagram()

    if not clickData:
        return "clickData: None", fig

    return f"clickData: {clickData}", fig



