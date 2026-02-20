from dash import html
import dash
import dash_bootstrap_components as dbc

dash.register_page(
    __name__,
    path="/whatsnext",
    name="What's Next",
    title="● What's Next ●"
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

layout = html.Div(
    [
        html.H2(
            "Upcoming work for the next six months",
            className="text-center mb-4",
            style={"color": "#003060"}
        ),

        html.P(
            """
            Overview of the key priorities we will focus on 
            before the end of the project (June 2026).
            """,
            className="text-center text-muted",
            style={"fontSize": "15px", "maxWidth": "900px", "margin": "0 auto 30px auto"}
        ),

        # --- CARDS LIST ---
        dbc.Container([

            # 1 — New 2.5 km resolution
            html.Div(
                [
                    html.Strong("New 2.5km resolution"), html.Br(),
                    "Adaptation of the procedures to the new 2.5-km resolution."
                ],
                style=CARD_STYLE
            ),

            # 2 — Verification reports
            html.Div(
                [
                    html.Strong("Verification reports"), html.Br(),
                    "Comparing the downscaled seasonal forecasts using analogues "
                    "and machine-learning-based downscaling techniques."
                ],
                style=CARD_STYLE
            ),

            # 3 — Updating the SClimWare viewer
            html.Div(
                [
                    html.Strong("Updating SClimWare viewer"), html.Br(),
                    "Enhancing the spatial resolution of precipitation and temperature "
                    "forecasts and integrating additional seasonal forecast systems."
                ],
                style=CARD_STYLE
            ),

            # 4 — Workflow consolidation
            html.Div(
                [
                    html.Strong("Workflow consolidation"), html.Br(),
                    "Ensuring the weighting methodology is operational, reviewed, "
                    "and all pending components are finalised."
                ],
                style=CARD_STYLE
            ),

            # 5 — Visualisation
            html.Div(
                [
                    html.Strong("Visualisation"), html.Br(),
                    "Improved maps, interactive dashboards, and enhanced UI elements."
                ],
                style=CARD_STYLE
            ),

            # 6 — Basins analysis
            html.Div(
                [
                    html.Strong("Basins diagnosis"), html.Br(),
                    "Integration of hydrological basin analyses to strengthen evaluation."
                ],
                style=CARD_STYLE
            ),

            # 7 — Documentation & final milestone
            html.Div(
                [
                    html.Strong("Documentation"), html.Br(),
                    "Delivering the final milestone report with consolidated results "
                    "as the project approaches June 2026."
                ],
                style=CARD_STYLE
            ),

        ], style={"maxWidth": "850px"}),

    ],
    style={"padding": "40px"}
)
