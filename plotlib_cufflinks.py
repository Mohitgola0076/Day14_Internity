'''
                            # Getting Started with Plotly in Python : 
                            
The plotly Python library is an interactive, open-source plotting library that supports over 40 unique chart types covering a wide 
range of statistical, financial, geographic, scientific, and 3-dimensional use-cases.

Built on top of the Plotly JavaScript library (plotly.js), plotly enables Python users to create beautiful interactive web-based 
visualizations that can be displayed in Jupyter notebooks, saved to standalone HTML files, or served as part of pure Python-built 
web applications using Dash. The plotly Python library is sometimes referred to as "plotly.py" to differentiate it from the 
JavaScript library. 
'''

                            # Installation : 
                            
plotly may be installed using pip:

$ pip install plotly==5.0.0
or conda:

$ conda install -c plotly plotly=5.0.0
This package contains everything you need to write figures to standalone HTML files.

            # Example : 
import plotly.graph_objects as go
fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
fig.write_html('first_figure.html', auto_open=True)


                # Plotly chart in Dash : 
  
  
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

app = dash.Dash(__name__)

app.layout = html.Div([
    html.P("Color:"),
    dcc.Dropdown(
        id="dropdown",
        options=[
            {'label': x, 'value': x}
            for x in ['Gold', 'MediumTurquoise', 'LightGreen']
        ],
        value='Gold',
        clearable=False,
    ),
    dcc.Graph(id="graph"),
])

@app.callback(
    Output("graph", "figure"), 
    [Input("dropdown", "value")])
def display_color(color):
    fig = go.Figure(
        data=go.Bar(y=[2, 3, 1], marker_color=color))
    return fig

app.run_server(debug=True)



                # Plotly & Cufflinks : 
'''
Plotly is an open-source and browser-based graphing library which facilitates interactive plotting.  The library is available for 
a number of programming languages such as Python, R, MATLAB, Perl, Julia, Arduino, and REST, among others.
Cufflinks is another library that connects the Pandas data frame with Plotly enabling users to create visualizations directly 
from Pandas. The library binds the power of Plotly with the flexibility of Pandas for easy plotting.
'''

        # Installing Cufflinks
To install cufflinks type and execute the following commands

pip install cufflinks


                    # Importing necessary libraries : 
For iplots, you might want to stick to using Jupyter Notebook as it has great support for it.

import plotly
import cufflinks as cf
import pandas as pd
import numpy as np

#Enabling the offline mode for interactive plotting locally
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot
init_notebook_mode(connected=True)
cf.go_offline()

#To display the plots
%matplotlib inline


                        # Importing The Dataset : 
Consider a simple dataset of random numbers. You can either create your own download the same sample used in the below examples by clicking here.

data = pd.read_csv("sample_data.csv")


                        # Creating Interactive Plots : 
Let’s do a simple plot of the numerical features in the dataset which are columns A, B and C.

data[['A','B','C']].iplot()

