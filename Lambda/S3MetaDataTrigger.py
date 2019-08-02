from __future__ import print_function
import boto3, logging

access_key_id="*****************"
secret_access_key= "******************"

s3 = boto3.client('s3',aws_access_key_id=access_key_id,
         aws_secret_access_key= secret_access_key)

dynamodb = boto3.resource('dynamodb',region_name='us-east-1',aws_access_key_id=access_key_id,aws_secret_access_key=secret_access_key)
table = dynamodb.Table('***')



logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    
  for record in event['Records']:
    bucket = record['s3']['bucket']['name']
    key = record['s3']['object']['key']
   
    response = s3.head_object(Bucket=bucket, Key=key)
    
    docket_venue_id = response['Metadata']['docket_venue_id']
    docket_court_year= response['Metadata']['docket_court_year']
    item_type = response['Metadata']['item_type']
    document_description = response['Metadata']['document_description']
    document_privacy_reason = response['Metadata']['document_privacy_reason']
    docket_type_code = response['Metadata']['docket_type_code']
    document_mime_type = response['Metadata']['document_mime_type']
    document_privacy_code = response['Metadata']['document_privacy_code']
    efiling_court_div = response['Metadata']['efiling_court_div']
    document_code = response['Metadata']['document_code']
    docket_seq_number = response['Metadata']['docket_seq_number']
    

    
    DocketNumber = docket_venue_id+docket_type_code+docket_court_year+docket_seq_number
    

  
    logger.info('Response: {}'.format(response))

    
    table.put_item(
            Item={
              'DocketNumber': DocketNumber,
              'S3ObjectKey': key,
              'S3BucketName': bucket,
              'Docket_Venue_ID' : docket_venue_id,
              'Docket_Court_Year': docket_court_year,
              'Item_Type' : item_type,
             'Document_Description' : document_description,
    'Document_Privacy_Reason' : document_privacy_reason,
    'Docket_Type_Code' : docket_type_code,
    'Document_mime_Type' : document_mime_type,
    'Document_Privacy_Code' : document_privacy_code,
    'Efiling_court_Div' : efiling_court_div,
    'document_code' : document_code,
    'docket_seq_number' : docket_seq_number
   
            }
      )
