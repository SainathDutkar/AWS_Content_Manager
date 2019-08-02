import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

access_key_id="****************"
secret_access_key= "**********************"

dynamodb = boto3.resource('dynamodb',region_name='us-east-1',aws_access_key_id=access_key_id,aws_secret_access_key=secret_access_key)
table = dynamodb.Table('CMPOC')

def get_DocID(VenueId,DockCode,Year,Seq):
    
    DockNumber = VenueId+DockCode+Year+Seq
   
    response = table.query(
    KeyConditionExpression=Key('DocketNumber').eq(DockNumber))
    
    print(response)
    items= response['Items']
    
    S3ObjectData = []
    
    for x in items:
        S3ObjectData.append(x['S3ObjectKey'])

    return S3ObjectData    

def lambda_handler(event, context):
    # TODO implement
    #eventBody = json.load(event)
    #eventData = eventBody.get('body')

    
    venueID = event['queryStringParameters']['VenueId']
    DockCode = event['queryStringParameters']['DockCode']
    year = event['queryStringParameters']['Year']
    Sequence = event['queryStringParameters']['Seq']
    
    S3DocIDs = get_DocID(venueID,DockCode,year,Sequence)
    
    
    message={'message':'S3 Document Object Key : '}
   
    for x in S3DocIDs:
        message.update({S3DocIDs.index(x):x})
        

    
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(message)
        #'isBase64Encoded':false
    }