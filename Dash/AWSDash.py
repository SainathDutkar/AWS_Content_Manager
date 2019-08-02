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
from UploadtoS3 import upload_file
from getFilesAPI import getDocNames
from downloadS3 import  download_S3_file
from MergeFiles import merge_S3_files


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
        html.Div([html.H3("New Jersey Courts Content Manager")], style={'width':'75%', 'margin':25, 'textAlign': 'center'}),
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
            'width': '40%',
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
                html.H6('Enter the following details'),
                html.Table([
                html.Tr([
                        html.Td([html.Label('Sequenece Number')]),
                        html.Td([dcc.Input(id='RetSeq',type='text')]),
                        html.Td([html.Label('Venue ID')]),
                        html.Td([dcc.Input(id='RetVenue',type='text')])
                        ]),
                html.Tr([
                        html.Td([html.Label('Court Year')]),
                        html.Td([dcc.Input(id='RetYear',type='text')]),
                        html.Td([html.Label('Type Code')]),
                        html.Td([dcc.Input(id='RetType',type='text')])
                        ]),
                html.Tr([
                         html.Td([html.Button(id='Get_Files', n_clicks=0, children='Get Files Details')])
                        ])
                ]),
                
                html.Div(id='FilesData',children='Enter a value and press submit'),
             
                html.H6("Enter the information to download the document"),
                
                html.Table([
                html.Tr([
                        html.Td([html.Label('S3 Object Key')]),
                        html.Td([dcc.Input(id='s3Obj',type='text')]),
                        html.Td([html.Label('S3 Bucket Name')]),
                        html.Td([dcc.Input(id='s3Bucket',type='text')])
                        ]),
                html.Tr([
                         html.Td([html.Button(id='download_Files', n_clicks=0, children='Download File')])
                        ])
                ]),
                html.Div(id='downloadData')
    
        ]),
        dcc.Tab(label='Merge Files', children=[
                
                html.H6('Enter Document name and S3 Bucket Name to Merge the files'),
                html.Table([
                html.Tr([
                        html.Td([html.Label('Document 1')]),
                        html.Td([dcc.Input(id='MergeDoc1',type='text')]),
                        html.Td([html.Label('Dcoument 2')]),
                        html.Td([dcc.Input(id='MergeDoc2',type='text')])
                        ]),
                html.Tr([
                        html.Td([html.Label('S3 Bucket Name')]),
                        html.Td([dcc.Input(id='Bucket',type='text')])
                        ]),
                html.Tr([
                         html.Td([html.Button(id='MergeFiles', n_clicks=0, children='Merge Files')])
                        ])
                ]),
            html.Div(id='MergeOutput')
                
        ]),
    ])
])



global fileData

@app.callback(
                Output(component_id='FilesData', component_property='children'),
                [Input(component_id='Get_Files',component_property= 'n_clicks')],
                [dash.dependencies.State(component_id='RetSeq', component_property='value'),
                dash.dependencies.State(component_id='RetVenue', component_property='value'),
               dash.dependencies.State(component_id='RetYear', component_property='value'),
               dash.dependencies.State(component_id='RetType', component_property='value')
               ])
def render_document(n_clicks,Seq,Venue, year,Rettype):
    parameters = {"VenueId":Venue, "DockCode":Rettype,"Year":year,"Seq":Seq}
    Docresults = getDocNames(parameters)
    result = "S3 Bucket Name : njcpoc  "+str(Docresults)
    return str(result)


@app.callback(
                Output(component_id='MergeOutput', component_property='children'),
                [Input(component_id='MergeFiles',component_property= 'n_clicks')],
                [dash.dependencies.State(component_id='MergeDoc1', component_property='value'),
                dash.dependencies.State(component_id='MergeDoc2', component_property='value')
               ])
def merge_document(n_clicks,doc1,doc2):
    print(doc1)
    print(doc2)
    mergeResult = merge_S3_files(doc1,doc2)
    return str(mergeResult)


@app.callback(
                Output(component_id='downloadData', component_property='children'),
                [Input(component_id='download_Files',component_property= 'n_clicks')],
                [dash.dependencies.State(component_id='s3Obj', component_property='value'),
                dash.dependencies.State(component_id='s3Bucket', component_property='value')
               ])
def download_document(n_clicks,S3Obj,S3Bucket):
    dwnresult = download_S3_file(S3Bucket,S3Obj)
    return str(dwnresult)




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
      dash.dependencies.State(component_id='ItemType', component_property='value')
    ]
)
def update_output_div(n_clicks,fileName,fileData, input1,input2,input3,input4,input5,input6,input7,input8,input9,input10,input11):
        
    if fileData is not None:
        print('already inside')
        data = fileData.encode("utf8").split(b";base64,")[1]
        Base64data = base64.decodebytes(data)
        fileData = str(Base64data)
        fileObj = fileName[:-4]
        upload_file(fileName,'njcpoc',fileObj,input1,input2,input3,input4,input5,input6,input7,input8,input9,input10,input11)
        returnResult = 'File Uploaded Successfully, Please Note following infromation for retrival: File object Name : "{}" Bucket Name : "njcpoc"'.format(
        fileName)
        return returnResult
    
        #return str(fileName+input1+input2+input3+input4+input5+input6+input7+input8+input9+input10+input11)
        



if __name__ == '__main__':
    app.run_server(debug=True)