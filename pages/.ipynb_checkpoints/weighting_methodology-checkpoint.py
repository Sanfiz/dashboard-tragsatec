import dash
from dash import html, dcc, register_page
import dash_bootstrap_components as dbc
from components.nav_arrows import nav_arrows


PROXY_PREFIX = "/user/esp9221/proxy/8055/" 

register_page(
    __name__,
    path="/weighting/methodology",
    name="Weighting - Methodology"
)

# Layout 
layout = dbc.Container(
    [

        html.H2(
            "Weighting Methodology",
            style={
                "textAlign": "center",
                "color": "#003060",
                "marginBottom": "40px"
            }
        ),

        # ------------------------------
        # CONTENIDO DEL TEXTO
        # ------------------------------
html.Div(
    [

  
        # =======================================================================
        # 1. Variability Modes (EOF or PLS)
        # =======================================================================
        html.H4("1. Variability Modes: EOF or PLS",
                style={"color": "#003060", "marginTop": "10px"}),

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
                by Clementine Dalelane, Andreas Paxian, Martín Senande, Sabela Sanfiz, 
                Esteban Rodríguez Guisado, Jan Wandel, and Abhinav Tyagi (2025).
                """
            ],
            style={"fontSize": "0.9rem", "lineHeight": "1.45"}
        ),

        # =======================================================================
        # 2. Ensemble Member Weighting
        # =======================================================================

        html.Br(),
        html.H4("2. Ensemble Member Weighting",
                style={"color": "#003060", "marginTop": "20px"}),

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
)

,

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
