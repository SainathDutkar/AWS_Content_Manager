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
from S3UploadTest import upload_fileTo_S3


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
                        html.Td([dcc.Input(id='DocSeq',type='text')]),
                        html.Td([html.Label('Type Code')]),
                        html.Td([dcc.Input(id='DocType',type='text')])
                        ]),
     
                html.Tr([
                        html.Td([html.Label('Venue ID')]),
                        html.Td([dcc.Input(id='VenueID',type='text')]),
                        html.Td([html.Label('Court Year')]),
                        html.Td([dcc.Input(id='Year',type='text')])
                        ]),
             
                html.Tr([
                        html.Td([html.Label('Privacy Code')]),
                        html.Td([dcc.Input(id='PrvCode',type='text')]),
                        html.Td([html.Label('Privacy Reason')]),
                        html.Td([dcc.Input(id='PrvReason',type='text')])
                        ]),
                
                html.Tr([
                        html.Td([html.Label('Document Code')]),
                        html.Td([dcc.Input(id='DocCode',type='text')]),
                         html.Td([html.Label('Description')]),
                        html.Td([dcc.Input(id='Desc',type='text')])
                        ]),
              
                html.Tr([
                        html.Td([html.Label('Mime Type')]),
                        html.Td([dcc.Input(id='MType',type='text')]),
                        html.Td([html.Label('Efiling Court Division')]),
                        html.Td([dcc.Input(id='CourtDiv',type='text')])
                        ]),
                html.Tr([
                        html.Td([html.Label('Item Type')]),
                        html.Td([dcc.Input(id='ItemType',type='text')])
                       
                        ]),
                html.Tr([
                         html.Td([html.Button(id='submit-button', n_clicks=0, children='Upload File')])
                        ])
                ]),
        html.Br(),
        html.Div(id='outputLable'),
        html.Div(id='my-div')
            
             
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



global fileData


"""
@app.callback(Output('outputLable', 'children'),
              [Input('upload-data', 'contents')]
              )
             # [State('upload-data', 'filename')])
def update_output(file_content):
    decoded = ''
    fileContent = ''
    if file_content is not None:    
        content_type, content_string = file_content.split(',')
        decoded = base64.b64decode(content_string)
        fileContent = decoded
        
    return str(fileContent)
"""

@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='submit-button',component_property= 'n_clicks')],
     [dash.dependencies.State(component_id='upload-data', component_property='filename'),
      dash.dependencies.State(component_id='upload-data', component_property='contents'),
      dash.dependencies.State(component_id='DocSeq', component_property='value'),
      dash.dependencies.State(component_id='DocType', component_property='value'),
      dash.dependencies.State(component_id='VenueID', component_property='value'),
      dash.dependencies.State(component_id='Year', component_property='value'),
      dash.dependencies.State(component_id='PrvCode', component_property='value'),
      dash.dependencies.State(component_id='PrvReason', component_property='value'),
      dash.dependencies.State(component_id='DocCode', component_property='value'),
      dash.dependencies.State(component_id='Desc', component_property='value'),
      dash.dependencies.State(component_id='MType', component_property='value'),
      dash.dependencies.State(component_id='CourtDiv', component_property='value'),
      dash.dependencies.State(component_id='ItemType', component_property='value'),
    ]
)
def update_output_div(n_clicks,fileName,fileData, input1,input2,input3,input4,input5,input6,input7,input8,input9,input10,input11):
    
    data = fileData.encode("utf8").split(b";base64,")[1]
    Base64data = base64.decodebytes(data)
    fileData = str(Base64data)
    fileObj = fileName[:-4]
    upload_fileTo_S3(fileName,'njcpoc',fileObj,input1,input2,input3,input4,input5,input6,input7,input8,input9,input10,input11)
    if n_clicks is not None:
        return str("Completed Successfully")
    
        #return str(fileName+input1+input2+input3+input4+input5+input6+input7+input8+input9+input10+input11)
        



if __name__ == '__main__':
    app.run_server(debug=True)
