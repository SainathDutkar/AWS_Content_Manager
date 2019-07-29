# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 15:03:30 2019

@author: sainath.dutkar
"""

import logging
import boto3
from botocore.exceptions import ClientError


"""
def upload_file(file_name, bucket, object_name,DocSeq,
                DocType,Venue,Year,DocPrv,PrvReason,DocCode,DocDes,Mime,CourtDiv,ItemType):
    
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name
        
   
        
    # Upload the file
    s3_client = boto3.client('s3',aws_access_key_id=access_key_id,
         aws_secret_access_key= secret_access_key)
    try:
     
        response = s3_client.upload_file(file_name, bucket, object_name,ExtraArgs={'Metadata':
            {'Docket_Seq_Number': DocSeq,
             'Docket_Type_Code': DocType,
             'Docket_Venue_ID':Venue,
             'Docket_Court_Year':Year,
             'Document_Privacy_Code':DocPrv,
             'Document_Privacy_reason':PrvReason,
             'Document_Code':DocCode,
             'Document_Description':DocDes,
             'Document_Mime_Type':Mime,
             'EFILING_COURT_DIV':CourtDiv,
             'Item_Type':ItemType
             }})
    except ClientError as e:
        logging.error(e)
        return False
    return True
"""

def upload_file(file_name, bucket, object_name=None):
    
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name
     
        
    # Upload the file
    s3_client = boto3.client('s3',aws_access_key_id=access_key_id,
         aws_secret_access_key= secret_access_key)
    try:
     
        response = s3_client.upload_file(file_name, bucket, object_name,ExtraArgs={'Metadata':
            {'Docket_Seq_Number': '3005',
             'Docket_Type_Code': 'CL',
             'Docket_Venue_ID':'ATL',
             'Docket_Court_Year':'19',
             'Document_Privacy_Code':'abc',
             'Document_Privacy_reason':'abc',
             'Document_Code':'abc',
             'Document_Description':'abc',
             'Document_Mime_Type':'abc',
             'EFILING_COURT_DIV':'abc',
             'Item_Type':'abc'
             }})
    except ClientError as e:
        logging.error(e)
        return False
    return True


file = "Doc5.txt"
#upload_file(file,'njcpoc','Doc5','3005','CL','ATL','19','abcd','abcd','abcd','abcd','abcd','abcd','abcd')
upload_file(file,'njcpoc','Doc5')


#flag = upload_file(file,"njcpoc","Doc2")

#print(flag)
