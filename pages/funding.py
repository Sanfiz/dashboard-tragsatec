import dash
from dash import html

dash.register_page(
    __name__,
    path="/funding",
    name="Funding",
    title="● Funding ●",
)

layout = html.Div(
    [
        html.H6("Funding", className="text-center mb-4"),

        html.Div(
            [
                html.P(
                    "This project is funded through a service contract in which "
                    "Tragsatec acts as a subcontractor to the Spanish Met Service (AEMET).",
                    className="text-center text-muted",
                ),
                html.Br(),

                html.P(
                    "AEMET leads the work within the framework of seasonal forecasting, which is part of the Climate Evaluation and Modelling Area.",
                    className="text-center text-muted",
                ),
                html.Br(),

                html.P(
                    "The service contract runs until summer 2026.",
                    className="text-center text-muted",
                ),
            ],
            style={
                "fontSize": "14px",
                "maxWidth": "900px",
                "margin": "0 auto",
                "lineHeight": "1.6",
            },
        ),

        html.Div(style={"height": "50px"})
    ]
)
