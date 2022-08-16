import dash_bootstrap_components as dbc
import dash_html_components as html
from dash import Dash 
import base64

"""
Dashboard for HOC Parliamentary Debates

- app.py
- assets/images/
"""
base_path = "./assets/images/"
#Using direct image file path
IMG_LIST = ["Covid-19 2021", "Covid-19 2020","co_occurence_covid_20","co_occurence_covid_21","wordcloud_covid",
"wordcloud_ireland","government_21","virus_21","top_semantic_change","least_semantic_change"]

# Using base64 encoding and decoding
def b64_image(image_filename):
    with open(image_filename, 'rb') as f:
        image = f.read()
    return 'data:image/png;base64,' + base64.b64encode(image).decode('utf-8')


app = Dash(external_stylesheets=[dbc.themes.COSMO])
server = app.server

app.layout = html.Div([
   
    html.H1(id='Title1',children='HOC Hansard Parliament',style={'text-align':'center'}),
    
    html.Div( className="row", children=[
        html.Div(html.Img(src=b64_image(base_path+IMG_LIST[0]+".png"), style={'height':'100%', 'width':'110%'}), style=dict(width='50%') ),
        html.Div(html.Img(src=b64_image(base_path+IMG_LIST[1]+".png"), style={'height':'100%', 'width':'110%'}), style=dict(width='50%') )],
        style=dict(display='flex')
    ),
    html.Br(),

    html.Div( className="row", children=[
        html.Div(html.Img(src=b64_image(base_path+IMG_LIST[2]+".png"), style={'height':'100%', 'width':'110%'}), style=dict(width='50%') ),
        html.Div(html.Img(src=b64_image(base_path+IMG_LIST[3]+".png"), style={'height':'100%', 'width':'110%'}), style=dict(width='50%') )],
        style=dict(display='flex')
    ),
    html.Br(),

    html.Div( className="row", children=[
        html.Div(html.Img(src=b64_image(base_path+IMG_LIST[4]+".png"), style={'height':'100%','margin-left': 150, 'width':'70%'}), style=dict(width='50%') ),
        html.Div(html.Img(src=b64_image(base_path+IMG_LIST[5]+".png"), style={'height':'100%','margin-left': 150, 'width':'70%'}), style=dict(width='50%') )],
        style=dict(display='flex')
    ),
    html.Br(),


    html.Div( className="row", children=[
        html.Div(html.Img(src=b64_image(base_path+IMG_LIST[6]+".png"), style={'height':'100%','margin-left': 150, 'width':'70%'}), style=dict(width='50%') ),
        html.Div(html.Img(src=b64_image(base_path+IMG_LIST[7]+".png"), style={'height':'100%','margin-left': 150, 'width':'70%'}), style=dict(width='50%') )],
        style=dict(display='flex')
    ),
    html.Br(),
    html.Br(),

    html.Div( className="row", children=[
        html.Div(html.Img(src=b64_image(base_path+IMG_LIST[8]+".png"), style={'height':'100%','margin-left': 150, 'width':'70%'}), style=dict(width='50%') ),
        html.Div(html.Img(src=b64_image(base_path+IMG_LIST[9]+".png"), style={'height':'100%', 'margin-left': 150, 'width':'70%'}), style=dict(width='50%') )],
        style=dict(display='flex')
    ),
    html.Br(),

    html.Div( className="row", children=[
        html.Iframe(
            src="https://shubh802.github.io/hoc/lda.html",
            style={"height": "1067px",'margin-left': 100, "width": "90%"},
        )
    ]
    ),


])

if __name__ == "__main__":
    app.run_server(debug=True)