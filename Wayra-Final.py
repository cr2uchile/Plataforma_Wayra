#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 11:14:01 2021

@author: sebastian
"""

import dash
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_extensions import Download
from dash_extensions.snippets import send_data_frame
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import os as os
import numpy as np
import datetime
import base64
from datetime import date
from datetime import timedelta
from textwrap import dedent
from datetime import datetime as dt


image_filename_cr2 = 'logo_footer110.png'
encoded_image_cr2 = base64.b64encode(open(image_filename_cr2, 'rb').read()).decode('ascii')
image_filename_DMC = 'logoDMC_140x154.png'
encoded_image_DMC = base64.b64encode(open(image_filename_DMC, 'rb').read()).decode('ascii')
image_filename_tololo = 'wayra.png'
encoded_image_tololo = base64.b64encode(open(image_filename_tololo, 'rb').read()).decode('ascii')
image_filename_cr2_celeste = 'cr2_celeste.png'
encoded_image_cr2_celeste = base64.b64encode(open(image_filename_cr2_celeste, 'rb').read()).decode('ascii')
image_filename_GWA = 'gaw_logo.png'
encoded_image_GWA = base64.b64encode(open(image_filename_GWA, 'rb').read()).decode('ascii')
image_filename_GWA_center = 'GAW_index.png'
encoded_image_GWA_center = base64.b64encode(open(image_filename_GWA_center, 'rb').read()).decode('ascii')
image_filename_rapa_nui = 'RapaNui.png'
encoded_image_rapa_nui = base64.b64encode(open(image_filename_rapa_nui, 'rb').read()).decode('ascii')

############################################  Mapas############################

Rapa_Nui = pd.DataFrame(data={"lat": [-27.13], "lon":[-109.35]})

fig = px.scatter_mapbox(Rapa_Nui, lat="lat", lon="lon",
                        color_discrete_sequence=["blue"], zoom=10)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

Tololo = pd.DataFrame(data={"lat": [-30.169], "lon":[-70.804]})

fig2 = px.scatter_mapbox(Tololo, lat="lat", lon="lon",
                        color_discrete_sequence=["blue"], zoom=5)
fig2.update_layout(mapbox_style="open-street-map")
fig2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}], title='Wayra') 
mathjax = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML'
####### opciones matemáticas
app.scripts.append_script({ 'external_url' : mathjax })

navbar = dbc.Navbar(
    dbc.Container([
        dbc.Col([
            html.A([       
            html.Img(src = 'data:image/png;base64,{}'.format(encoded_image_tololo), 
                                                           style = {"height":"50px"})], 
                                                           href = 'http://www.cr2.cl/',
                                                           style = {
                                                                    'display':'inline-block'},
                                                                    ),        
#            html.A([
#            dbc.NavbarBrand("Wayra", style = {'font-size': '22pt',
#                                      'font-family': 'times',
#                                      'color':'white', 'display':'inline-block'})],
#                style={'display':'inline-block'}),
            html.A([       
            html.Img(src = 'data:image/png;base64,{}'.format(encoded_image_cr2_celeste), 
                                                           style = {"height":"50px"})], 
                                                           href = 'http://www.cr2.cl/',
                                                           style = {'margin-left':'20px',
                                                                    'display':'inline-block'},
                                                           ),
                                                        
            html.A([
            html.Img(src = 'data:image/png;base64,{}'.format(encoded_image_DMC), 
                                                           style = {"height":"50px"})],
                                                           href = 'http://www.meteochile.gob.cl/PortalDMC-web',
                                                           style = {'margin-left':'20px',
                                                                    'display':'inline-block'}),
           html.A([
           html.Img(src='data:image/png;base64,{}'.format(encoded_image_GWA),
                                                        style = {"height":"50px"})],
                                                        href = 'https://www.wmo.int/pages/prog/arep/gaw/gaw_home_en.html',
                                                        style = {'margin-left':'20px',
                                                                 'display':'inline-block'})
            ], style={'display':'inline-block'}, xs=12, sm=12, md=4, lg=4, xl=4),
        dbc.Col([
            html.Div([
            html.P("Language:" , style={'font-size':'15pt','color': 'white', 'margin-top': '30px', 'text-align': 'center'})], style={'display':'inline-block'}),
            html.Div([
            daq.ToggleSwitch(
                id='Switch_Lang',
                className='SwicthLang',
                value=True,
                )], style={'display':'inline-block','margin-left':'2%'})
            ], style={'margin-left':'20%'},xs=10, sm=12, md=4, lg=4, xl=4)
    ]), color="#1766a0")



content =  html.Div(id='tabs-content', style={'background-color':'#f6f6f6'})

@app.callback(Output('tabs-content', 'children'),
              Input('Switch_Lang', 'value'))
def Web_Language(Switch_Lang):
    if Switch_Lang==True:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([
                        
                    html.H2(html.A("Rapa Nui Dashboard",href = 'https://rapanui.wayra.cr2.cl/' ), style={'margin-left':'10px',
                                                                                     'text-align': 'center','font-family': 'Abel','font-size': '22px','color': '#0668a1','backgroundColor': '#f6f6f6'}),
                    dcc.Graph(figure=fig, style={'height':'auto', 'width':'75%', 'margin-left':'12%'})
                        ,
                        html.H2(html.A("Tololo Dashboard", href='https://tololo.wayra.cr2.cl/') ,style={'margin-left':'10px',
                                                                                     'text-align': 'center','font-family': 'Abel','font-size': '22px','color': '#0668a1','backgroundColor': '#f6f6f6'}),
                        dcc.Graph(figure=fig2, style={'height':'auto', 'width':'75%', 'margin-left':'12%'})],
                        md=10, lg={'size': 6,  "offset": 0, 'order': 1}),
                    dbc.Col([
                        html.H1("Global Atmospheric Watch (GAW) stations in Chile", style={'margin-left':'6%',
                                                                                     'text-align': 'center','font-family': 'Abel','font-size': '28px','color': '#0668a1'}),
            dcc.Markdown(dedent(f'''
                 La Organización Meteorológica Mundial (WMO) estableció el programa de Vigilancia Atmosférica Global (GAW) para evaluar, cuantificar y proporcionar una base para predecir cambios en la composición atmosférica en 1989. Actualmente,
                 la red de vigilancia de la GAW consta de 30 estaciones GAW totalmente equipadas y aprox. 400 estaciones regionales, incluidas las estaciones colaboradoras,
                 que recopilan datos sobre gases de efecto invernadero, aerosoles, química de las precipitaciones, etc. Estos datos se recopilan en centros de datos y se ponen a disposición del público en Internet: https://gawsis.meteoswiss.ch/GAWSIS/#/                '''), style={'margin-left':'6%'})
          ,html.Img(src='data:image/png;base64,{}'.format(encoded_image_GWA_center),style={'width':'100%', 'margin-left':'6%'}),
          dcc.Markdown(dedent(f'''
                               Como parte del programa subregional para el cono sur de América del Sur, se instalaron tres estaciones en Chile bajo los auspicios de la GAW y la Oficina Meteorológica de Chile  (DMC) a mediados de 1990. Así fueron instalados, un dispositivo de sondeo O3 en Rapa Nui (27ºS, 109ºW, 51 m s.n.m.); un monitor de superficie de O3, sensores meteorológicos y de radiación en Cerro Tololo (30ºS, 70ºW, 2200 m s.n.m.); y un radiómetro multibanda en Valdivia (39.8ºS, 73ºW, 10 m s.n.m.).
                               Desafortunadamente, la estación de Valdivia fue destruida en un incendio a mediados de 2000.
                               Cerro Tololo y Rapa Nui se han mantenido en funcionamiento de manera bastante continua desde mediados de la década de 1990, acercándose hoy a un récord de 25 años cada uno. Además, se ha ampliado Cerro Tololo. Actualmente, los monitores de metano, dióxido de carbono, monóxido de carbono, radiación y aerosoles están operando allí. Las publicaciones que han proporcionado análisis de estos datos se enumeran a continuación.                              Principal Investigators: Laura Gallardo (CR2, DGF, Universidad de Chile) and Carmen Vega (DMC)
                              Site manager: Francisca Muñoz (CR2)
                              Data Scientists: Camilo Menares (CR2), Charlie Opazo (CR2, DGF) and Sebastián Villalón (CR2)
                              In this joint platform between the Center for Climate and Resilience Research and the Chilean Weather Office, we present Tololo and Rapa Nui data, and provide statistical analyses including decadal trends. This platform is complementary to designated data providers within GAW.
                '''), style={'margin-left':'6%'}),
                html.H1("Publicaciones", style={'text-align': 'center','font-family': 'Abel','font-size': '28px','color': '#0668a1'}),
                dcc.Markdown(dedent(f'''
                    
                    a) **Rapa Nui**
                    
                             
                    Gallardo, L., Henríquez, A., Thompson, A. M., Rondanelli, R., Carrasco, J., Orfanoz-Cheuquelaf, A., et al. (2016). The first twenty years (1994-2014) of ozone soundings from Rapa Nui (27°S, 109°W, 51m a.s.l.). Tellus, Ser. B Chem. Phys. Meteorol. 68, 29484. doi:10.3402/tellusb.v68.29484.
                    
                    Calderón, J. and Fuenzalida, H. 2014. Radiación ultravioleta en Isla de Pascua: factores climáticos y ozono total. Stratus 2, 8. Revista de la Dirección Meteorológica de Chile. ISSN 0719-4544
                    
                    
                    b) **Tololo**
                
                    Anet, G. J., Steinbacher, M., Gallardo, L., Velásquez Álvarez, A. P., Emmenegger, L., and Buchmann, B. (2017). Surface ozone in the Southern Hemisphere: 20 years of data from a site with a unique setting in El Tololo, Chile. Atmos. Chem. Phys. 17, 6477–6492. doi:10.5194/acp-17-6477-2017.
                    
                    Gallardo, L., Carrasco, J., and Olivares, G. (2000). An analysis of ozone measurements at Cerro Tololo (30°S, 70°W, 2200 m.a.s.l.) in Chile. Tellus, Ser. B Chem. Phys. Meteorol. 52, 50–59. doi:10.3402/tellusb.v52i1.16081.
                    
                    Kalthoff, N., Bischoff-Gauß, I., Fiebig-Wittmaack, M., Fiedler, F., Thürauf, J., Novoa, E., et al. (2002). Mesoscale wind regimes in Chile at 30°S. J. Appl. Meteorol. 41, 953–970. doi:10.1175/1520-0450(2002)041<0953:MWRICA>2.0.CO;2.
                    
                    Rondanelli, R., Gallardo, L., and Garreaud, R. D. (2002). Rapid changes in ozone mixing ratios at Cerro Tololo (30°10′S, 70°48′W, 2200 m) in connection with cutoff lows and deep troughs. J. Geophys. Res. Atmos. 107, ACL 6-1-ACL 6-15. doi:10.1029/2001JD001334.
                        
                    
                    c) **Valdivia**
                    
                    Diaz, S., Camilión, C., Deferrari, G., Fuenzalida, H., Armstrong, R., Booth, C., et al. (2006). Ozone and UV Radiation over Southern South America: Climatology and Anomalies. Photochem. Photobiol. 82, 834–843. doi:https://doi.org/10.1562/2005-09-26-RA-697.

                    Huovinen, P., Gómez, I., and Lovengreen, C. (2006). A Five-year Study of Solar Ultraviolet Radiation in Southern Chile (39° S): Potential Impact on Physiology of Coastal Marine Algae? Photochem. Photobiol. 82, 515–522. doi:https://doi.org/10.1562/2005-07-05-RA-601.

                    Lovengreen, C., Fuenzalida, H., and Villanueva, L. (2000). Ultraviolet solar radiation at Valdivia, Chile (39.8°S). Atmos. Environ. 34, 4051–4061. doi:10.1016/S1352-2310(00)00227-2.
                
               '''), style={'margin-left':'%6'}) 
                        ], md=10, lg={'size': 6,  "offset": 0, 'order': 0}),
                   
                    ])
                ], style={'background-color':'#f6f6f6'})
            
            ]
    if Switch_Lang==False:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([
                        
                    html.H2(html.A("Rapa Nui Dashboard",href = 'https://rapanui.wayra.cr2.cl/' ), style={'margin-left':'10px',
                                                                                     'text-align': 'center','font-family': 'Abel','font-size': '22px','color': '#0668a1','backgroundColor': '#f6f6f6'}),
                    dcc.Graph(figure=fig, style={'height':'auto', 'width':'75%', 'margin-left':'12%'})
                        ,
                        html.H2(html.A("Tololo Dashboard", href='https://tololo.wayra.cr2.cl/') ,style={'margin-left':'10px',
                                                                                     'text-align': 'center','font-family': 'Abel','font-size': '22px','color': '#0668a1','backgroundColor': '#f6f6f6'}),
                        dcc.Graph(figure=fig2, style={'height':'auto', 'width':'75%', 'margin-left':'12%'})],
                        md=10, lg={'size': 6,  "offset": 0, 'order': 1}),
                    dbc.Col([
                        html.H1("Global Atmospheric Watch (GAW) stations in Chile", style={'margin-left':'6%',
                                                                                     'text-align': 'center','font-family': 'Abel','font-size': '28px','color': '#0668a1'}),
            dcc.Markdown(dedent(f'''
                 The World Meteorological Organization (WMO) established the Global Atmospheric Watch (GAW) program to assess, quantify and provide a basis for predicting changes in atmospheric composition in 1989. Currently,
                the GAW monitoring network consists of 30 fully equipped GAW stations, and ca. 400 regional stations, including contributing stations,
                that collect data on greenhouse gases, aerosols, precipitation chemistry, etc. These data are collected in data centers and made publically available over the internet: https://gawsis.meteoswiss.ch/GAWSIS/#/  '''), style={'margin-left':'6%'})
          ,html.Img(src='data:image/png;base64,{}'.format(encoded_image_GWA_center),style={'width':'100%', 'margin-left':'6%'}),
          dcc.Markdown(dedent(f'''
                               As part of the sub-regional program for the southern cone of South America, three stations were installed in Chile under the auspices of GAW and the Chilean Weather Office (In Spanish Dirección Meteorológica de Chile, DMC) by the mid-1990. Namely, an O3 sounding device on Rapa Nui (27ºS, 109ºW, 51 m a.s.l.); a surface O3 monitor, meteorological and radiation sensors at Cerro Tololo (30ºS, 70ºW, 2200 m a.s.l.); and a multiband radiometer at Valdivia (39.8ºS, 73ºW, 10 m a.s.l.). 
                              Unfortunately, the Valdivia station was destroyed in a fire in the mid-2000. 
                              Cerro Tololo and Rapa Nui have been kept in operation rather continuously since the mid 1990’s, approaching today a 25-year record each. Moreover, Cerro Tololo has been expanded. Presently, methane, carbon dioxide, carbon monoxide, radiation and aerosol monitors are operating there. Publications that have provided analyses of these data are listed below.
                              Principal Investigators: Laura Gallardo (CR2, DGF, Universidad de Chile) and Carmen Vega (DMC)
                              Site manager: Francisca Muñoz (CR2)
                              Data Scientists: Camilo Menares (CR2), Charlie Opazo (CR2, DGF) and Sebastián Villalón (CR2)
                              In this joint platform between the Center for Climate and Resilience Research and the Chilean Weather Office, we present Tololo and Rapa Nui data, and provide statistical analyses including decadal trends. This platform is complementary to designated data providers within GAW.
                '''), style={'margin-left':'6%'}),
                html.H1("Publicaciones", style={'text-align': 'center','font-family': 'Abel','font-size': '28px','color': '#0668a1'}),
                dcc.Markdown(dedent(f'''
                    
                    
                    a) **Rapa Nui**
                    
                             
                    Gallardo, L., Henríquez, A., Thompson, A. M., Rondanelli, R., Carrasco, J., Orfanoz-Cheuquelaf, A., et al. (2016). The first twenty years (1994-2014) of ozone soundings from Rapa Nui (27°S, 109°W, 51m a.s.l.). Tellus, Ser. B Chem. Phys. Meteorol. 68, 29484. doi:10.3402/tellusb.v68.29484.
                    
                    Calderón, J. and Fuenzalida, H. 2014. Radiación ultravioleta en Isla de Pascua: factores climáticos y ozono total. Stratus 2, 8. Revista de la Dirección Meteorológica de Chile. ISSN 0719-4544
                    
                    
                    b) **Tololo**
                
                    Anet, G. J., Steinbacher, M., Gallardo, L., Velásquez Álvarez, A. P., Emmenegger, L., and Buchmann, B. (2017). Surface ozone in the Southern Hemisphere: 20 years of data from a site with a unique setting in El Tololo, Chile. Atmos. Chem. Phys. 17, 6477–6492. doi:10.5194/acp-17-6477-2017.
                    
                    Gallardo, L., Carrasco, J., and Olivares, G. (2000). An analysis of ozone measurements at Cerro Tololo (30°S, 70°W, 2200 m.a.s.l.) in Chile. Tellus, Ser. B Chem. Phys. Meteorol. 52, 50–59. doi:10.3402/tellusb.v52i1.16081.
                    
                    Kalthoff, N., Bischoff-Gauß, I., Fiebig-Wittmaack, M., Fiedler, F., Thürauf, J., Novoa, E., et al. (2002). Mesoscale wind regimes in Chile at 30°S. J. Appl. Meteorol. 41, 953–970. doi:10.1175/1520-0450(2002)041<0953:MWRICA>2.0.CO;2.
                    
                    Rondanelli, R., Gallardo, L., and Garreaud, R. D. (2002). Rapid changes in ozone mixing ratios at Cerro Tololo (30°10′S, 70°48′W, 2200 m) in connection with cutoff lows and deep troughs. J. Geophys. Res. Atmos. 107, ACL 6-1-ACL 6-15. doi:10.1029/2001JD001334.
                        
                    
                    c) **Valdivia**
                    
                    Diaz, S., Camilión, C., Deferrari, G., Fuenzalida, H., Armstrong, R., Booth, C., et al. (2006). Ozone and UV Radiation over Southern South America: Climatology and Anomalies. Photochem. Photobiol. 82, 834–843. doi:https://doi.org/10.1562/2005-09-26-RA-697.

                    Huovinen, P., Gómez, I., and Lovengreen, C. (2006). A Five-year Study of Solar Ultraviolet Radiation in Southern Chile (39° S): Potential Impact on Physiology of Coastal Marine Algae? Photochem. Photobiol. 82, 515–522. doi:https://doi.org/10.1562/2005-07-05-RA-601.

                    Lovengreen, C., Fuenzalida, H., and Villanueva, L. (2000). Ultraviolet solar radiation at Valdivia, Chile (39.8°S). Atmos. Environ. 34, 4051–4061. doi:10.1016/S1352-2310(00)00227-2.
               '''), style={'margin-left':'%6'}) 
                        ], md=10, lg={'size': 6,  "offset": 0, 'order': 0}),
                   
                    ])
                ], style={'background-color':'#f6f6f6'})
            
            ]                       
    
app.layout = html.Div(
    [navbar,
     content]
)

if __name__ == '__main__':
    app.run_server(debug=True, port=8888)
