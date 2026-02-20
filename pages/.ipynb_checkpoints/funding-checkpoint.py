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
        html.H2("Financiación", className="text-center mb-4"),

        html.P(
            """
            Este proyecto está financiado mediante una encomienda entre
            Tragsatec y la Agencia Estatal de Meteorología (AEMET).
            """,
            className="text-center text-muted",
            style={"fontSize": "14px", "maxWidth": "900px", "margin": "0 auto"},
        ),

        html.Br(),

 

        html.Div(style={"height": "50px"})
    ]
)
