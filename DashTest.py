# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 14:53:08 2019

@author: sainath.dutkar
"""
import base64
import datetime
import io
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
        html.H3("New Jersey Courts Content Manager"),
    dcc.Tabs(id="tabs", children=[
        dcc.Tab(label='Upload a File', children=[
            html.Div([
                  dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '50%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=False
                ),
        html.H6('Please enter the file details'),
        html.Table([
                html.Tr([
                        html.Td([html.Label('Sequenece Number')]),
                        html.Td([dcc.Input(id='DocSeq',type='text')])
                        ]),
                html.Tr([
                        html.Td([html.Label('Type Code')]),
                        html.Td([dcc.Input(id='DocType',type='text')])
                        ]),
                html.Tr([
                        html.Td([html.Label('Venue ID')]),
                        html.Td([dcc.Input(id='VenueID',type='text')])
                        ]),
                html.Tr([
                        html.Td([html.Label('Court Year')]),
                        html.Td([dcc.Input(id='Year',type='text')])
                        ]),
                html.Tr([
                        html.Td([html.Label('Privacy Code')]),
                        html.Td([dcc.Input(id='PrvCode',type='text')])
                        ]),
                html.Tr([
                        html.Td([html.Label('Privacy Reason')]),
                        html.Td([dcc.Input(id='PrvReason',type='text')])
                        ]),
                html.Tr([
                        html.Td([html.Label('Document Code')]),
                        html.Td([dcc.Input(id='DocCode',type='text')])
                        ]),
                html.Tr([
                        html.Td([html.Label('Description')]),
                        html.Td([dcc.Input(id='Desc',type='text')])
                        ]),
                html.Tr([
                        html.Td([html.Label('Mime Type')]),
                        html.Td([dcc.Input(id='MType',type='text')])
                        ]),
                html.Tr([
                        html.Td([html.Label('Efiling Court Division')]),
                        html.Td([dcc.Input(id='CourtDiv',type='text')])
                        ]),
                html.Tr([
                        html.Td([html.Label('Item Type')]),
                        html.Td([dcc.Input(id='ItemType',type='text')])
                        ]),
                ]),
        html.Br(),
        html.Button(id='submit-button', n_clicks=0, children='Upload File'),
        html.Div(id='outputLable')
            
             
            ])
        ]),
        dcc.Tab(label='Retrieve Files', children=[
                dcc.Graph(
                    id='example-graph-1',
                    figure={
                        'data': [
                            {'x': [1, 2, 3], 'y': [1, 4, 1],
                                'type': 'bar', 'name': 'SF'},
                            {'x': [1, 2, 3], 'y': [1, 2, 3],
                             'type': 'bar', 'name': u'Montréal'},
                        ]
                    }
                )
        ]),
        dcc.Tab(label='Merge Files', children=[
                dcc.Graph(
                    id='example-graph-2',
                    figure={
                        'data': [
                            {'x': [1, 2, 3], 'y': [2, 4, 3],
                                'type': 'bar', 'name': 'SF'},
                            {'x': [1, 2, 3], 'y': [5, 4, 3],
                             'type': 'bar', 'name': u'Montréal'},
                        ]
                    }
                )
        ]),
    ])
])


@app.callback(Output('outputLable', 'children'),
              [Input('upload-data', 'contents')])
             # [State('upload-data', 'filename')])
def update_output(file_content):
   # if file_content is not None:
    #    content_type, content_string = file_content.split(',')
     #   decoded = base64.b64decode(content_string)
        
    return file_content
        



if __name__ == '__main__':
    app.run_server(debug=True)