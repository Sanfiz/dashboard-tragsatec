from dash import html, register_page
from components.nav_arrows import nav_arrows



register_page(__name__, path="/downscaling/methodology", name="Downscaling Methodology")

layout = html.Div([

    html.H2(
        "Downscaling - Methodology",
        style={"textAlign": "center", "color": "#003060"}
    ),
    
    html.Div(style={"height": "22px"}),  
    # -----------------------------------------------------------------------------
    # INTRO
    html.P(
        """
        The precipitation downscaling algorithm developed at AEMET provides daily precipitation 
        over a high-resolution grid (5 km × 5 km, comprising a total of 20,945 grid cells) 
        covering peninsular Spain and the Balearic Islands. It does so by means of a set of 
        synoptic analogues to the target day (reference period 1981–1996), computed from 
        low-resolution atmospheric data from the ERA5 reanalysis, together with their associated 
        precipitation patterns. To characterise the target day, atmospheric data from seasonal 
        prediction systems are employed.
        """,
        style={"maxWidth": "900px", "margin": "0 auto 25px auto", "lineHeight": "1.6"}
    ),

    html.P(
        "The process is divided into two phases:",
        style={"maxWidth": "900px", "margin": "0 auto 25px auto"}
    ),

    # -----------------------------------------------------------------------------
    # 1. CALIBRATION PHASE
    html.H5(
        "1. Calibration phase",
        style={"textAlign": "center", "color": "#003060", "marginTop": "20px", "marginBottom": "15px"}
    ),

    html.Div([

            html.P([
                "a. A weather-type classification is performed using K-means clustering, identifying the ",
                html.Strong("reference synoptic database"),
                ". Similarity is computed from weighted Euclidean distances of standardised geostrophic wind components ",
                "at the surface and 500 hPa."
            ],
            style={"marginLeft": "40px","lineHeight": "1.55","marginBottom": "20px"}),


        html.P(
            """
            b. Each synoptic situation in the reference database is associated with a precipitation 
            pattern, which is then used to estimate precipitation for the target day.
            """,
            style={"marginLeft": "40px", "lineHeight": "1.55"}
        ),

        html.P(html.Strong("Datasets used:"), style={"marginLeft": "40px", "lineHeight": "1.55"}),

        html.Ul([
            html.Li("Daily atmospheric database (ERA5):"),
            html.Ul([
                html.Li("Geostrophic wind components (ug, vg) from MSL and T1000"),
                html.Li("Wind components at 500 hPa (u500, v500)")
            ], style={"paddingLeft": "60px"}),
            html.Li("Daily precipitation database (ROCÍO_IBEB)")
        ], style={"paddingLeft": "60px", "marginTop": "10px"}),


        html.Div(
            html.Img(
                src=f"/assets/imgs_downscaling/method_down_1.png",
                style={
                    "width": "70%",          
                    "display": "block",
                    "margin": "30px auto 10px auto",  # centrado 
                    "borderRadius": "10px"})
        ),


    html.Div(style={"height": "15px"}),  
        
    ], style={"maxWidth": "900px", "margin": "0 auto"}),

    # -----------------------------------------------------------------------------
    # 2. ESTIMATION PHASE
    

    html.H5(
        "2. Estimation phase",
        style={"textAlign": "center", "color": "#003060", "marginTop": "20px", "marginBottom": "15px"}
    ),

    html.Div([

        html.P(
            """
            The precipitation estimate for each grid cell is obtained from the weighted mean of the 
            precipitation associated with the most analogous synoptic situations in the reference 
            database, using similarity of geostrophic wind fields at surface and 500 hPa.
            """,
            style={"maxWidth": "900px", "margin": "0 auto 25px auto", "lineHeight": "1.6"}
        ),

        html.P(html.Strong("Datasets used:"), style={"marginLeft": "0px", "lineHeight": "1.55"}),

        html.Ul([
            html.Li("Daily atmospheric databases (C3S models):"),
            html.Ul([
                html.Li("Geostrophic wind components (ug, vg from MSL and T1000)"),
                html.Li("Wind components (u500, v500) at 500 hPa")
            ], style={"paddingLeft": "40px"})
        ], style={"paddingLeft": "10px", "marginTop": "10px"}),

        html.Div(
            html.Img(
                src=f"/assets/imgs_downscaling/method_down_2.png",
                style={
                    "width": "70%",          
                    "display": "block",
                    "margin": "30px auto 10px auto",  # centrado 
                    "borderRadius": "10px"})
        ),



        

    ], style={"maxWidth": "900px", "margin": "0 auto"}),

    # -----------------------------------------------------------------------------
    nav_arrows(
        prev_href=f"/downscaling",
        next_href=f"/downscaling/results",
        prev_text="Back to Downscaling Main",
        next_text="Go to Downscaling Results"
    )

], style={"padding": "40px"})
