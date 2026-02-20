import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(
    __name__,
    path="/data",
    name="Copernicus Data",
    title="● Data ●",
)

layout = dbc.Container(
    [
        html.H2("Copernicus Climate Data Store (C3S)", className="mb-4 text-center"),

        dbc.Row([
            dbc.Col([
                dbc.Card(
                    dbc.CardBody([
                        html.H4("Seasonal Forecast Data", className="card-title text-center"),
                            html.Br(),
                             html.P([
                                "This project uses data from ",
                                html.A(
                                    "Copernicus Climate Data Store (C3S)",
                                    href="https://cds.climate.copernicus.eu/",
                                    target="_blank",  
                                ),
                                html.Br(),
                                html.Br(),
                                "The models employed are ECMWF-SEAS5.1, DWD, CMCC."
                            ], className="card-text"),
                    ]),
                    className="mb-4 shadow-sm"
                ),
            ], md=8 , className="mx-auto"),
        ]),

        dbc.Row([
            dbc.Col([
                dbc.Card(
                    dbc.CardBody([
                        html.H4("Download", className="card-title text-center"),
                        html.P(
                            """
                            Raw data were downloaded from Climate Data Store thorugh official Copernicus API (cdsapi).
                            
                            
                            """,
                            className="card-text"
                        ),

                    ]),
                    className="mb-4 shadow-sm"
                ),
            ], md=8 , className="mx-auto"),
        ]),

        dbc.Row([
            dbc.Col([
                dbc.Card(
                    dbc.CardBody([
                        html.H4("Variables", className="card-title text-center"),
                        html.P(
                            """
                            For the statistical methodologies used in downscaling, ensemble weighting, and seasonal verification, the following are mainly used:
                            """,
                            className="card-text"
                        ),
                        html.Ul([
                            html.Li("Sea Level Pressure (msl)"),
                            html.Li("Geopotential Height 500 hPa (z500)"),
                            html.Li("Temperature at 2 m (t2m)"),
                            html.Li("Total Precipitation (tp)"),
                        ])
                    ]),
                    className="mb-4 shadow-sm"
                ),
            ], md=8 , className="mx-auto"),
        ]),

        html.Div(style={"height": "40px"}), 
    ],
    fluid=True,
)
