import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
import botocore
from botocore.exceptions import ClientError

access_key_id="******************"
secret_access_key= "*********************"
    
s3 = boto3.resource('s3',region_name='us-east-1',
                        aws_access_key_id=access_key_id,
                        aws_secret_access_key= secret_access_key)

def merge_S3_file(bucket,docKey1,docKey2):
    
    obj = s3.Object(bucket,docKey1)
    body = obj.get()['Body'].read().decode()
    
    s3.Object(bucket,docKey2).put(Body=body)
    
    return True    

def lambda_handler(event, context):
    # TODO implement
    #eventBody = json.load(event)
    #eventData = eventBody.get('body')
   
    Docum1 = event['queryStringParameters']['Doc1']
    Docum2 = event['queryStringParameters']['Doc2']
    
    flag = merge_S3_file('njcpoc',Docum1,Docum2)

    if flag:
        message={'message':'Merge Complete'}
    else:    
        message={'message':'Error during merging '}
  

    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(message)
        #'isBase64Encoded':false
    }
