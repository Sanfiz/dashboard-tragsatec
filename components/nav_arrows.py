from dash import html, dcc
import dash_bootstrap_components as dbc

AEMET_BLUE = "#003060"

def nav_arrows(prev_href=None, next_href=None, prev_text="Back", next_text="Next"):
    buttons = []

    button_style = {
        "backgroundColor": "rgba(0, 48, 96, 0.08)",  # azul AEMET MUY suave
        "color": AEMET_BLUE,
        "border": f"1px solid rgba(0,48,96,0.25)",
        "fontSize": "0.85rem",
        "padding": "6px 14px",
        "borderRadius": "20px",
        "backdropFilter": "blur(2px)",
        "transition": "all 0.2s ease-in-out",
    }

    hover_style = {
        "backgroundColor": "rgba(0, 48, 96, 0.20)",
        "border": f"1px solid rgba(0,48,96,0.35)",
    }

    # LEFT BUTTON
    if prev_href:
        buttons.append(
            dcc.Link(
                html.Button(
                    f"← {prev_text}",
                    style=button_style,
                    className="nav-arrow-btn",
                ),
                href=prev_href
            )
        )

    # RIGHT BUTTON
    if next_href:
        buttons.append(
            dcc.Link(
                html.Button(
                    f"{next_text} →",
                    style=button_style,
                    className="nav-arrow-btn",
                ),
                href=next_href
            )
        )

    return html.Div(
        buttons,
        style={
            "display": "flex",
            "justifyContent": "center",
            "marginTop": "110px",
            "marginBottom": "20px",
            "gap": "15px",
        }
    )
